from ImageCalculators import AsymCalculator


xRange = 750
yRange = 750
path = '/Data/'
jobNum = 140603
minTask = 10
maxTask = 14

calc = AsymCalculator(path, jobNum, minTask, maxTask, xRange, yRange)
variables = calc.CalculateAsymmetries()
for var in variables:
    print(str(var.w2) + " " + str(var.Idiff) + " " + str(var.asym))
