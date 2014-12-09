from ROOT import *

def HistShowOverflow(hist):
    under = hist.GetBinContent(0)
    bin1 = hist.GetBinContent(1)
    hist.SetBinContent(1,bin1+under)
    hist.SetBinContent(0,0)
    over = hist.GetBinContent(hist.GetNbinsX()+1)
    bin_last = hist.GetBinContent(hist.GetNbinsX())
    hist.SetBinContent(hist.GetNbinsX(),bin_last+over)
    hist.SetBinContent(hist.GetNbinsX()+1,0)
    

