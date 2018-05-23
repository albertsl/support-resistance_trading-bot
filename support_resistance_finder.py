# Class that encapsulates the finding of supports and resistances.
# Author: Albert Sanchez
# May 2018

# Define what characteristics a support and a resistance needs to have to be considered a support or a resistance
# We have to decide if we treat supports and resistances as a discrete value or as a range of values and if we add a confidence interval that this is a support/resistances
# Should we indicate in the data which are the maximum and minimum values used by our algorithm to decide that a certain price level is a supp/resistance

class Support_Resistance_Finder:
     def __init__(self):
         pass

     def find_supports(self, price_sequence):
         """
         :param price_sequence:
         :return: a list of tuples (m,b,p) defining the line equations of the lines found,
         plus a number p defining the likelihood of that line.
         """
         pass

     def find_resistances(self, price_sequence):
         """
         :param price_sequence:
         :return: a list of tuples (m,b,p) defining the line equations of the lines found,
         plus a number p defining the likelihood of that line.
         """
