import sys
from ROOT import gSystem
gSystem.Load("libOverlay_DataOverlay")
from ROOT import sample

try:

    print "PyROOT recognized your class %s" % str(sample)

except NameError:

    print "Failed importing DataOverlay..."

sys.exit(0)

