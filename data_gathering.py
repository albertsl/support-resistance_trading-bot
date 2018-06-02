# Class that encapsulates the gathering of the data.
# Author: Albert Sanchez
# May 2018

from os.path import abspath, exists
import pandas as pd
from pandas_datareader import data
from os import makedirs

class Data_Gatherer:
    def __init__(self):
        pass


    def download_data(self, ticker, category, start_time, end_time, resolution):
        """
        :param ticker: identifier of the asset (String)
        :param category: used to divide assets in different categories (String)
        :param start_time: datetime
        :param end_time: datetime
        :param resolution: granularity of the datetime
        :return: the path of the file that has been downloaded

        goes to the internet and downloads the requested data, and saves to a file

        """
        # Download price data for open, close, high, low, volume for the given ticker
        # Structure the data following the dataset structure
        file = self.get_file_path(ticker, category)
        df = data.DataReader(ticker, 'morningstar', start_time, end_time)
        df.to_csv(file)
        return file

    def get_data(self, ticker, category, start_time, end_time, resolution, overwrite=True):
        """
        :param ticker: identifier of the asset (String)
        :param category: used to divide assets in different categories (String)
        :param start_time: datetime
        :param end_time: datetime
        :param resolution: granularity of the datetime
        :return: data frame with the requested data

        goes to the repository (directory) and loads the data into a data frameself.
        If the data does not exists, it downloads it.

        """
        file = self.get_file_path(ticker, category)

        if overwrite:
            self.download_data(ticker, category, start_time, end_time, resolution)
        else:
            if not exists(file):
                self.download_data(ticker, category, start_time, end_time, resolution)

        return pd.read_csv(file)

    def get_file_path(self, ticker, category):
        """
        :param ticker: identifier of the asset (String)
        :param category: used to divide assets in different categories (String)
        :return: absolute path for the requested data file

        """
        folder = abspath('data/' + category)
        if not exists(folder):
            makedirs(folder)

        return abspath(folder + '/' + ticker + '.csv')
