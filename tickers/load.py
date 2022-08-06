import pandas as pd


from tickers.schema import ticker_file_usecols
from tickers.schema import ticker_file_dtypes
from tickers.schema import ticker_file_dates


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
	return ticker_data_file
	
	



	







