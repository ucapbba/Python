from Source.MachineLearning.Clustering.ClusteringHelper import ClusteringHelper
from Source.Base.BasePlotter import BasePlotter

path = '/Data/'
filename = 'Binned_Initial_Condition_Grid_trunc1'
helper = ClusteringHelper(path, filename)

print("Loading Data " + filename + " ..... ")
helper.LoadToArray()
helper.TruncateArray(10000)
helper.CreateDataFrame()
helper.AssignColumnNames()
helper.FilterByOrbit(1)
helper.DropColumns()

print("Running Clustering .....")
helper.RunClustering(0.5, 30)

print("Plotting .....")
plotter = BasePlotter(helper)
plotter.plotScatter(helper.p0, helper.p0_perp, "Clustering Resutls", 15, 0.5)
