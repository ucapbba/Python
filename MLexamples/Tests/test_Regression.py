from MLexamples.Regression.IRIS.IRISclass import IRISclass
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import math


def test_LoadIRISdata():
    iris = IRISclass()
    data = iris.df.values[0]
    # real: array([5.1, 3.5, 1.4, 0.2])
    assert data[0] == 5.1
    assert data[1] == 3.5
    assert data[2] == 1.4
    assert data[3] == 0.2


def test_LinearRegression():
    iris = IRISclass()
    X = iris.df.drop(labels='sepal length (cm)', axis=1)
    y = iris.df['sepal length (cm)']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=101)
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    lr.predict(X_test)
    predictions = lr.predict(X_test)
    assert math.isclose(predictions[0], 5.491579724105749)
