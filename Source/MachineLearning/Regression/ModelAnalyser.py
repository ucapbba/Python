import os
import string
from Source.Plotters.TrajDataHelper import TrajDataHelper
from sklearn import metrics
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np


class ModelAnalyser(object):
    def __init__(self, _helper: TrajDataHelper):
        self.helper = _helper

    def stat_data(self, y_test, test_preds):
        cnf_matrix = metrics.confusion_matrix(y_test, test_preds)
        precision = metrics.precision_score(y_test, test_preds, average='macro')
        print("Precision:", precision)
        accuracy = metrics.accuracy_score(y_test, test_preds)
        print("Accuracy:", accuracy)
        sensitivity = metrics.recall_score(y_test, test_preds, average='macro')
        print("Sensitivity:", sensitivity)
        specificity = cnf_matrix[0][0] / (cnf_matrix[0][0] + cnf_matrix[0][1])
        print("Specificity:", specificity)
        return precision, accuracy, sensitivity, specificity

    def try_models(self, df: pd.DataFrame, model):
        y = df.orbit
        X = df.drop([self.helper.orbit, self.helper.p0, self.helper.pf], axis=1)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=4)
        dataset_train = pd.concat([X_train, y_train], axis=1)
        for column in dataset_train.drop(['orbit'], axis=1).columns:
            dataset_train[column] = (dataset_train[column] - dataset_train[column].min())\
                / (dataset_train[column].max() - dataset_train[column].min())
        model1 = model
        model1.fit(X_train, y_train)
        test_preds = model1.predict(X_test)
        test_preds = np.array([int(i) for i in test_preds])
        print(f'Statistical data for {model1} without even splitting between orbits in training data')
        return self.stat_data(y_test, test_preds)

    def try_models_even(self, df: pd.DataFrame, model):
        y = df.orbit
        X = df.drop(['orbit', 'p0[0]', 'pf[0]'], axis=1)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=4)
        dataset_train = pd.concat([X_train, y_train], axis=1)
        for column in dataset_train.drop(['orbit'], axis=1).columns:
            dataset_train[column] = (dataset_train[column] - dataset_train[column].min())\
                / (dataset_train[column].max() - dataset_train[column].min())
        data_orbit1 = dataset_train.loc[(dataset_train['orbit'] != 2) &\
                                        (dataset_train['orbit'] != 3) & (dataset_train['orbit'] != 4)]
        data_orbit2 = dataset_train.loc[(dataset_train['orbit'] != 1) &\
                                        (dataset_train['orbit'] != 3) & (dataset_train['orbit'] != 4)]
        data_orbit3 = dataset_train.loc[(dataset_train['orbit'] != 2) &\
                                        (dataset_train['orbit'] != 1) & (dataset_train['orbit'] != 4)]
        data_orbit4 = dataset_train.loc[(dataset_train['orbit'] != 2) &\
                                        (dataset_train['orbit'] != 3) & (dataset_train['orbit'] != 1)]
        dataset_train_even = pd.concat([data_orbit1.head(data_orbit4.shape[0]),\
                                        data_orbit2.head(data_orbit4.shape[0]),\
                                        data_orbit3.head(data_orbit4.shape[0]), data_orbit4])
        y_train_even = dataset_train_even.orbit
        X_train_even = dataset_train_even.drop(['orbit'], axis=1)
        model2 = model
        model2.fit(X_train_even, y_train_even)
        test_preds = model2.predict(X_test)
        test_preds = np.array([int(i) for i in test_preds])
        print(f'Statistical data for {model2} without even splitting between orbits in training data')
        return self.stat_data(y_test, test_preds)

    def stats_compare_models(self, df: pd.DataFrame, models: list, path: string):
        models_dict = dict.fromkeys(map(lambda x: str(x).replace('()', ''), models), [])
        for i in models:
            stats = ['precision', 'accuracy', 'sensitivity', 'specificity']
            stats_dict = dict.fromkeys(stats)
            precision, accuracy, sensitivity, specificity = self.try_models(df, i)
            stats_dict['precision'], stats_dict['accuracy'], stats_dict['sensitivity'], \
                stats_dict['specificity'] = precision, accuracy, sensitivity, specificity
            models_dict[str(i).replace('()', '')] = stats_dict
        df = pd.DataFrame.from_dict(models_dict, orient="index")
        cwd = os.getcwd()
        df.to_csv(cwd + '/' + path)
