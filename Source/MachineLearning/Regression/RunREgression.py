from Source.MachineLearning.Regression.ModelAnalyserIO import ModelAnalyserIO
from Source.Plotters.TrajDataHelper import TrajDataHelper
from Source.MachineLearning.Regression.ModelAnalyser import ModelAnalyser
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import ExtraTreeClassifier

path = '/Data/'
filename = 'Binned_Initial_Condition_Grid_trunc'
helper = TrajDataHelper(path, filename)
print("Loading to array....")
helper.LoadToArray()
helper.CreateDataFrame()
helper.AssignColumnNames()

print("Running Analyser....")
models = [DecisionTreeClassifier(), ExtraTreeClassifier()]
testSize = 0.25
analyser = ModelAnalyser(helper, models, testSize)
analyser.CompareModels()

print("Output Results...")
analyserIO = ModelAnalyserIO(analyser)
analyserIO.printDataStructureToScreen()
analyserIO.printModelPerformanceToScreen()
