#include "Simulation/SimPhotons.h"

//----------------------------------------------------------------------------
sim::SimPhotons::SimPhotons()
{
}

//----------------------------------------------------------------------------
sim::SimPhotons & sim::SimPhotons::operator+=(const SimPhotons &rhs)
{
  for(SimPhotons::const_iterator it = rhs.begin(); it!=rhs.end(); it++){
    push_back(*it);
  }
  return *this;
}

//----------------------------------------------------------------------------
const sim::SimPhotons sim::SimPhotons::operator+(const SimPhotons &rhs) const
{
  return SimPhotons(*this)+=rhs;
}
