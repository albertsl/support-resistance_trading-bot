# Class that encapsulates the filtering of the prices
# Author: Hermes Valenciano
# May 2018

class Signal_Processor:
    def __init__(self):
        pass

    def filter_signal(self, price_sequence, filter_type, filtering_factor):
        """
        :param price_sequence:
        :param filtering_factor: (idea) number between 0 and 1 that tells how aggressive is the filtering
        :param filter_type: Filter to be applied: Gaussian, Fourier, etc.
        :return: filtered sequence
        """
        pass