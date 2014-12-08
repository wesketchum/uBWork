//ROOT macro for comparing hits in HitAnaAlg
//
int analyzeFile(TString file_name){
  
  TFile f(file_name,"READ");
  TDirectoryFile* dir = f.Get("hitana");
  TTree* wdtree = dir->Get("wireDataTree");

}
