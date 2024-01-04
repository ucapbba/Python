from Source.Plotters.ContourPlot.ContourDataHelper import ContourDataHelper
from Source.Base.BasePlotter import BasePlotter

xRange = 500
yRange = 400
_min = 1e-4
_max = 1e-1
path = '/../../CQSFA/'
filename = 'Amplitude_Grid_w2_3_10_phi_0.9_500X400.dat'

dataHelper = ContourDataHelper(path, filename, xRange, yRange, _min, _max)
dataHelper.LoadToArray()
dataHelper.CreateArray(7)
dataHelper.Normalise()

plotter = BasePlotter(dataHelper)
plotter.PlotColourMesh()
