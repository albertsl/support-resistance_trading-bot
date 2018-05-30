# Class that encapsulates the visualization of the data.
# Author: Albert Sanchez
# May 2018

import matplotlib.pyplot as plt
from datetime import datetime

class Data_Visualizer:
    def __init__(self):
        pass

    def plot_support_resistance(self, data, levels):
        """
        :param data: dataframe with all the data to plot
        :param levels: list with the levels of support and resistance
        :return: returns nothing. Shows a plot of the price and the supports and resistances.

        Create a chart with the price data and the found supports and resistance for the given ticker

        """
        ax = plt.axes()
        ax.grid(color='silver')

        plt.plot(data['Close'],'k')
        plt.plot(data['High'], 'g')
        plt.plot(data['Low'], 'r')
        plt.plot(data['Open'], '#404040')

        for level in levels:
            ax.axhline(y=level)

        plt.show()

    def plot_support_resistance_volume(self, data, levels):
        """
        :param data: dataframe with all the data to plot
        :param levels: list with the levels of support and resistance
        :return: returns nothing. Shows a plot of the price and the supports and resistances.

        Create a chart with the price data and the found supports and resistance for the given ticker

        """
        fig, axs = self._plot_price_volume(data)

        for level in levels:
            axs[0].axhline(y=level)

        plt.show()

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

        self._plot_price_volume(data)

        plt.show()

    def _plot_price_volume(self, data):
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
        axs[1].bar(x=range(len(data)),height=data['Volume'])

        return fig, axs

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
        start_year = 2017
        start_month = 5
        start_day = 20
        end_year = 2018
        end_month = 5
        end_day = 20

        start_date = datetime(year = start_year, month = start_month, day = start_day)
        end_date = datetime(year = end_year, month = end_month, day = end_day)

        dg = Data_Gatherer()
        return dg.get_data('GLW','USAstocks', start_date,end_date,1,True)

    def test(self):
        data = self._get_test_data()
        self.compare_time_series(data['High'], data['Low'])
        self.plot_price(data)

        levels = [29.46, 29.1, 33.89, 28.8]
        self.plot_support_resistance_volume(data, levels)
        self.plot_support_resistance(data, levels)

if __name__ == "__main__":
    from data_gathering import Data_Gatherer

    dv = Data_Visualizer()
    dv.test()
