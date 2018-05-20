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

from data_gathering import Data_Gatherer

def main():
    dg = Data_Gatherer()



if __name__ == "__main__":
    main()
