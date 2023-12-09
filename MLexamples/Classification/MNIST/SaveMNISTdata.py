from Classification.MNIST.DataFunctions import SaveBunchPickle, SaveDataFrameCSV, SaveDataFrameCSV
from sklearn.datasets import fetch_openml
from sklearn.utils import Bunch
from pandas import DataFrame, Series

mnist = fetch_openml('mnist_784', version = 1)
print(mnist.keys())
theData: DataFrame = mnist['data']
theNumber: Series = mnist['target']

SaveBunchPickle("mnist_784.pkl","/Classification/MNIST/",mnist) #MUCH faster than CSV
# SaveDataFrameCSV("Data.csv","/Classification/MNIST/",theData)
# SaveDataFrameCSV("Numbers.csv","/Classification/MNIST/",theNumber)