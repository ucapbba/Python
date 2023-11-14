import matplotlib.pyplot as plt
import numpy as np
import Source.Base.BaseDataHelper as BaseDataHelper

class BasePlotter():
     """description of class"""
     def __init__(self,_helper):
        self.helper=_helper
     
     def plotScatter(self,col1,col2,title="",fontsize=15):
          df = self.helper.GetDataFrame()
          Xarray = np.asarray(df[col1])
          Yarray = np.asarray(df[col2])
          fig = plt.figure()  
          fig.canvas.set_window_title(title + " plot")
          plt.title(title,fontsize = fontsize)
          plt.xlabel(col1,fontsize = fontsize)
          plt.ylabel(col2,fontsize = fontsize)
          plt.xticks(fontsize = 15)
          plt.yticks(fontsize = 15)
          plt.scatter(Xarray, Yarray)
          plt.show()
     
     def plot2Scatter(self,col1,col2,col3,col4,title="",fontsize=15):
          df = self.helper.GetDataFrame()
          Xarray = np.asarray(df[col1])
          Yarray = np.asarray(df[col2])
          X2array = np.asarray(df[col3])
          Y2array = np.asarray(df[col4])
          fig = plt.figure()  
          fig.canvas.set_window_title(title + " plot")
          ax1 = fig.add_subplot(221)
          ax2 = fig.add_subplot(222)
          ax1.scatter(Xarray,Yarray,s=0.001,color = "purple")
          ax2.scatter(X2array,Y2array,s=0.001,color = "purple")
          #axis
          ax1.set_xlabel(col1,fontsize = fontsize)
          ax1.set_ylabel(col2,fontsize = fontsize)
          ax2.set_xlabel(col3,fontsize = fontsize)
          plt.show()
     

