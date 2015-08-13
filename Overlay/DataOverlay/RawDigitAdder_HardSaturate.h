/**
 * \file RawDigitAdder_HardSaturate.h
 *
 * \ingroup DataOverlay
 * 
 * \brief Defintion for a class to add two vectors together,
 *        and give an "added" waveform. Takes in a saturation point.
 *
 *
 * @author wketchum
 */

/** \addtogroup DataOverlay

    @{*/
#ifndef OVERLAY_DATAOVERLAY_RAWDIGITADDER_HARDSATURATE_H
#define OVERLAY_DATAOVERLAY_RAWDIGITADDER_HARDSATURATE_H

#include <vector>
#include <string>
#include "RawDigitAdder.h"

/**
   \class RawDigitAdder_HardSaturate
   Add two vectors together. Needs a saturation point set, where
   everything above that point is just the max.
   
*/
class RawDigitAdder_HardSaturate : public RawDigitAdder {

public:

  RawDigitAdder_HardSaturate(bool t=true);
  void SetSaturationPoint(short x);

  std::string Name() { return "RawDigitAdder_HardSaturate"; }
  
 private:

  short _max;
  void AddRawDigit( short const&, short const&, short&);

};

#endif
/** @} */ // end of doxygen group 

