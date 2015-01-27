#ifndef SIMPHOTONS_H
#define SIMPHOTONS_H

#include "TVector3.h"
#include <vector>

namespace sim{
  
  class OnePhoton 
  {
  public:
    OnePhoton() {}    
    bool           SetInSD;
    TVector3       InitialPosition;
    TVector3       FinalLocalPosition; // in cm
    float          Time;
    float          Energy;
  };

  
  class SimPhotons : public std::vector<OnePhoton> 
  {
  public:
    SimPhotons();

    void Push_back(const OnePhoton& ph) { this->push_back(ph); }
    
    int  fOpChannel;  /// volume number for the OpDet
    
#ifndef __GCCXML__
  public:
    
    typedef std::vector<OnePhoton>             list_type;
    typedef list_type::value_type              value_type;
    typedef list_type::iterator                iterator;
    typedef list_type::const_iterator          const_iterator;
    typedef list_type::reverse_iterator        reverse_iterator;
    typedef list_type::const_reverse_iterator  const_reverse_iterator;
    typedef list_type::size_type               size_type;
    typedef list_type::difference_type         difference_type;
    
    // define addition operators for combining hits
    //   (add all photons to one vector)
    SimPhotons& operator+=(const SimPhotons &rhs);
    const SimPhotons operator+(const SimPhotons &rhs) const;
    
    int       OpChannel() const;
    void      SetChannel(int ch);
    
#endif
    
  };
    
}

#ifndef __GCCXML__

inline int         sim::SimPhotons::OpChannel()       const                     { return fOpChannel;      }
inline void        sim::SimPhotons::SetChannel(int ch)                          { fOpChannel = ch;        }
#endif

#endif
