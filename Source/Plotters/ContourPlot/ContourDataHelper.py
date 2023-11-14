from Source.Base.BaseDataHelper import BaseDataHelper
import numpy as np


class ContourDataHelper(BaseDataHelper):
    """For importing and manipulating file data in trajectory plotter"""
    def __init__(self, _path, _fname, _xRange, _yRange, _min, _max):
        BaseDataHelper.__init__(self, _path, _fname)
        self.xRange = _xRange
        self.yRange = _yRange
        self.min = _min
        self.max = _max
        self.myArray = 0
        self.XRESI = 0
        self.YRESI = 0
        self.ZRESI = 0

    def CreateArrays(self, ampIndex):
        data = self.myArray
        self.XRESI = data[:, 0].reshape(self.xRange, self.yRange)
        self.YRESI = data[:, 1].reshape(self.xRange, self.yRange)
        self.ZRESI = (data[:, ampIndex]).reshape(self.xRange, self.yRange)

    def Normalise(self):
        maxVal = np.amax(self.ZRESI)
        self.ZRESI = [x / maxVal for x in self.ZRESI]
        self.ZRESI = np.array(self.ZRESI)
        self.ZRESI[self.ZRESI < self.min] = 0
