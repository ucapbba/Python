from pandas import DataFrame
import pandas as pd
from sklearn.utils import Bunch
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
from sklearn import datasets
import seaborn as sns
import matplotlib.pyplot as plt


class IRISclass:
    def __init__(self):
        self.irisB: Bunch = datasets.load_iris()
        print(self.irisB.feature_names)
        self.df: DataFrame = pd.DataFrame(data=self.irisB.data, columns=self.irisB.feature_names)

    def converter(self, specie):
        if specie == 0:
            return 'setosa'
        elif specie == 1:
            return 'versicolor'
        else:
            return 'virginica'

    def PrintInfos(self) -> np.void:
        print(self.df)
        print(self.df.describe())
        print(self.df.info())

    def loadIRISdata(self) -> DataFrame:
        return self.iris

    def plotIRISdata(self) -> np.void:
        target: DataFrame = pd.DataFrame(data=self.irisB.target, columns=['species'])
        target['species'] = target['species'].apply(self.converter)
        iris = pd.concat([self.df, target], axis=1)
        sns.pairplot(iris, hue='species')
        plt.show()

    def PrintPerformanceInfo(self, predictions, y_test):
        for prediction, y in zip(predictions, y_test):
            print("predicted length = " + str(prediction) + " ### actual length = " + str(y))
        print('Mean Absolute Error:', mean_absolute_error(y_test, predictions))
        print('Mean Squared Error:', mean_squared_error(y_test, predictions))
        print('Mean Root Squared Error:', np.sqrt(mean_squared_error(y_test, predictions)))
