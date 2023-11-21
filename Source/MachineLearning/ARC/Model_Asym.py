from Source.Base.BaseDataHelper import BaseDataHelper

path = '/Data/job/'
jobNum = 41044
filename = 'varAsymm_' + str(jobNum) + '_.out'
helper = BaseDataHelper(path, filename)
helper.LoadToArray()
array = helper.GetArray()
print(array[0])
