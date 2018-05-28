# Class that encapsulates the finding of supports and resistances.
# Author: Albert Sanchez
# May 2018

# Define what characteristics a support and a resistance needs to have to be considered a support or a resistance
# We have to decide if we treat supports and resistances as a discrete value or as a range of values and if we add a confidence interval that this is a support/resistances
# Should we indicate in the data which are the maximum and minimum values used by our algorithm to decide that a certain price level is a supp/resistance

import numpy as np
import pandas as pd

class Support_Resistance_Finder:
    def __init__(self):
        pass
    def find_supports(self, price_sequence, method):
        """
        :param price_sequence:
        :param method: string with the name of the method used to find resistances
        :return: a list of tuples (m,b,p) defining the line equations of the lines found,
        plus a number p defining the likelihood of that line.

        List of available methods:
        - elementary: Use elementary math (derivatives to find max and min)
        - volume: Use volume and price relation (high volume with low price change)
        - trendline: Find trendlines according to CryptoCred video
        - weight: Find horizontal lines by assigning weights according to their quality according to CryptoCred video criteria
        - pivot_points: Use pivot points
        - mean_shift_clustering: Use the mean shift clustering algorithm
        - so: Use algorithm found on Stackoverflow
        """
        if method == "elementary":
            self._elementary_method(price_sequence)

    def find_resistances(self, price_sequence, method):
        """
        :param price_sequence:
        :param method: string with the name of the method used to find resistances
        :return: a list of tuples (m,b,p) defining the line equations of the lines found,
        plus a number p defining the likelihood of that line.

        List of available methods:
        - elementary: Use elementary math (derivatives to find max and min)
        - volume: Use volume and price relation (high volume with low price change)
        - trendline: Find trendlines according to CryptoCred video
        - weight: Find horizontal lines by assigning weights according to their quality according to CryptoCred video criteria
        - pivot_points: Use pivot points
        - mean_shift_clustering: Use the mean shift clustering algorithm
        - so: Use algorithm found on Stackoverflow
        """
        pass

    # Methods for finding resistances and supports
    def _elementary_method(self, price_sequence, threshold=0.005):
        # Find turning points
        derivative = abs(self._derivative(price_sequence))
        for element in derivative:
            if element <= threshold:
                print(element)

    def _volume_method(self, price_sequence):
        pass

    def _trendline(self, price_sequence):
        pass

    def _weight(self, price_sequence):
        pass

    def _pivot_points(self, price_sequence):
        pass

    def _mean_shift_clustering(self, price_sequence):
        pass

    def _so(self, price_sequence):
        pass

    # Other internal methods
    def _derivative(self, price_sequence):
        return pd.Series(np.gradient(price_sequence), price_sequence.index, name='slope')

    # Testing methods
    def _get_test_data(self):
        start_year = 2016
        start_month = 1
        start_day = 1
        end_year = 2018
        end_month = 1
        end_day = 1

        start_date = datetime(year = start_year, month = start_month, day = start_day)
        end_date = datetime(year = end_year, month = end_month, day = end_day)

        dg = Data_Gatherer()
        df = dg.get_data('GLW','USAstocks', start_date,end_date,1)
        s = df['High'] # I only use high for testing purposes

        sp = Signal_Processor()
        return s, sp.filter_signal(s)

    def test_derivative(self):
        #Let's try to plot the derivative of 2x+1
        # x = np.linspace(0, 100)
        # y = (2*x)+1
        # s1 = pd.Series(y)
        # s2 = self._derivative(s1)
        # print(s2)
        # dv.compare_time_series(s1, s2)
        # #It's working!

        s, sfiltered = self._get_test_data()
        derivative = self._derivative(sfiltered)

        dv = Data_Visualizer()
        dv.compare_time_series(sfiltered, derivative)

    def test_support_finder(self):
        s, sfiltered = self._get_test_data()

        self.find_supports(s,"elementary")

if __name__ == "__main__":
    from data_gathering import Data_Gatherer
    from visualization import Data_Visualizer
    from signal_processing import Signal_Processor
    from datetime import datetime

    srf = Support_Resistance_Finder()
    # srf.test_derivative()
    srf.test_support_finder()
