from numpy import ndarray
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict


class MLFunctions():
    predictions: ndarray

    def __init__(self, _images, _numbers, testSize: int):
        self.images = _images
        self.numbers = _numbers
        self.model = SGDClassifier(random_state=42)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(_images, _numbers, test_size=testSize, random_state=42)

    def MakePredictions(self, images, numbers):
        self.model.fit(self.X_train, self.y_train)
        self.predictions = self.model.predict(self.X_test)

    def GetPerformanceMeasures(self):
        print("cross_val_score")
        array = cross_val_score(self.model, self.X_train, self.y_train, cv=3, scoring="accuracy")
        print(array)
        print("cross_val_predict")
        y_train_pred = cross_val_predict(self.model, self.X_train, self.y_train, cv=3)
        print(y_train_pred)
        print("confusion_matrix")
        conf = confusion_matrix(self.y_train, y_train_pred)
        print(conf)
