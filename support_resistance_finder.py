# Class that encapsulates the finding of supports and resistances.
# Author: Albert Sanchez
# May 2018

# Define what characteristics a support and a resistance needs to have to be considered a support or a resistance
# We have to decide if we treat supports and resistances as a discrete value or as a range of values and if we add a confidence interval that this is a support/resistances
# Should we indicate in the data which are the maximum and minimum values used by our algorithm to decide that a certain price level is a supp/resistance

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
        pass

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

    def _elementary_method(self, price_sequence):
        pass

    def _volume method(self, price_sequence):
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
