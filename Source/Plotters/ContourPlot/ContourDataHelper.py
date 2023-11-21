from Source.Base.BaseDataHelper import BaseDataHelper
from numpy import array, ndarray, void, amax


class ContourDataHelper(BaseDataHelper):
    myArray: ndarray
    XRESI: ndarray
    YRESI: ndarray
    ZRESI: ndarray
    """For importing and manipulating file data in contour plotter"""
    def __init__(self, _path, _fname, _xRange, _yRange, _min, _max):
        BaseDataHelper.__init__(self, _path, _fname)
        self.xRange = _xRange
        self.yRange = _yRange
        self.min = _min
        self.max = _max

    def CreateArray(self, ampIndex) -> void:
        data = self.myArray
        self.XRESI = data[:, 0].reshape(self.xRange, self.yRange)
        self.YRESI = data[:, 1].reshape(self.xRange, self.yRange)
        self.ZRESI = (data[:, ampIndex]).reshape(self.xRange, self.yRange)

    def Normalise(self) -> void:
        maxVal = amax(self.ZRESI)
        self.ZRESI = [x / maxVal for x in self.ZRESI]
        self.ZRESI = array(self.ZRESI)  # array creates an ndarray
        self.ZRESI[self.ZRESI < self.min] = 0
