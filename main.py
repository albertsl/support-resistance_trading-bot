# Main file of the project. This file is pretended to run the code.
# Author: Albert Sanchez
# May 2018

# We have to decide how do we structure our datasets
# We will create different categories of assets. To start with:
# - USA stocks
# - European stocks
# - Spanish stocks
# - Forex
# - Crypto
# - Commodities
# Feel free to add more
# Define what characteristics a support and a resistance needs to have to be considered a support or a resistance
# We have to decide if we treat supports and resistances as a discrete value or as a range of values and if we add a confidence interval that this is a support/resistances
# Should we indicate in the data which are the maximum and minimum values used by our algorithm to decide that a certain price level is a supp/resistance

from datetime import datetime
from data_gathering import Data_Gatherer

def main():
    start_year = 2016
    start_month = 1
    start_day = 1
    end_year = 2018
    end_month = 1
    end_day = 1

    start_date = datetime(year = start_year, month = start_month, day = start_day)
    end_date = datetime(year = end_year, month = end_month, day = end_day)

    dg = Data_Gatherer()
    dg.download_data('AAPL','USAstocks', start_date,end_date,1)

if __name__ == "__main__":
    main()
