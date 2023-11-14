import os
from numpy.lib import math
from ImageClassifierHelper import ImageClassifierHelper
from Source.Base.BaseDataHelper import BaseDataHelper
from Source.Plotters.ContourPlot.ContourDataHelper import ContourDataHelper


class AsymCalculator(object):
    def __init__(self, _path, _jobNum, _minTask, _maxTask, _xrange, _yrange):
        self.path = _path
        self.jobNum = _jobNum
        self.minTask = _minTask
        self.maxTask = _maxTask
        self.xRange = _xrange
        self.yRange = _yrange

    def CalculateAssymetries(self):
        filePaths = self.getFilePaths()
        asym = []
        for filepath in filePaths:
            print(" processing file " + filepath.filename)
            contourHelper = ContourDataHelper(filepath.path, filepath.filename, self.xRange, self.yRange, 0, 0)
            contourHelper.LoadToArray()
            contourHelper.CreateArrays(7)
            thisasym = self.CalcualteAsymmetry(contourHelper.ZRESI)
            helper = ImageClassifierHelper(filepath.path, filepath.filename)
            imageValues = helper.GetValuesFromFilename()
            imageValues.asym = thisasym
            asym.append(imageValues)
        return asym

    def getFilePaths(self):
        filePaths = []
        cwd = os.getcwd()
        for task in range(self.minTask, self.maxTask):
            path = self.path + str(self.jobNum) + '.' + str(task) + '/Data/'
            fullPath = cwd + path
            if not os.path.exists(fullPath):
                print('path ' + fullPath + ' does not exisit - moving on....')
                continue
            for fileName in os.listdir(fullPath):
                if os.path.isfile(os.path.join(fullPath, fileName)):
                    helper = ImageClassifierHelper("", fileName)
                    if helper.IsAmpGrid() is False:
                        continue
                    baseData = BaseDataHelper(path, fileName)
                    filePaths.append(baseData)
        return filePaths

    def CalcualteAsymmetry(self, amplitudeValues):
        rhsSum = 0
        lhsSum = 0
        lineSum = 0
        count = 0
        for amplitudeRow in amplitudeValues:
            count += 1
            if count > self.xRange / 2:
                rhsSum += lineSum
            else:
                lhsSum += lineSum
            lineSum = 0
            for amplitude in amplitudeRow:
                if amplitude == 0:
                    continue
                lineSum += math.log(amplitude)
        asym = rhsSum / lhsSum
        print("asym = " + str(asym))
        return asym
