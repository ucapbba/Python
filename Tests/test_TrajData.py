from Source.Plotters.TrajDataHelper import TrajDataHelper


def test_filepath():
    path = "../../../Data/"
    filename = "Binned_Initial_Condition_Grid_1e+07"
    obj = TrajDataHelper(path, filename)
    assert obj.GetFilePath() == path + filename


def test_dataframevalues():
    path = "/Data/"
    filename = "Binned_Initial_Condition_Grid_trunc"
    obj = TrajDataHelper(path, filename)
    obj.CreateDataFrame()
    obj.AssignColumnNames()
    df = obj.GetDataFrame()
    assert df[obj.p0][0] == 2.25719


def test_filterbyorbit():
    path = "/Data/"
    filename = "Binned_Initial_Condition_Grid_trunc"
    obj = TrajDataHelper(path, filename)
    obj.CreateDataFrame()
    obj.AssignColumnNames()
    orbitNum = 3
    obj.FilterByOrbit(orbitNum)
    df_filtered = obj.GetDataFrame()
    array = df_filtered.to_numpy()
    if not array.any():
        assert False
    assert True
