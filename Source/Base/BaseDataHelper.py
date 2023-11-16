import string
import numpy as np
import pandas as pd
import os

class BaseDataHelper:
    """For importing and manipulating file data"""
    myDataFrame : pd.DataFrame
    myArray : np.array
    def __init__(self, _path : string, _fname : string):
        self.path = _path
        self.filename = _fname

    def GetFilePath(self):
        return self.path + self.filename

    def LoadToArray(self):
        cwd = os.getcwd()
        filePath = BaseDataHelper.GetFilePath(self)
        self.myArray = np.loadtxt(cwd + filePath)

    def TruncateArray(self, size : int):
        newArray = self.myArray[:size]
        self.myArray = newArray

    def GetArray(self):
        return self.myArray
