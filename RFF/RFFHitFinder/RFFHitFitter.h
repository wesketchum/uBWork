#ifndef RFFHITFITTER_H
#define RFFHITFITTER_H

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

#include <vector>
#include <set>

namespace hit{

  struct SignalSetComp{
    bool operator() (const std::pair<float,float>& lhs,
		     const std::pair<float,float>& rhs) const
    { return lhs.first < rhs.first; } 		     
  };

  class RFFHitFitter {

    typedef std::pair<float,float> MeanSigmaPair;
    
  public:
    RFFHitFitter(float,unsigned int);

    void RunFitter(const std::vector<float>& signal);

    const std::vector<float>& MeanVector() { return fMeanVector; }
    const std::vector<float>& SigmaVector() { return fSigmaVector; }
    unsigned int NHits() { return fMeanVector.size(); }

    void ClearResults();

    void PrintResults();
			 
  private:
    float fMeanMatchThreshold;
    unsigned int fMinMergeMultiplicity;

    std::vector<float> fMeanVector;
    std::vector<float> fSigmaVector;
    std::vector<float> fMeanErrorVector;
    std::vector<float> fSigmaErrorVector;

    std::multiset< MeanSigmaPair, SignalSetComp > fSignalSet;
    std::vector< std::vector< std::multiset<MeanSigmaPair>::iterator > >
      fMergeVector;

    void CalculateAllMeansAndSigmas(const std::vector<float>& signal);
    void CalculateMergedMeansAndSigmas();
    void CreateMergeVector();

  };

}

#endif
