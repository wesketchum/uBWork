from ROOT import hit
from ROOT.hit import RegionAboveThresholdFinder

from ROOT import vector

signal = vector('float')(15,1.0)
signal[2] = 3.5
signal[3] = 4.5
signal[4] = 5.5
signal[5] = 4.5
signal[6] = 3.5
signal[10] = 3.5
signal[11] = 4.5
signal[12] = 2.5
signal[13] = 4.5
signal[14] = 4.5

finder = RegionAboveThresholdFinder(3.0)

start_ticks = vector('unsigned int')()
end_ticks = vector('unsigned int')()

finder.FillStartAndEndTicks(signal,start_ticks,end_ticks)

print start_ticks.size(),end_ticks.size()
for x in range(0,start_ticks.size()):
    print "\t",start_ticks[x],end_ticks[x]


from ROOT.hit import RFFHitFitter

fitter = RFFHitFitter(1.0,2)

fitter.RunFitter(signal)
fitter.PrintResults()
