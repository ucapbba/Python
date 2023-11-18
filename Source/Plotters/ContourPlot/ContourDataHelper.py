from Source.Base.BaseDataHelper import BaseDataHelper
import numpy as np


class ContourDataHelper(BaseDataHelper):
    myArray: np.ndarray
    XRESI: np.ndarray
    YRESI: np.ndarray
    ZRESI: np.ndarray
    """For importing and manipulating file data in contour plotter"""
    def __init__(self, _path, _fname, _xRange, _yRange, _min, _max):
        BaseDataHelper.__init__(self, _path, _fname)
        self.xRange = _xRange
        self.yRange = _yRange
        self.min = _min
        self.max = _max

    def CreateArray(self, ampIndex) -> np.void:
        data = self.myArray
        self.XRESI = data[:, 0].reshape(self.xRange, self.yRange)
        self.YRESI = data[:, 1].reshape(self.xRange, self.yRange)
        self.ZRESI = (data[:, ampIndex]).reshape(self.xRange, self.yRange)

    def Normalise(self) -> np.void:
        maxVal = np.amax(self.ZRESI)
        self.ZRESI = [x / maxVal for x in self.ZRESI]
        self.ZRESI = np.array(self.ZRESI)
        self.ZRESI[self.ZRESI < self.min] = 0
