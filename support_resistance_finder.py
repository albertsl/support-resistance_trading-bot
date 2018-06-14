# Class that encapsulates the finding of supports and resistances.
# Author: Albert Sanchez
# May 2018

# Define what characteristics a support and a resistance needs to have to be considered a support or a resistance
# We have to decide if we treat supports and resistances as a discrete value or as a range of values and if we add a confidence interval that this is a support/resistances
# Should we indicate in the data which are the maximum and minimum values used by our algorithm to decide that a certain price level is a supp/resistance

import numpy as np
import pandas as pd
from sklearn.cluster import MeanShift, estimate_bandwidth

class Support_Resistance_Finder:
    def __init__(self):
        pass
    def find_supports(self, price_sequence, method, volume=None, params=None):
        """
        :param price_sequence:
        :param method: string with the name of the method used to find resistances
        :param volume: pandas Series with the volume. Only needed for the volume method
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
            return self._elementary_method(price_sequence)
        elif method == "volume":
            return self._volume_method(price_sequence, volume)
        elif method == "mean_shift":
            return self._mean_shift_clustering(price_sequence, params)

    def find_resistances(self, price_sequence, method, volume=None):
        """
        :param price_sequence:
        :param method: string with the name of the method used to find resistances
        :param volume: pandas Series with the volume. Only needed for the volume method
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
    def _elementary_method(self, price_sequence, threshold=0.005): #Attention, not finished yet!!!!!!
        # Find turning points
        derivative = abs(self._derivative(price_sequence))
        for element in derivative:
            if element <= threshold:
                print(element)

    def _volume_method(self, price_sequence, volume, threshold=0.01,prcentile=50):
        # Let's calculate the derivative of price to see price change
        levels = []
        derivative = abs(self._derivative(price_sequence))
        qvolume = np.percentile(volume, prcentile)

        for i in range(len(price_sequence)):
            if derivative[i] <= threshold and volume[i] >= qvolume:
                levels.append(price_sequence[i])

        return levels

    def _trendline(self, price_sequence):
        pass

    def _weight(self, price_sequence):
        pass

    def _pivot_points(self, price_sequence):
        pass

    def _mean_shift_clustering(self, price_sequence,q=0.1):
        ps = price_sequence.values.reshape((-1,1))
        bandwidth = estimate_bandwidth(ps, quantile=q, n_samples=100)
        ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
        ms.fit(ps)

        ml_results = []
        for k in range(len(np.unique(ms.labels_))):
            my_members = ms.labels_ == k
            values = price_sequence[my_members]
            # find the edges
            ml_results.append(min(values))
            ml_results.append(max(values))

        return ml_results

    def _so(self, price_sequence):
        pass

    # Other internal methods
    def _derivative(self, price_sequence):
        return pd.Series(np.gradient(price_sequence), price_sequence.index, name='slope')

    # Testing methods
    def _get_test_data(self):
        start_year = 2017
        start_month = 5
        start_day = 20
        end_year = 2018
        end_month = 5
        end_day = 20

        start_date = datetime(year = start_year, month = start_month, day = start_day)
        end_date = datetime(year = end_year, month = end_month, day = end_day)

        dg = Data_Gatherer()
        df = dg.get_data('GLW','USAstocks', start_date,end_date,1,False)
        s = df['High'] # I only use high for testing purposes

        sp = Signal_Processor()
        return s, sp.filter_signal(s), df

    def test_derivative(self):
        #Let's try to plot the derivative of 2x+1
        # x = np.linspace(0, 100)
        # y = (2*x)+1
        # s1 = pd.Series(y)
        # s2 = self._derivative(s1)
        # print(s2)
        # dv.compare_time_series(s1, s2)
        # #It's working!

        s, sfiltered, df = self._get_test_data()
        derivative = self._derivative(sfiltered)

        dv = Data_Visualizer()
        dv.compare_time_series(sfiltered, derivative)

    def test_support_finder(self):
        s, sfiltered, df = self._get_test_data()

        #supports = self.find_supports(s,"volume",df['Volume'])
        supports = self.find_supports(s,"mean_shift")
        print(supports)

    def tag_support_resistance(self, data, levels, threshold=0.001):
        """
        :param data: Pandas DataFrame with stock data
        :param levels: list with support and resistance levels
        :param threshold: Threshold level at which a price is considered to be touching the support or resistance level
        :return: input dataframe with additional column SR
        """
        lSR = [0] * data.shape[0]

        for i, row in data.iterrows():
            for level in levels:
                current_price = data['Close'].iloc[i]
                max_threshold = level + level * threshold
                min_threshold = level - level * threshold

                if current_price < max_threshold and current_price > min_threshold:
                    lSR[i] = 1

        data['SR'] = pd.Series(lSR)
        return data

if __name__ == "__main__":
    from data_gathering import Data_Gatherer
    from visualization import Data_Visualizer
    from signal_processing import Signal_Processor
    from datetime import datetime

    srf = Support_Resistance_Finder()
    # srf.test_derivative()
    srf.test_support_finder()
