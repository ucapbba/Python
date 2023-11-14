from Source.Plotters.ContourPlot.ContourDataHelper import ContourDataHelper
from Source.Base.BasePlotter import BasePlotter

xRange = 750
yRange = 750
_min = 1e-4
_max = 1e-1
path = '/Data/'
filename = 'Amplitude_Grid_w2_1_1000_phi_0.025_750X750.dat'

dataHelper = ContourDataHelper(path, filename, xRange, yRange, _min, _max)
dataHelper.LoadToArray()
dataHelper.CreateArrays(7)
dataHelper.Normalise()

plotter = BasePlotter(dataHelper)
plotter.PlotColourMesh()
