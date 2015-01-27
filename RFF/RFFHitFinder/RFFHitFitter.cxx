/*!
 * Title:   RFFHitFitter Class
 * Author:  Wes Ketchum (wketchum@lanl.gov)
 *
 * Description: 
 * Class that does the base RFF algorithm. RFF works by simplifiying a Gaussian
 * fit by dividing a pulse by its derivative. for a Guassian, the result is a
 * line, with the slope and intercept related to the sigma and mean of the 
 * Gaussian. 
 *
 * Input:  Signal (vector of floats)
 * Output: Guassian means and sigmas
*/

#include "RFFHitFitter.h"
#include <iostream>
#include <cmath>

hit::RFFHitFitter::RFFHitFitter(float max_mean, unsigned int min_multi)
{
  fMeanMatchThreshold = max_mean;
  fMinMergeMultiplicity = min_multi;
  
  if(fMinMergeMultiplicity==0)
   fMinMergeMultiplicity=1;
}

void hit::RFFHitFitter::RunFitter(const std::vector<float>& signal)
{
  CalculateAllMeansAndSigmas(signal);
  CreateMergeVector();
  CalculateMergedMeansAndSigmas();
}

void hit::RFFHitFitter::CalculateAllMeansAndSigmas(const std::vector<float>& signal)
{
  if(signal.size()<=2) return;
  
  float prev_dev=0,this_dev=0;; 
  float slope=0; float sigma=0; 
  float intercept=0; float mean=0;
  for(size_t i_tick=1; i_tick < signal.size()-1; i_tick++){
    
    this_dev = 0.5*(signal[i_tick+1]-signal[i_tick-1])/signal[i_tick];
    slope = this_dev - prev_dev;
    
    prev_dev = this_dev;
    
    if(slope>=0)
      continue;
    
    sigma = std::sqrt(-1/slope); 
    intercept = 0.5*(signal[i_tick+1]-signal[i_tick-1])/signal[i_tick] - slope*i_tick;
    mean = -1*intercept/slope;
    
    fSignalSet.insert(std::make_pair(mean,sigma));
    
  }
  
}

void hit::RFFHitFitter::CreateMergeVector()
{
  fMergeVector.clear(); fMergeVector.reserve( fSignalSet.size() );
  
  float prev_mean=-999;
  for(std::multiset<MeanSigmaPair>::iterator it=fSignalSet.begin();
      it!=fSignalSet.end();
      it++)
    {
      if( std::abs(it->first - prev_mean) > fMeanMatchThreshold )
	fMergeVector.push_back( std::vector< std::multiset<MeanSigmaPair>::iterator >(1,it) );
      else
	fMergeVector.back().push_back(it);
      prev_mean = it->first;
    }
}

void hit::RFFHitFitter::CalculateMergedMeansAndSigmas()
{
  fMeanVector.reserve(fMergeVector.size());
  fSigmaVector.reserve(fMergeVector.size());
  fMeanErrorVector.reserve(fMergeVector.size());
  fSigmaErrorVector.reserve(fMergeVector.size());

  for(size_t i_col=0; i_col<fMergeVector.size(); i_col++){

    if(fMergeVector[i_col].size()<fMinMergeMultiplicity) continue;

    fMeanVector.push_back(0.0);
    fSigmaVector.push_back(0.0);

    for(auto const& sigpair : fMergeVector[i_col]){
      fMeanVector.back() += sigpair->first;
      fSigmaVector.back() += sigpair->second;
    }

    fMeanVector.back() /= fMergeVector[i_col].size();
    fSigmaVector.back() /= fMergeVector[i_col].size();


    fMeanErrorVector.push_back(0.0);
    fSigmaErrorVector.push_back(0.0);

    for(auto const& sigpair : fMergeVector[i_col]){
      fMeanErrorVector.back() += 
	(sigpair->first-fMeanVector.back())*(sigpair->first-fMeanVector.back());
      fSigmaErrorVector.back() += 
	(sigpair->second-fSigmaVector.back())*(sigpair->second-fSigmaVector.back());
    }

    fMeanErrorVector.back() = std::sqrt(fMeanErrorVector.back()) / fMergeVector[i_col].size();
    fSigmaErrorVector.back() = std::sqrt(fSigmaErrorVector.back()) / fMergeVector[i_col].size();

  }

}

void hit::RFFHitFitter::GaussianElimination(const std::vector< std::vector<float> >& scaled_distances,
					    const std::vector<float>& peak_heights,
					    std::vector<float>& solutions)
{
  const size_t N_PEAKS = scaled_distances.size();

  if(peak_heights.size() != N_PEAKS )
    throw std::runtime_error("ERROR in RFFHitFitter:  cannot do Guassian elimination of non-square matrix");
  
  solutions.resize(N_PEAKS,0.0);
  std::vector< std::vector<float> > matrix(N_PEAKS,std::vector<float>(N_PEAKS+1,0.0)); //N_PEAKS rows, N_PEAKS+1 columns for augmented matrix

  for(size_t i=0; i<N_PEAKS; i++){
    std::vector<float> const& this_row = scaled_distances[i];

    if(this_row.size() != N_PEAKS)
      throw std::runtime_error("ERROR in RFFHitFitter:  cannot do Guassian elimination of non-square matrix");

    for(size_t j=0; j<N_PEAKS; j++)
      if(this_row[j] < 4.0)
	matrix[i][j] = GAUS_5SIGMA_TENTH[std::floor(this_row[j]*10 + 0.5)];
    
    matrix[i][N_PEAKS] = peak_heights[i];

  }//end filling augmented matrix

  //now, eliminate
  for(size_t i=0; i<N_PEAKS; i++){
    for(size_t j=i+1; j<N_PEAKS; j++){
      float scale_val = matrix[j][i] / matrix[i][i];
      for(size_t k=i; k<N_PEAKS+1; k++)
	matrix[j][k] -= matrix[i][k]*scale_val;
    }
  }//end elimination

  //now fill solutions
  for(int i=N_PEAKS-1; i>=0; i--){
    solutions[i] = matrix[i][N_PEAKS];

    for(size_t j=i+1; j<N_PEAKS; j++)
      solutions[i] -= matrix[i][j]*solutions[j];

    solutions[i] /= matrix[i][i];
  }//end filling solutions

}

void hit::RFFHitFitter::ClearResults()
{
  fMeanVector.clear();
  fSigmaVector.clear();
  fSignalSet.clear();
  fMergeVector.clear();
}

void hit::RFFHitFitter::PrintResults()
{
    
  std::cout << "InitialSignalSet" << std::endl;
  
  for(auto const& sigpair : fSignalSet)
    std::cout << "\t" << sigpair.first << " / " << sigpair.second << std::endl;
  
  std::cout << "\nNHits = " << NHits() << std::endl;
  std::cout << "\tMean / Sigma" << std::endl;
  for(size_t i=0; i<NHits(); i++)
    std::cout << "\t" 
	      << fMeanVector[i] <<  " +- " << fMeanErrorVector[i] << " / " 
	      << fSigmaVector[i] << " +- " << fSigmaErrorVector[i] 
	      << std::endl;
}
