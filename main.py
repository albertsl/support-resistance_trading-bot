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

def download_data(ticker):
    # Download price data for open, close, high, low, volume for the given ticker
    # Structure the data following the dataset structure
    pass

def find_supports(ticker):
     #Find the supports for the given ticker according to our support definition
     pass

def find_resistances(ticker):
     #Find the resistances for the given ticker according to our resistance definition
     pass

def graph_support_resistance(ticker):
    # Create a chart with the price data and the found supports and resistance for the given ticker
    pass
