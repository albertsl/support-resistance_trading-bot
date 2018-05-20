
class Data_Gatherer:
    def __init__(self):
        pass


    def download_data(self, ticker, start_time, end_time, resolution):
        """
        :param ticker: identifier of the asset (String)
        :param start_time: datetime
        :param end_time: datetime
        :param resolution: granularity of the datetime
        :return: the path of the file that has been downloaded

        goes to the internet and downloads the requested data, and saves to a file

        """
        # Download price data for open, close, high, low, volume for the given ticker
        # Structure the data following the dataset structure
        pass

    def get_data(self, ticker, start_time, end_time, resolution):
        """
        :param ticker:
        :param start_time:
        :param end_time:
        :param resolution:
        :return: data frame with the requested data

        goes to the repository (directory) and loads the data into a data frame
        """
        pass




