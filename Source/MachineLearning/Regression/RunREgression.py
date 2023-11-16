from xml.parsers.expat import model
from Source.Base.BasePlotter import BasePlotter
from Source.Plotters.TrajDataHelper import TrajDataHelper
from Source.MachineLearning.Regression.ModelAnalyser import ModelAnalyser

import sklearn.multiclass
import sklearn.multioutput
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import ExtraTreeClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import RadiusNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import RidgeClassifier
from sklearn.linear_model import RidgeClassifierCV

path = '/Data/'
filename = 'Binned_Initial_Condition_Grid_trunc'
helper = TrajDataHelper(path, filename)
print("Loading to array....")
helper.LoadToArray()
helper.CreateDataFrame()
helper.AssignColumnNames()

models = [DecisionTreeClassifier(), ExtraTreeClassifier(),
          ExtraTreesClassifier(), KNeighborsClassifier(), 
          RandomForestClassifier()
          ]

models_multilable = [MLPClassifier(),
                     RidgeClassifier(),
                     RidgeClassifierCV()]

analyser = ModelAnalyser(helper)
analyser.stats_compare_models(helper.GetDataFrame(),models,"stats_multiclass_multioutput.csv")
analyser.stats_compare_models(helper.GetDataFrame(),models_multilable,"stats_multilabel.csv")