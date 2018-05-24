# Class that encapsulates the visualization of the data.
# Author: Albert Sanchez
# May 2018

import matplotlib.pyplot as plt
import seaborn as sns
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

         plt.plot(data['Close'],'k')
         plt.plot(data['High'], 'g')
         plt.plot(data['Low'], 'r')
         plt.plot(data['Open'], '#404040')
         # plt.plot(data['Volume'])
         plt.show()
