from Source.AttoPhysics.TrajectoryPlotter.PlotTrajDataHelper import PlotTrajDataHelper
import os
cwd = os.getcwd()

path='/Data/'
filename= 'Binned_Initial_Condition_Grid_trunc'
dataHelper = PlotTrajDataHelper(path,filename)
dataHelper.CreateDataFrame();
dataHelper.AssignColumnNames();
df = dataHelper.GetDataFrame()
firstcolmn = df[dataHelper.p0]