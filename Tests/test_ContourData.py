from Source.Plotters.ContourPlot.ContourDataHelper import ContourDataHelper


def test_filepath():
    path = "../../../Data/"
    filename = "Binned_Initial_Condition_Grid_1e+07"
    obj = ContourDataHelper(path, filename, 0, 0, 0, 0)
    assert obj.GetFilePath() == path + filename


# TODO - decrease size of data file to speed up test
def test_createarrays():
    xRange = 750
    yRange = 750
    _min = 0
    _max = 0
    path = "/Data/"
    filename = "Amplitude_Grid_w2_1_1000_phi_0.025_750X750.dat"
    obj = ContourDataHelper(path, filename, xRange, yRange, _min, _max)
    obj.LoadToArray()
    obj.CreateArray(7)
    XRESI = obj.XRESI
    YRESI = obj.YRESI
    ZRESI = obj.ZRESI
    if not XRESI.any():
        assert False
    if not YRESI.any():
        assert False
    if not ZRESI.any():
        assert False
    assert True
