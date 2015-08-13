#ifndef OVERLAY_DATAOVERLAY_RAWDIGITADDER_HARDSATURATE_CXX
#define OVERLAY_DATAOVERLAY_RAWDIGITADDER_HARDSATURATE_CXX

#include "RawDigitAdder_HardSaturate.h"
#include <limits>
#include <stdexcept>

RawDigitAdder_HardSaturate::RawDigitAdder_HardSaturate(bool t):
  RawDigitAdder(t),
  _max(std::numeric_limits<short>::max())
{}

void RawDigitAdder_HardSaturate::SetSaturationPoint(short x)
{
  if(x<0){
    if(_throw)
      throw std::runtime_error("Error in RawDigitAdder_HardSaturate::SetSaturationPoint : point < 0");
    return;
  }
  _max = x;
}

void RawDigitAdder_HardSaturate::AddRawDigit(short const& d1, short const& d2, short& d_out)
{
  d_out = d1 + d2;  
  FixOverflow(d_out);
  if(d_out > _max)
    d_out=_max;
}

#endif
