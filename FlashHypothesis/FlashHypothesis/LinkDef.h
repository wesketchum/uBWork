//
// cint script to generate libraries
// Declaire namespace & classes you defined
// #pragma statement: order matters! Google it ;)
//

#ifdef __CINT__
#pragma link off all globals;
#pragma link off all classes;
#pragma link off all functions;

#pragma link C++ class sample+;
#pragma link C++ namespace opdet;
#pragma link C++ class opdet::FlashHypothesis+;
#pragma link C++ class opdet::FlashHypothesisCollection+;
#pragma link C++ class opdet::FlashHypothesisCalculator+;
#pragma link C++ class opdet::FlashUtilities+;
#pragma link C++ class opdet::FlashHypothesisComparison+;

#pragma link C++ namespace sim;
#pragma link C++ class sim::OnePhoton;
#pragma link C++ class sim::SimPhotons;

#pragma link C++ class opdet::SimPhotonCounter;
//ADD_NEW_CLASS ... do not change this line
#endif
