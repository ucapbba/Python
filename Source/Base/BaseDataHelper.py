import numpy as np


class BaseDataHelper:
    """For importing and manipulating file data"""
    def __init__(self, _path, _fname):
        self.path = _path
        self.filename = _fname
        self.myDataFrame = 0
        self.myArray = 0

    def GetFilePath(self):
        return self.path + self.filename

    def LoadToArray(self):
        import os
        cwd = os.getcwd()
        filePath = BaseDataHelper.GetFilePath(self)
        self.myArray = np.loadtxt(cwd + filePath)

    def TruncateArray(self, size):
        newArray = self.myArray[:size]
        self.myArray = newArray

    def GetArray(self):
        return self.myArray
