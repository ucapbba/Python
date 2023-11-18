import math
from Source.MachineLearning.ARC.ImageClassifierHelper import ImageClassifierHelper
from Source.MachineLearning.ARC.ImageCalculators import AsymCalculator
from Source.Plotters.ContourPlot.ContourDataHelper import ContourDataHelper


def test_GetValuesFromFilename():
    somePath = "somePath"
    filename = "Amplitude_Grid_w2_1_1000_phi_0.025_750X750.dat"
    helper = ImageClassifierHelper(somePath, filename)
    values = helper.GetValuesFromFilename()
    Idiff = values.Idiff
    w2 = values.w2
    phi = values.phi
    assert w2 == str(1)
    assert Idiff == str(1000)
    assert phi == str(0.025)


def test_IsAmplitudeGrid():
    somePath = "somePath"
    filename = "Amplitude_Grid_w2_1_1000_phi_0.025_750X750.dat"
    helper = ImageClassifierHelper(somePath, filename)
    assert helper.IsAmpGrid()
    filename = "random_name"
    helper = ImageClassifierHelper(somePath, filename)
    assert not helper.IsAmpGrid()


def GetPathDetailsForTest():
    path = '/Data/'
    jobNum = 140603
    minTask = 10
    maxTask = 14
    xRange = 750
    yRange = 750
    return path, jobNum, minTask, maxTask, xRange, yRange


def test_GeARCDATAFilePath():
    path, jobNum, minTask, maxTask, xRange, yRange = GetPathDetailsForTest()
    helper = AsymCalculator(path, jobNum, minTask, maxTask, xRange, yRange)
    filePaths = helper.getFilePaths()
    assert len(filePaths) is 1
    filePath = filePaths[0].GetFilePath()
    thePath = '/Data/140603.10/Data/Amplitude_Grid_w2_1_1000_phi_0.025_750X750.dat'
    assert filePath == thePath


def test_AsymmCalc():
    path, jobNum, minTask, maxTask, xRange, yRange = GetPathDetailsForTest()
    helper = AsymCalculator(path, jobNum, minTask, maxTask, xRange, yRange)
    filePaths = helper.getFilePaths()
    filePath = filePaths[0]
    contourHelper = ContourDataHelper(filePath.path, filePath.filename, xRange, yRange, 0, 0)
    contourHelper.LoadToArray()
    contourHelper.CreateArray(7)
    asym = helper.CalcualteAsymmetry(contourHelper.ZRESI)
    assert math.isclose(asym, 1.0006104342748006)
