# Class that encapsulates the filtering of the prices
# Author: Hermes Valenciano
# May 2018
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

from data_gathering import Data_Gatherer


class Signal_Processor:
    def __init__(self):
        pass

    def _generate_syntethic_signal(self):
        # vueltas = 10
        # ppv = 30
        # std = .8
        # x = np.linspace(0, vueltas * 2 * np.pi, vueltas * ppv)
        # y = (np.sin(x) + np.random.normal(0, std, vueltas * ppv) + np.arange(vueltas * ppv) * 0.01)
        # return y
        start_year = 2014
        start_month = 7
        start_day = 11
        end_year = 2018
        end_month = 1
        end_day = 15

        start_date = datetime(year=start_year, month=start_month, day=start_day)
        end_date = datetime(year=end_year, month=end_month, day=end_day)
        dg = Data_Gatherer()
        df = dg.get_data('GLW', 'USAstocks', start_date, end_date, 1)
        return df['High'], df['Low'], df['Close']


    def _filter(self,x):
        agr = 1
        b, a = signal.butter(8, 1/(2**agr))
        y = signal.filtfilt(b, a, x, padlen=30)
        return y

    def filter_signal(self, price_sequence, filter_type, filtering_factor):
        """
        :param price_sequence:
        :param filtering_factor: (idea) number between 0 and 1 that tells how aggressive is the filtering
        :param filter_type: Filter to be applied: Gaussian, Fourier, etc.
        :return: filtered sequence
        """

        self._show_side_by_side()

    def _show_side_by_side(self):
        sgnH, sgnL, sgnC = self._generate_syntethic_signal()
        filteredH = self._filter(sgnH)
        filteredL = self._filter(sgnL)
        filteredC = self._filter(sgnC)

        plt.subplot(2, 1, 1)
        plt.title('Unfiltered')
        plt.plot(range(len(sgnC)), sgnC, 'r-')
        plt.plot(range(len(sgnH)), sgnH, 'g-')
        plt.plot(range(len(sgnL)), sgnL, 'b-')


        plt.subplot(2, 1, 2)
        plt.plot(range(len(filteredC)), filteredC, 'r-',markersize=1)
        plt.plot(range(len(filteredH)), filteredH, 'g-',markersize=1)
        plt.plot(range(len(filteredL)), filteredL, 'b-',markersize=1)
        plt.title('Filtered')
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    sp = Signal_Processor()
    sp.filter_signal(None,None,None)