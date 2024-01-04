from Source.MachineLearning.Clustering.ClusteringHelper import ClusteringHelper
import copy
from Source.MachineLearning.Clustering.GlobalClusteringFunctions import LoopClusteringParams, PlotResults
from Source.MachineLearning.Clustering.GlobalClusteringFunctions import CreateHelpersForOrbits

path = '/Data/'
filename = 'Binned_Initial_Condition_Grid_trunc1'
coreHelper = ClusteringHelper(path, filename)

print("Loading Data " + filename + " ..... ")
coreHelper.LoadToArray()
coreHelper.CreateDataFrame()
coreHelper.AssignColumnNames()
# Uncomment to re-save data
# InitialPlots(coreHelper, pairPoints=10000, scatterPoints=100000)

MLhelper = copy.deepcopy(coreHelper)
MLhelper.Truncate(100000)
MLhelper.path = MLhelper.path + "Clustering/"

# Variables for clustering loop
minEps = 0.01
maxEps = 3
minSamples = 25
maxSamples = 125
maxRange = 30

MLhelpers = CreateHelpersForOrbits(MLhelper)
i = 0
for helper in MLhelpers:
    if i < 2:
        i = i + 1
        continue
    if i == 0:
        orbit = 'All'
        minClusters = 4
        maxClusters = 5
    else:
        minClusters = 2
        maxClusters = 4
        orbit = str(i)
    print("Running Clustering orbit " + orbit)
    helpers = LoopClusteringParams(helper, minSamples, maxSamples, minEps, maxEps, minClusters, maxClusters, maxRange)
    print("Plotting .....")
    PlotResults(helpers, orbit)
    i = i + 1
