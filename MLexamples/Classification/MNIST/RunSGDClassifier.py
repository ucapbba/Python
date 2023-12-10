from Classification.MNIST.DataFunctions import LoadBunchPickle, PrintDataDetails
from Classification.MNIST.MLFunctions import MLFunctions

# MUCH faster than CSV
mnistData = LoadBunchPickle("mnist_784.pkl", "/Classification/MNIST/")
data = mnistData["data"]
numbers = mnistData["target"]

PrintDataDetails(data)
PrintDataDetails(numbers)
# for i in range(1,10):
#    plotNumber(data, numbers, i)

truncate = 10000
images = data.values[:truncate]
numbers = numbers[:truncate]

ML = MLFunctions(images, numbers, 0.01)
ML.MakePredictions(images, numbers)

for prediction, y in zip(ML.predictions, ML.y_test):
    print("prediction = " + str(prediction) + " ### actual = " + str(y))

print("Getting performance measures")
ML.GetPerformanceMeasures()
