from ROOT import *
import numpy as np
from array import array

"""Após a leitura dos arquivos, definiu-se histogramas correspondentes aos dados, que foram preenchidos em um loop."""

arquivo = TFile("monitoring_PbPb_5k.root", "READ")
arquivo2 = TFile("monitoring_alps_3GeV_100k.root", "READ")
tree = arquivo.Hlt1Bs2GammaGamma.monitor_tree_twoclusters
tree2 = arquivo2.Hlt1Bs2GammaGamma.monitor_tree_twoclusters

histogramaMass = TH1F("Mass", "Mass - PbPb", 100, 0, 6000)
histogramaEt = TH1F("Et", "Et - PbPb", 100, 0, 5200)
histogramaDistance = TH1F("Distance", "Distance - PbPb", 100, 0, 8400)
histogramax1 = TH1F("x1", "x1 - PbPb", 100, -4000, 4000)
histogramax2 = TH1F("x2", "x2 - PbPb", 100, -4000, 4000)
histogramay1 = TH1F("y1", "y1 - PbPb", 100, -3200, 3200)
histogramay2 = TH1F("y2", "y2 - PbPb", 100, -3200, 3200)
histogramaet1 = TH1F("et1", "et1 - PbPb", 100, 0, 3900)
histogramaet2 = TH1F("et2", "et2 - PbPb", 100, 0, 3900)
histogramae19_1 = TH1F("e19_1", "e19_1 - PbPb", 100, 0.1, 1.01)
histogramae19_2 = TH1F("e19_2", "e19_2 - PbPb", 100, 0.1, 1.01)
histogramanum_twoclusters = TH1F("num_twoclusters", "num_twoclusters - PbPb", 100, 0, 40000)
histogramaevent_number = TH1F("event_number", "event_number - PbPb", 100, 0, 505)


for i in range(0,tree.GetEntries()):
    tree.GetEntry(i)
    histogramaMass.Fill(tree.Mass)
    histogramaEt.Fill(tree.Et)
    histogramaDistance.Fill(tree.Distance)
    histogramax1.Fill(tree.x1)
    histogramax2.Fill(tree.x2)
    histogramay1.Fill(tree.y1)
    histogramay2.Fill(tree.y2)
    histogramaet1.Fill(tree.et1)
    histogramaet2.Fill(tree.et2)
    histogramae19_1.Fill(tree.e19_1)
    histogramae19_2.Fill(tree.e19_2)
    histogramanum_twoclusters.Fill(tree.num_twoclusters)
    histogramaevent_number.Fill(tree.event_number)
    
    
    

    

hist2dAlp = TH2F("Mass x Et - Alp", "Mass x Et - Alp", 100, 0, 4400, 100, 0, 2500)
hist2dAlp.SetBit(TH1.kNoStats)  #Retirar Stats Box do Histograma
hist2dAlp.SetContour(1000)

histograma2Mass = TH1F("Mass", "Mass - Alp", 100, 0, 4400)
histograma2Et = TH1F("Et", "Et - Alp", 100, 0, 2500)
histograma2Distance = TH1F("Distance", "Distance - Alp", 100, 0, 9100)
histograma2x1 = TH1F("x1", "x1 - Alp", 100, -4000, 4000)
histograma2x2 = TH1F("x2", "x2 - Alp", 100, -4000, 4000)
histograma2y1 = TH1F("y1", "y1 - Alp", 100, -3200, 3200)
histograma2y2 = TH1F("y2", "y2 - Alp", 100, -3200, 3200)
histograma2et1 = TH1F("et1", "et1 - Alp", 100, 0, 2300)
histograma2et2 = TH1F("et2", "et2 - Alp", 100, 0, 2300)
histograma2e19_1 = TH1F("e19_1", "e19_1 - Alp", 100, 0.2, 1.01)
histograma2e19_2 = TH1F("e19_2", "e19_2 - Alp", 100, 0.2, 1.01)
histograma2num_twoclusters = TH1F("num_twoclusters", "num_twoclusters - Alp", 100, 0, 30)
histograma2event_number = TH1F("event_number", "event_number - Alp", 100, 0, 1000)



for i in range(0,tree2.GetEntries()):
    tree2.GetEntry(i)
    hist2dAlp.Fill(tree2.Mass, tree2.Et)
    histograma2Mass.Fill(tree2.Mass)
    histograma2Et.Fill(tree2.Et)
    histograma2Distance.Fill(tree2.Distance)
    histograma2x1.Fill(tree2.x1)
    histograma2x2.Fill(tree2.x2)
    histograma2y1.Fill(tree2.y1)
    histograma2y2.Fill(tree2.y2)
    histograma2et1.Fill(tree2.et1)
    histograma2et2.Fill(tree2.et2)
    histograma2e19_1.Fill(tree2.e19_1)
    histograma2e19_2.Fill(tree2.e19_2)
    histograma2num_twoclusters.Fill(tree2.num_twoclusters)
    histograma2event_number.Fill(tree2.event_number)
    
    


    
"""Criação do TCanvas e plot dos histogramas MB"""
  
canvas = TCanvas("Canvas", "Canvas", 800, 600)


"""Função Scale utilizada para normalizar os histogramas"""


histogramaMass.Scale(1/histogramaMass.Integral())
histogramaMass.Draw("HIST")
canvas.Draw()
canvas.Print("Mass.gif")

histogramaEt.Scale(1/histogramaEt.Integral())
histogramaEt.Draw("HIST")
canvas.Draw()
canvas.Print("Et.gif")

histogramaDistance.Scale(1/histogramaDistance.Integral())
histogramaDistance.Draw("HIST")
canvas.Draw()
canvas.Print("Distance.gif")

histogramax1.Scale(1/histogramax1.Integral())
histogramax1.Draw("HIST")
canvas.Draw()
canvas.Print("x1.gif")

histogramax2.Scale(1/histogramax2.Integral())
histogramax2.Draw("HIST")
canvas.Draw()
canvas.Print("x2.gif")

histogramay1.Scale(1/histogramay1.Integral())
histogramay1.Draw("HIST")
canvas.Draw()
canvas.Print("y1.gif")

histogramay2.Scale(1/histogramay2.Integral())
histogramay2.Draw("HIST")
canvas.Draw()
canvas.Print("y2.gif")

histogramaet1.Scale(1/histogramaet1.Integral())
histogramaet1.Draw("HIST")
canvas.Draw()
canvas.Print("et1.gif")

histogramaet2.Scale(1/histogramaet2.Integral())
histogramaet2.Draw("HIST")
canvas.Draw()
canvas.Print("et2.gif")

histogramae19_1.Scale(1/histogramae19_1.Integral())
histogramae19_1.Draw("HIST")
canvas.Draw()
canvas.Print("e19_1.gif")

histogramae19_2.Scale(1/histogramae19_2.Integral())
histogramae19_2.Draw("HIST")
canvas.Draw()
canvas.Print("e19_2.gif")

histogramanum_twoclusters.Scale(1/histogramanum_twoclusters.Integral())
histogramanum_twoclusters.Draw("HIST")
canvas.Draw()
canvas.Print("num_twoclusters.gif")

histogramaevent_number.Scale(1/histogramaevent_number.Integral())
histogramaevent_number.Draw("HIST")
canvas.Draw()
canvas.Print("event_number.gif")


"""Plot dos histogramas Alp, da mesma forma que o MB"""

histograma2Mass.Scale(1/histograma2Mass.Integral())
histograma2Mass.Draw("HIST")
canvas.Draw()
canvas.Print("MassAlp.gif")

histograma2Et.Scale(1/histograma2Et.Integral())
histograma2Et.Draw("HIST")
canvas.Draw()
canvas.Print("EtAlp.gif")

histograma2Distance.Scale(1/histograma2Distance.Integral())
histograma2Distance.Draw("HIST")
canvas.Draw()
canvas.Print("DistanceAlp.gif")

histograma2x1.Scale(1/histograma2x1.Integral())
histograma2x1.Draw("HIST")
canvas.Draw()
canvas.Print("x1Alp.gif")

histograma2x2.Scale(1/histograma2x2.Integral())
histograma2x2.Draw("HIST")
canvas.Draw()
canvas.Print("x2Alp.gif")

histograma2y1.Scale(1/histograma2y1.Integral())
histograma2y1.Draw("HIST")
canvas.Draw()
canvas.Print("y1Alp.gif")

histograma2y2.Scale(1/histograma2y2.Integral())
histograma2y2.Draw("HIST")
canvas.Draw()
canvas.Print("y2Alp.gif")

histograma2et1.Scale(1/histograma2et1.Integral())
histograma2et1.Draw("HIST")
canvas.Draw()
canvas.Print("et1Alp.gif")

histograma2et2.Scale(1/histograma2et2.Integral())
histograma2et2.Draw("HIST")
canvas.Draw()
canvas.Print("et2Alp.gif")

histograma2e19_1.Scale(1/histograma2e19_1.Integral())
histograma2e19_1.Draw("HIST")
canvas.Draw()
canvas.Print("e19_1Alp.gif")

histograma2e19_2.Scale(1/histograma2e19_2.Integral())
histograma2e19_2.Draw("HIST")
canvas.Draw()
canvas.Print("e19_2Alp.gif")

histograma2num_twoclusters.Scale(1/histograma2num_twoclusters.Integral())
histograma2num_twoclusters.Draw("HIST")
canvas.Draw()
canvas.Print("num_twoclustersAlp.gif")

histograma2event_number.Scale(1/histograma2event_number.Integral())
histograma2event_number.Draw("HIST")
canvas.Draw()
canvas.Print("event_numberAlp.gif")

"""Plot Histograma 2d"""

gStyle.SetPalette(kRainBow)
hist2dAlp.Draw("COLZ")
canvas.Draw()
canvas.Print("Mass_x_Et-Alp.pdf")


"""Plot comparação dos histogramas. A criação de um novo canvas serve para não confundir e desconfigurar possíveis plots."""

canvas2 = TCanvas("Canvas2", "Canvas2", 800, 600)

gStyle.SetOptStat(0)

canvas2.cd()

histograma2Mass.SetLineColor(kRed)
histograma2Mass.Draw("HIST")
histogramaMass.Draw("HIST SAME")
canvas2.Draw()
gPad.BuildLegend()
canvas2.Print("MassComp.gif")

histograma2Et.SetLineColor(kRed)
histograma2Et.Draw("HIST")
histogramaEt.Draw("HIST SAME")
canvas2.Draw()
gPad.BuildLegend()
canvas2.Print("EtComp.gif")

histograma2Distance.SetLineColor(kRed)
histograma2Distance.Draw("HIST")
histogramaDistance.Draw("HIST SAME")
canvas2.Draw()
gPad.BuildLegend()
canvas2.Print("DistanceComp.gif")

histograma2x1.SetLineColor(kRed)
histograma2x1.Draw("HIST")
histogramax1.Draw("HIST SAME")
canvas2.Draw()
gPad.BuildLegend()
canvas2.Print("x1Comp.gif")

histograma2x2.SetLineColor(kRed)
histograma2x2.Draw("HIST")
histogramax2.Draw("HIST SAME")
canvas2.Draw()
gPad.BuildLegend()
canvas2.Print("x2Comp.gif")

histograma2y1.SetLineColor(kRed)
histograma2y1.Draw("HIST")
histogramay1.Draw("HIST SAME")
canvas2.Draw()
gPad.BuildLegend()
canvas2.Print("y1Comp.gif")

histograma2y2.SetLineColor(kRed)
histograma2y2.Draw("HIST")
histogramay2.Draw("HIST SAME")
canvas2.Draw()
gPad.BuildLegend()
canvas2.Print("y2Comp.gif")

histograma2et1.SetLineColor(kRed)
histograma2et1.Draw("HIST")
histogramaet1.Draw("HIST SAME")
canvas2.Draw()
gPad.BuildLegend()
canvas2.Print("et1Comp.gif")

histograma2et2.SetLineColor(kRed)
histograma2et2.Draw("HIST")
histogramaet2.Draw("HIST SAME")
canvas2.Draw()
gPad.BuildLegend()
canvas2.Print("et2Comp.gif")

histograma2e19_1.SetLineColor(kRed)
histograma2e19_1.Draw("HIST")
histogramae19_1.Draw("HIST SAME")
canvas2.Draw()
gPad.BuildLegend()
canvas2.Print("e19_1Comp.gif")

histograma2e19_2.SetLineColor(kRed)
histograma2e19_2.Draw("HIST")
histogramae19_2.Draw("HIST SAME")
canvas2.Draw()
gPad.BuildLegend()
canvas2.Print("e19_2Comp.gif")

histograma2num_twoclusters.SetLineColor(kRed)
histogramanum_twoclusters.Draw("HIST")
histograma2num_twoclusters.Draw("HIST SAME")
canvas2.Draw()
gPad.BuildLegend()
canvas2.Print("num_twoclustersComp.gif")

histograma2event_number.SetLineColor(kRed)
histogramaevent_number.Draw("HIST")
histograma2event_number.Draw("HIST SAME")
canvas2.Draw()
gPad.BuildLegend()
canvas2.Print("event_numberComp.gif")


"""Fit no Mass ALP, criando uma array para os parâmetros e os guardando, a serem utilizados depois na função 'total' """

par = array('d',5*[0.])

func = TF1("func", "gaus", 2600, 3400)
func2 = TF1("func2", "pol1", 2000, 4000)
total = TF1("total", "gaus(0)+pol1(3)", 2000, 4000)

func.SetLineColor(kBlack)
func2.SetLineColor(kGreen)
total.SetLineColor(kRed)

canvas3 = TCanvas("Canvas3", "Canvas3", 800, 600)


canvas3.cd()

histograma2Mass.Fit("func","R")
histograma2Mass.Fit("func2","R+")

par1 = func.GetParameters()
par2 = func2.GetParameters()

par[0], par[1], par[2] = par1[0], par1[1], par1[2]
par[3], par[4] = par2[0], par2[1]
total.SetParameters(par)
histograma2Mass.Sumw2(kFALSE)    #para remover as barras de erro
histograma2Mass.Draw("SAME")
histograma2Mass.Fit("total","R+")
histograma2Mass.SetLineColor(kBlue)
legend = TLegend(0.67,0.75,0.89,0.89)
legend.AddEntry(func, "Gauss", "L")
legend.AddEntry(func2, "Pol1", "L")
legend.AddEntry(total, "Total", "L")
legend.Draw()
canvas3.Draw()
canvas3.Print("MassAlpFit.gif")













































