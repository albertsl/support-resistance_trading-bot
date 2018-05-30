# Main file of the project. This file is pretended to run the code.
# Author: Albert Sanchez
# May 2018

from datetime import datetime
from data_gathering import Data_Gatherer
from visualization import Data_Visualizer

def main():
    start_year = 2016
    start_month = 1
    start_day = 1
    end_year = 2018
    end_month = 1
    end_day = 1

    start_date = datetime(year = start_year, month = start_month, day = start_day)
    end_date = datetime(year = end_year, month = end_month, day = end_day)

    asset_categories = ['USAstocks','EUROPEANstocks','SPANISHstocks','FOREX','CRYPTO','COMMODITIES']

    dg = Data_Gatherer()
    dg.get_data('GLW','USAstocks', start_date,end_date,1,True)

if __name__ == "__main__":
    main()
