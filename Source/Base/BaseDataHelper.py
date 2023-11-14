import numpy as np
import pandas as pd

class BaseDataHelper:
    """For importing and manipulating file data"""
    def __init__(self, _path, _fname):
        self.path = _path
        self.filename = _fname
        self.myDataFrame = 0
    
    def GetFilePath(self):
        return self.path+self.filename;

    def CreateDataFrame(self):
         import os
         cwd = os.getcwd() 
         filePath  = BaseDataHelper.GetFilePath(self)
         array = np.loadtxt(cwd+filePath)
         df= pd.DataFrame(array)
         self.myDataFrame=df
         
    def GetDataFrame(self):
         return self.myDataFrame
        

