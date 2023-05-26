# Antes de rodar, verifique se fez "source root/bin/thisroot.sh" no seu environment - deve ser feito no terminal do ubuntu e não aqui i.e antes de abrir o vs code

#%% Import ROOT
import ROOT
#%%
f = ROOT.TF1("f1", "sin(x)/x", 0., 10.)
c = ROOT.TCanvas()
f.Draw()
c.Draw()
#%%
h = ROOT.TH1F("myHist", "myTitle", 64, -4, 4)
h.FillRandom("gaus")
d = ROOT.TCanvas()
h.Draw()
d.Draw()
# %%
