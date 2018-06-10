# Class that encapsulates the gathering of the data.
# Author: Albert Sanchez
# May 2018

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

class ML_Models:
    def __init__(self):
        pass

    def _x_y(self, data):
        """
        :param data: pandas DataFrame with all the data
        :return: x and y values to give the ML model

        """
        y = data['Up']
        x = data.drop(['Up','Symbol','Date'], axis = 1)
        return x, y

    def _train_test_set(self, x, y):
        """
        :param x: x parameter for the model
        :param y: y parameter for the model
        :return: x_train, x_test, y_train, y_test to give the ML model

        """
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)
        return x_train, x_test, y_train, y_test

    def _results(self, y_test, predictions):
        """
        :param y_test: y_test column
        :param predictions: predictions for the y_test column
        :return: nothing, just prints the results

        """
        print(classification_report(y_test,predictions))
        print(confusion_matrix(y_test,predictions))

    def logistic_regression(self, data):
        """
        :param data: pandas DataFrame with all the data
        :return:

        """
        x, y = self._x_y(data)
        x_train, x_test, y_train, y_test = self._train_test_set(x,y)

        logmodel = LogisticRegression()
        logmodel.fit(x_train,y_train)

        predictions = logmodel.predict(x_test)
        self._results(y_test,predictions)

    def random_forest(self, data):
        """
        :param data: pandas DataFrame with all the data
        :return:

        """
        x, y = self._x_y(data)
        x_train, x_test, y_train, y_test = self._train_test_set(x,y)

        rfc = RandomForestClassifier(n_estimators=200)
        rfc.fit(x_train, y_train)
        predictions = rfc.predict(x_test)

        self._results(y_test,predictions)
