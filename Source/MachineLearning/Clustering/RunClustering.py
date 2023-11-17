import random
from Source.MachineLearning.Clustering.ClusteringHelper import ClusteringHelper
from Source.Base.BasePlotter import BasePlotter
import copy

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

helpers=[]
# Variables for clustering loop
minEps=0.1
maxEps = 2
minSamples = 10
maxSamples = 50
minClusters = 4
maxClusters = 8
print("Running Clustering .....")
for i in range(1,50):
        eps = random.randint(minEps * 10, maxEps * 10)/10
        samples = random.randint(minSamples, maxSamples)
        helperCopy= copy.deepcopy(helper)
        clusters = helperCopy.RunClustering(eps, samples)
        if clusters >= minClusters and clusters < maxClusters:
            helpers.append(helperCopy)

print("Plotting .....")
for helper in helpers:
    plotter = BasePlotter(helper)
    plotter.plotScatter(helper.p0, helper.p0_perp, \
                        "Clustering Resutls - eps = " + str(helper.eps) + " Samples = " + str(helper.samples) \
                        , 15, 0.5)
