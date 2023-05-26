from ROOT import *
import numpy as np
from array import array

"""Fit no Mass do ALP para cada ADC, criando uma array para os parâmetros e os guardando, a serem utilizados depois na função 'total', e, após o fit da mesma, retornar os novos parâmetros gerados por esta nova função às funções originais.
Também é calculada a integral da função gaussiana presente em cada fit."""

gROOT.SetBatch(True)
gSystem.RedirectOutput("adccompet.txt")
arquivo = TFile("monitoring_alps_3GeV_100k_adc_0.root", "READ")
arquivo2 = TFile("monitoring_alps_3GeV_100k_adc_5.root", "READ")
arquivo3 = TFile("monitoring_alps_3GeV_100k_adc_10.root", "READ")
arquivo4 = TFile("monitoring_alps_3GeV_100k_adc_15.root", "READ")
arquivo5 = TFile("monitoring_alps_3GeV_100k_adc_30.root", "READ")
arquivo6 = TFile("monitoring_alps_3GeV_100k_adc_50.root", "READ")

tree = arquivo.Hlt1Bs2GammaGamma.monitor_tree_twoclusters
tree2 = arquivo2.Hlt1Bs2GammaGamma.monitor_tree_twoclusters
tree3 = arquivo3.Hlt1Bs2GammaGamma.monitor_tree_twoclusters
tree4 = arquivo4.Hlt1Bs2GammaGamma.monitor_tree_twoclusters
tree5 = arquivo5.Hlt1Bs2GammaGamma.monitor_tree_twoclusters
tree6 = arquivo6.Hlt1Bs2GammaGamma.monitor_tree_twoclusters


histogramaMass = TH1F("Mass", "Mass - Alp", 100, 0, 4400)
histograma2Mass = TH1F("Mass2", "Mass - Alp", 100, 0, 4400)
histograma3Mass = TH1F("Mass3", "Mass - Alp", 100, 0, 4400)
histograma4Mass = TH1F("Mass4", "Mass - Alp", 100, 0, 4400)
histograma5Mass = TH1F("Mass5", "Mass - Alp", 100, 0, 4400)
histograma6Mass = TH1F("Mass6", "Mass - Alp", 100, 0, 4400)


for i in range(0,tree.GetEntries()):
    tree.GetEntry(i)
    tree2.GetEntry(i)
    tree3.GetEntry(i)
    tree4.GetEntry(i)
    tree5.GetEntry(i)
    tree6.GetEntry(i)
    if tree.Et<500:
        histogramaMass.Fill(tree.Mass)
    if tree2.Et<500:
        histograma2Mass.Fill(tree2.Mass)
    if tree3.Et<500:
        histograma3Mass.Fill(tree3.Mass)
    if tree4.Et<500:
        histograma4Mass.Fill(tree4.Mass)
    if tree5.Et<500:
        histograma5Mass.Fill(tree5.Mass)
    if tree6.Et<500:
        histograma6Mass.Fill(tree6.Mass)


gStyle.SetOptStat(0)


#Para ADC 0


par = array('d',7*[0.])

func = TF1("func", "gausn", 2400, 3400)
func2 = TF1("func2", "pol3", 2000, 4000)
total = TF1("total", "gausn(0)+pol3(3)", 2000, 4000)

func.SetLineColor(kBlack)
func2.SetLineColor(kGreen)
total.SetLineColor(kRed)

canvas = TCanvas("Canvas", "Canvas", 800, 600)


canvas.cd()

histograma2Mass.Fit("func","0R")
histograma2Mass.Fit("func2","0R+")

par1 = func.GetParameters()
par2 = func2.GetParameters()

par[0], par[1], par[2] = par1[0], par1[1], par1[2]
par[3], par[4], par[5], par[6] = par2[0], par2[1], par2[2], par2[3]
total.SetParameters(par)
histogramaMass.Draw("SAME")
histogramaMass.Fit("total","R+")

par = total.GetParameters()

par1[0], par1[1], par1[2] = par[0], par[1], par[2]
func.SetParameters(par1)

Mean, Sigma = par[1], par[2]


par2[0], par2[1], par2[2], par2[3] = par[3], par[4], par[5], par[6]
func2.SetParameters(par2)
func.Draw("SAME")
func2.Draw("SAME")


integralgaus = par[0]/histogramaMass.GetBinWidth(2)
histogramaMass.SetLineColor(kBlue)
histogramaMass.GetXaxis().SetTitle("Mass")
histogramaMass.GetYaxis().SetTitle("Quantity")

legend = TLegend(0.67,0.75,0.89,0.89)
legend.AddEntry(func, "Gauss", "L")
legend.AddEntry(func2, "Pol3", "L")
legend.AddEntry(total, "Total", "L")
legend.Draw()
canvas.Draw()
canvas.Print("ADC0et.gif")
print(f"\n\nThe integral of the Gaussian for the ADC 0 Fit is = {integralgaus}\n\n" )


#Para ADC 5


par = array('d',7*[0.])

func3 = TF1("func3", "gausn", 2500, 3300)
func4 = TF1("func4", "pol3", 2000, 3900)
total2 = TF1("total2", "gausn(0)+pol3(3)", 2000, 3900)

func3.SetLineColor(kBlack)
func4.SetLineColor(kGreen)
total2.SetLineColor(kRed)

canvas2 = TCanvas("Canvas2", "Canvas2", 800, 600)


canvas2.cd()

histograma2Mass.Fit("func3","0R")
histograma2Mass.Fit("func4","0R+")

par1 = func3.GetParameters()
par2 = func4.GetParameters()

par[0], par[1], par[2] = par1[0], par1[1], par1[2]
par[3], par[4], par[5], par[6] = par2[0], par2[1], par2[2], par2[3]
total2.SetParameters(par)
histograma2Mass.Draw("SAME")
histograma2Mass.Fit("total2","R+")

par = total2.GetParameters()

par1[0], par1[1], par1[2] = par[0], par[1], par[2]
func3.SetParameters(par1)

Mean2, Sigma2 = par[1], par[2]


par2[0], par2[1], par2[2], par2[3] = par[3], par[4], par[5], par[6]
func4.SetParameters(par2)
func3.Draw("SAME")
func4.Draw("SAME")


integral2gaus = par[0]/histograma2Mass.GetBinWidth(2)
histograma2Mass.SetLineColor(kBlue)
histograma2Mass.GetXaxis().SetTitle("Mass")
histograma2Mass.GetYaxis().SetTitle("Quantity")

legend = TLegend(0.67,0.75,0.89,0.89)
legend.AddEntry(func3, "Gauss", "L")
legend.AddEntry(func4, "Pol3", "L")
legend.AddEntry(total2, "Total", "L")
legend.Draw()
canvas2.Draw()
canvas2.Print("ADC5et.gif")
print(f"\n\nThe integral of the Gaussian for ADC 5 Fit is = {integral2gaus}\n\n" )


#Para ADC 10


par = array('d',7*[0.])

func5 = TF1("func5", "gausn", 2300, 3300)
func6 = TF1("func6", "pol3", 2000, 3800)
total3 = TF1("total3", "gausn(0)+pol3(3)", 2000, 3800)

func5.SetLineColor(kBlack)
func6.SetLineColor(kGreen)
total3.SetLineColor(kRed)

canvas3 = TCanvas("Canvas3", "Canvas3", 800, 600)


canvas3.cd()

histograma3Mass.Fit("func5","0R")
histograma3Mass.Fit("func6","0R+")

par1 = func5.GetParameters()
par2 = func6.GetParameters()

par[0], par[1], par[2] = par1[0], par1[1], par1[2]
par[3], par[4], par[5], par[6] = par2[0], par2[1], par2[2], par2[3]
total3.SetParameters(par)
histograma3Mass.Draw("SAME")
histograma3Mass.Fit("total3","R+")

par = total3.GetParameters()

par1[0], par1[1], par1[2] = par[0], par[1], par[2]
func5.SetParameters(par1)

Mean3, Sigma3 = par[1], par[2]

par2[0], par2[1], par2[2], par2[3] = par[3], par[4], par[5], par[6]
func6.SetParameters(par2)
func5.Draw("SAME")
func6.Draw("SAME")


integral3gaus = par[0]/histograma3Mass.GetBinWidth(2)
histograma3Mass.SetLineColor(kBlue)
histograma3Mass.GetXaxis().SetTitle("Mass")
histograma3Mass.GetYaxis().SetTitle("Quantity")

legend = TLegend(0.67,0.75,0.89,0.89)
legend.AddEntry(func5, "Gauss", "L")
legend.AddEntry(func6, "Pol3", "L")
legend.AddEntry(total3, "Total", "L")
legend.Draw()
canvas3.Draw()
canvas3.Print("ADC10et.gif")
print(f"\n\nThe integral of the Gaussian for ADC 10 Fit is = {integral3gaus}\n\n")


#Para ADC 15


par = array('d',7*[0.])

func7 = TF1("func7", "gausn", 2300, 3200)
func8 = TF1("func8", "pol3", 2000, 3700)
total4 = TF1("total4", "gausn(0)+pol3(3)", 2000, 3700)

func7.SetLineColor(kBlack)
func8.SetLineColor(kGreen)
total4.SetLineColor(kRed)

canvas4 = TCanvas("Canvas4", "Canvas4", 800, 600)


canvas4.cd()

histograma4Mass.Fit("func7","0R")
histograma4Mass.Fit("func8","0R+")

par1 = func7.GetParameters()
par2 = func8.GetParameters()

par[0], par[1], par[2] = par1[0], par1[1], par1[2]
par[3], par[4], par[5], par[6] = par2[0], par2[1], par2[2], par2[3]
total4.SetParameters(par)
histograma4Mass.Draw("SAME")
histograma4Mass.Fit("total4","R+")

par = total4.GetParameters()

par1[0], par1[1], par1[2] = par[0], par[1], par[2]
func7.SetParameters(par1)

Mean4, Sigma4 = par[1], par[2]


par2[0], par2[1], par2[2], par2[3] = par[3], par[4], par[5], par[6]
func8.SetParameters(par2)
func7.Draw("SAME")
func8.Draw("SAME")


integral4gaus = par[0]/histograma4Mass.GetBinWidth(2)
histograma4Mass.SetLineColor(kBlue)
histograma4Mass.GetXaxis().SetTitle("Mass")
histograma4Mass.GetYaxis().SetTitle("Quantity")

legend = TLegend(0.67,0.75,0.89,0.89)
legend.AddEntry(func7, "Gauss", "L")
legend.AddEntry(func8, "Pol3", "L")
legend.AddEntry(total4, "Total", "L")
legend.Draw()
canvas4.Draw()
canvas4.Print("ADC15et.gif")
print(f"\n\nThe integral of the Gaussian for ADC 15 Fit is = {integral4gaus}\n\n")


#Para ADC 30


par = array('d',7*[0.])

func9 = TF1("func9", "gausn", 2000, 3300)
func10 = TF1("func10", "pol3", 1900, 3600)
total5 = TF1("total5", "gausn(0)+pol3(3)", 1900, 3600)

func9.SetLineColor(kBlack)
func10.SetLineColor(kGreen)
total5.SetLineColor(kRed)

canvas5 = TCanvas("Canvas5", "Canvas5", 800, 600)


canvas5.cd()

histograma5Mass.Fit("func9","0R")
histograma5Mass.Fit("func10","0R+")

par1 = func9.GetParameters()
par2 = func10.GetParameters()

par[0], par[1], par[2] = par1[0], par1[1], par1[2]
par[3], par[4], par[5], par[6] = par2[0], par2[1], par2[2], par2[3]
total5.SetParameters(par)
histograma5Mass.Draw("SAME")
histograma5Mass.Fit("total5","R+")

par = total5.GetParameters()

par1[0], par1[1], par1[2] = par[0], par[1], par[2]
func9.SetParameters(par1)

Mean5, Sigma5 = par[1], par[2]


par2[0], par2[1], par2[2], par2[3] = par[3], par[4], par[5], par[6]
func10.SetParameters(par2)
func9.Draw("SAME")
func10.Draw("SAME")


integral5gaus = par[0]/histograma5Mass.GetBinWidth(2)
histograma5Mass.SetLineColor(kBlue)
histograma5Mass.GetXaxis().SetTitle("Mass")
histograma5Mass.GetYaxis().SetTitle("Quantity")

legend = TLegend(0.67,0.75,0.89,0.89)
legend.AddEntry(func9, "Gauss", "L")
legend.AddEntry(func10, "Pol3", "L")
legend.AddEntry(total5, "Total", "L")
legend.Draw()
canvas5.Draw()
canvas5.Print("ADC30et.gif")
print(f"\n\nThe integral of the Gaussian for ADC 30 Fit is = {integral5gaus}\n\n")


#Para ADC 50


par = array('d',7*[0.])

func11 = TF1("func11", "gausn", 1800, 3300)
func12 = TF1("func12", "pol3", 1730, 3500)
total6 = TF1("total6", "gausn(0)+pol3(3)", 1730, 3500)

func11.SetLineColor(kBlack)
func12.SetLineColor(kGreen)
total6.SetLineColor(kRed)

canvas6 = TCanvas("Canvas6", "Canvas6", 800, 600)


canvas6.cd()

histograma6Mass.Fit("func11","0R")
histograma6Mass.Fit("func12","0R+")

par1 = func11.GetParameters()
par2 = func12.GetParameters()

par[0], par[1], par[2] = par1[0], par1[1], par1[2]
par[3], par[4], par[5], par[6] = par2[0], par2[1], par2[2], par2[3]
total6.SetParameters(par)
histograma6Mass.Draw("SAME")
histograma6Mass.Fit("total6","R+")

par = total6.GetParameters()

par1[0], par1[1], par1[2] = par[0], par[1], par[2]
func11.SetParameters(par1)

Mean6, Sigma6 = par[1], par[2]


par2[0], par2[1], par2[2], par2[3] = par[3], par[4], par[5], par[6]
func12.SetParameters(par2)
func11.Draw("SAME")
func12.Draw("SAME")


integral6gaus = par[0]/histograma6Mass.GetBinWidth(2)
histograma6Mass.SetLineColor(kBlue)
histograma6Mass.GetXaxis().SetTitle("Mass")
histograma6Mass.GetYaxis().SetTitle("Quantity")

legend = TLegend(0.67,0.75,0.89,0.89)
legend.AddEntry(func11, "Gauss", "L")
legend.AddEntry(func12, "Pol3", "L")
legend.AddEntry(total6, "Total", "L")
legend.Draw()
canvas6.Draw()
canvas6.Print("ADC50et.gif")
print(f"\n\nThe integral of the Gaussian for ADC 50 Fit is = {integral6gaus}\n\n")



"""TGraph"""

canvas7 = TCanvas("Canvas7", "Canvas7", 800, 600)


integral = array('d',6*[0.])
integral[0], integral[1], integral[2], integral[3], integral[4], integral[5] = integralgaus, integral2gaus, integral3gaus, integral4gaus, integral5gaus, integral6gaus
ADC = array('d',6*[0.])
ADC[0], ADC[1], ADC[2], ADC[3], ADC[4], ADC[5] = 0, 5, 10, 15, 30, 50

canvas7.cd()

graph = TGraph(6,ADC,integral)
graph.SetTitle("Integral vs ADC; ADC; Integral")
graph.Draw("AC*")
canvas7.Draw()
canvas7.Print("Integral_vs_ADC_ETcut.gif")


canvas8 = TCanvas("Canvas8", "Canvas8", 1280, 900)

Meantotal = array('d', 6*[0.])
Meantotal[0], Meantotal[1], Meantotal[2], Meantotal[3], Meantotal[4], Meantotal[5] = Mean, Mean2, Mean3, Mean4, Mean5, Mean6

Sigmatotal = array('d', 6*[0.])
Sigmatotal[0], Sigmatotal[1], Sigmatotal[2], Sigmatotal[3], Sigmatotal[4], Sigmatotal[5] = Sigma, Sigma2, Sigma3, Sigma4, Sigma5, Sigma6


pad1 = TPad("p1", "p1", 0.2, 0.1, 0.8, 0.5, 0, 0, 0)
pad1.Draw()

pad2 = TPad("p2", "p2", 0.2, 0.55, 0.8, 0.95, 0, 0, 0)
pad2.SetBottomMargin(0)
pad2.Draw()

pad1.cd()

graphMean = TGraph(6,ADC,Meantotal)
graphMean.SetTitle("Mean vs ADC")
graphMean.SetLineColor(kBlue)
graphMean.GetXaxis().SetTitle("ADC")
graphMean.GetYaxis().SetTitle("Mean")
graphMean.Draw("AC*")


pad2.cd()

graphSigma = TGraph(6,ADC,Sigmatotal)
graphSigma.SetTitle("Sigma vs ADC")
graphSigma.SetLineColor(kRed)
graphSigma.GetXaxis().SetTitle("ADC")
graphSigma.GetYaxis().SetTitle("Sigma")
graphSigma.Draw("AC*")


canvas8.Draw()
canvas8.Print("Mean_and_Sigma_vs_ADC_ETcut.gif")
