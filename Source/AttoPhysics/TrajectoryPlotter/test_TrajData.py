from Source.AttoPhysics.TrajectoryPlotter.PlotTrajDataHelper import PlotTrajDataHelper

def test_filepath():
    path ="../../../Data/"
    filename ="Binned_Initial_Condition_Grid_1e+07"
    obj = PlotTrajDataHelper(path,filename)
    assert obj.GetFilePath() == path+filename

def test_dataframevalues():
    path ="/Data/"
    filename ="Binned_Initial_Condition_Grid_trunc"
    dataHelper = PlotTrajDataHelper(path,filename)
    dataHelper.CreateDataFrame();
    dataHelper.AssignColumnNames()
    df = dataHelper.GetDataFrame();
    assert df[dataHelper.p0][0] == 2.25719