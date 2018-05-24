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

         axs[0].plot(data['Close'],'k')
         axs[0].plot(data['High'], 'g')
         axs[0].plot(data['Low'], 'r')
         axs[0].plot(data['Open'], '#404040')
         axs[1].plot(data['Volume'])

         plt.show()
