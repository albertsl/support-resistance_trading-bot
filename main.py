# Main file of the project. This file is pretended to run the code.
# Author: Albert Sanchez
# May 2018

from datetime import datetime
from data_gathering import Data_Gatherer
from signal_processing import Signal_Processor
from support_resistance_finder import Support_Resistance_Finder
from visualization import Data_Visualizer
from ml_models import ML_Models

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
    df = dg.get_data('GLW','USAstocks', start_date,end_date,1,False)
    close_price = df['Close']

    sp = Signal_Processor()
    close_price_filtered = sp.filter_signal(close_price)

    srf = Support_Resistance_Finder()
    lr = srf.find_supports(close_price_filtered, "mean_shift")

    dv = Data_Visualizer()
    dv.plot_support_resistance(df, lr)

    df2 = srf.tag_support_resistance(df, lr)

    mlm = ML_Models()
    mlm.random_forest(df2)

if __name__ == "__main__":
    main()
