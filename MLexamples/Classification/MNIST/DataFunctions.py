import pickle
import string
from numpy import void
from sklearn.utils import Bunch
from pandas import DataFrame, Series
from asyncio.windows_events import NULL
import pandas as pd
import os
import matplotlib as mpl
import matplotlib.pyplot as plt

def SaveDataFrameCSV(filename: string, filepath :string, data: DataFrame) -> void:
    cwd = os.getcwd()
    data.to_csv(cwd + filepath + filename)    

def SaveBunchPickle(filename: string, filepath :string, data: Bunch) -> void:
    cwd = os.getcwd()
    with open(cwd + filepath + filename, 'wb') as bunch:
        pickle.dump(data, bunch, protocol=pickle.HIGHEST_PROTOCOL)
        
def PrintDataDetails(data: DataFrame):
    print(data.shape)
 
def LoadDataFrameCSV(filename: string, filepath :string) -> DataFrame:
        cwd = os.getcwd()
        myDataFrame = pd.read_csv(cwd + filepath + filename)
        return myDataFrame

def LoadBunchPickle(filename: string, filepath :string) -> Bunch:
    cwd = os.getcwd()
    with open(cwd + filepath + filename, 'rb') as bunch:
        data = pickle.load(bunch)
    return data

def plotNumber(data: DataFrame, numbers: Series, index: int):
    some_digit = data.values[index]
    the_image = some_digit.reshape(28,28)
    plt.imshow(the_image, cmap="binary")
    plt.axis("off")
    plt.title("Label = " + str(numbers[index]))
    plt.show()
    