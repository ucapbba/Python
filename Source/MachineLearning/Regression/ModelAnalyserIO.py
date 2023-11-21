from numpy import void
from Source.MachineLearning.Regression.ModelAnalyser import ModelAnalyser


class ModelAnalyserIO(ModelAnalyser):
    def __init__(self, analyser: ModelAnalyser):
        self.helper = analyser.helper
        self.models = analyser.models
        self.modelKeys = analyser.modelKeys
        self.modelsDict = analyser.modelsDict
        self.testSize = analyser.testSize

    def printDataStructureToScreen(self) -> void:
        all_columns = self.helper.GetAllColumns()
        target_columns = self.helper.GetTargetColumns()
        dropped_columns = self.helper.GetColumnsToDrop()
        allStr, targetStr, dropStr = "", "", ""
        for column in all_columns:
            allStr = allStr + " " + column
        for column in target_columns:
            targetStr = targetStr + " " + column
        for column in dropped_columns:
            dropStr = dropStr + " " + column
        print("Initial Columns : " + allStr)
        print("Target Columns : " + targetStr)
        print("Dropped Columns : " + dropStr)

    def printModelPerformanceToScreen(self) -> void:
        for model in self.modelsDict:
            statsDict = self.modelsDict[model]
            print("Model : " + model)
            for key in statsDict:
                print("      " + key + " : " + str(statsDict[key]))
