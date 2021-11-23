import pandas as pd

from config.ticker import ticker_file_usecols, ticker_file_dtypes, ticker_file_dates

def load_a_ticker( scope, ticker ): # DONE
	share_data_file = pd.read_csv (  
									scope.path_share_data_file, 
									header      = 0,
									# nrows       = params.row_limitor, 
									usecols     = ticker_file_usecols,
									# index_col   = 'date', 
									dtype       = ticker_file_dtypes,
									parse_dates = ticker_file_dates,
									)
	scope.ticker_data_files[ticker] = share_data_file







