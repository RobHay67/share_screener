import pandas as pd

from config.initial_scope.ticker import ticker_file_usecols
from config.initial_scope.ticker import ticker_file_dtypes
from config.initial_scope.ticker import ticker_file_dates



def load_ticker(scope, ticker):
	ticker_data_file = pd.read_csv (  
									scope.path_ticker_data_file, 
									header      = 0,
									# nrows       = params.row_limitor, 
									usecols     = ticker_file_usecols,
									# index_col   = 'date', 
									dtype       = ticker_file_dtypes,
									parse_dates = ticker_file_dates,
									)
	scope.ticker_data_files[ticker] = ticker_data_file







