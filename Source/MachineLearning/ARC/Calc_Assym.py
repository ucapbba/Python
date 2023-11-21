from AsymCalculatorIO import AsymCalculator, AsymCalculatorIO

xRange = 500
yRange = 500
_min = 1e-6
_max = 1e2
path = '/Data/job/'
jobNum = 41044
minTask = 1
maxTask = 50

calc = AsymCalculator(path, jobNum, minTask, maxTask, xRange, yRange, _min, _max)
calc.CreateContourHelpers()
calc.CalculateAsymmetries()

print("Calcuation finished, output calcualtions ")
IO = AsymCalculatorIO(calc)
del calc
print('writing to file......')
IO.printToScreen()
IO.printToFile()
print('Done')
# print("Plotting Results : ")
# calc.plotColourMeshAsym()
