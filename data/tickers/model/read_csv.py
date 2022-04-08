import pandas as pd


from data.tickers.config import ticker_file_usecols
from data.tickers.config import ticker_file_dtypes
from data.tickers.config import ticker_file_dates

def load_ticker(scope, ticker):
	ticker_data_file = pd.read_csv (  
									scope.files['paths']['ticker_data'], 
									header      = 0,
									# nrows       = params.row_limitor, 
									usecols     = ticker_file_usecols,
									# index_col   = 'date', 
									dtype       = ticker_file_dtypes,
									parse_dates = ticker_file_dates,
									)
	scope.data['ticker_files'][ticker] = ticker_data_file







