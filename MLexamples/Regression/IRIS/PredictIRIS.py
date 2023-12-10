from sklearn.linear_model import LinearRegression
from Regression.IRIS.IRISclass import IRISclass
from sklearn.model_selection import train_test_split

iris = IRISclass()
iris.plotIRISdata()

X = iris.df.drop(labels='sepal length (cm)', axis=1)
y = iris.df['sepal length (cm)']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=101)

lr = LinearRegression()
lr.fit(X_train, y_train)
lr.predict(X_test)
predictions = lr.predict(X_test)

iris.PrintPerformanceInfo(predictions, y_test)
