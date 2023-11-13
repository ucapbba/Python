from asyncio.windows_events import NULL
from BaseDataHelper import BaseDataHelper


def test_filepath():
    path ="/Data/"
    filename ="Binned_Initial_Condition_Grid_1e+07"
    obj = BaseDataHelper(path,filename)
    assert obj.GetFilePath() == "/Data/Binned_Initial_Condition_Grid_1e+07"

def test_createdataframe():
    path ="/Data/"
    filename ="Binned_Initial_Condition_Grid_trunc"
    dataHelper = BaseDataHelper(path,filename)
    dataHelper.CreateDataFrame();
    assert dataHelper.GetDataFrame().empty == False
    
