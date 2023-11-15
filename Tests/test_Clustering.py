from Source.MachineLearning.Clustering.ClusteringHelper import ClusteringHelper


def test_RunClustering():
    path = '/Data/'
    filename = 'Binned_Initial_Condition_Grid_trunc1'
    helper = ClusteringHelper(path, filename)
    helper.LoadToArray()
    helper.TruncateArray(10000)
    helper.CreateDataFrame()
    helper.AssignColumnNames()
    helper.FilterByOrbit(1)
    helper.DropColumns()
    helper.RunClustering(0.5, 30)
    df = helper.GetDataFrame()
    orbitColumn = df[helper.orbit]
    assert orbitColumn.iloc[46] == 2
