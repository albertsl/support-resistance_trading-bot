# Class that encapsulates the visualization of the data.
# Author: Albert Sanchez
# May 2018

import matplotlib.pyplot as plt
# import seaborn as sns
from datetime import datetime

class Data_Visualizer:
    def __init__(self):
        pass

    def plot_support_resistance(self, data):
        """
        :param data: dataframe with all the data to plot
        :return: returns nothing. Shows a plot of the price and the supports and resistances.

        Create a chart with the price data and the found supports and resistance for the given ticker

        """
        pass

    def plot_price(self, data):
        """
        :param data: dataframe with all the data to plot
        :return: returns nothing. Shows a plot of the price and the supports and resistances.

        Create a chart with the price data for the given tickerself.
        Close price - Black
        High price - Green
        Low price - Red
        Open price - Dark grey

        """

        fig, axs = plt.subplots(2, 1, sharex=True)
        # Remove horizontal space between axes
        fig.subplots_adjust(hspace=0)

        axs[0].grid(color='silver')
        axs[1].grid(color='silver')
        
        axs[0].plot(data['Close'],'k')
        axs[0].plot(data['High'], 'g')
        axs[0].plot(data['Low'], 'r')
        axs[0].plot(data['Open'], '#404040')
        axs[1].plot(data['Volume'])

        plt.show()

    def compare_time_series(self, series1, series2):
        """
        :param series1: data for series1 (Pandas Series format)
        :param series2: data for series2 (Pandas Series format)
        :return: returns nothing. Shows a plot of the two time series.

        Create a chart with both time series.
        """

        fig, axs = plt.subplots(2, 1, sharex=True)
        # Remove horizontal space between axes
        fig.subplots_adjust(hspace=0)

        axs[0].grid(color='silver')
        axs[1].grid(color='silver')

        axs[0].plot(series1)
        axs[1].plot(series2)

        plt.show()

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
        return dg.get_data('GLW','USAstocks', start_date,end_date,1)

    def test(self):
        data = self._get_test_data()
        self.compare_time_series(data['High'], data['Low'])

if __name__ == "__main__":
    from data_gathering import Data_Gatherer

    dv = Data_Visualizer()
    dv.test()
