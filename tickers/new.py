import pandas as pd

from tickers.save import save_ticker
from tickers.events.new import new_ticker_data_event
from tickers.config import create_dictionary_to_store_ticker_data



def add_new_ticker(scope, ticker, new_ticker_data):


	if ticker in scope.tickers.keys():
		# Data already exists for this ticker
		print('Data exists so append it here')
		print(new_ticker_data['date'].value_counts())
		existing_ticker_df = scope.tickers[ticker]['df']
		existing_ticker_df = pd.concat([existing_ticker_df, new_ticker_data]).drop_duplicates(subset=['date'], keep='last')
		existing_ticker_df.sort_values(by=['date'], inplace=True, ascending=False)		# sort
	else:
		# ticker is new
		create_dictionary_to_store_ticker_data(scope, ticker)
		new_ticker_data.sort_values(by=['date'], inplace=True, ascending=False)	
		scope.tickers[ticker]['df'] = new_ticker_data		# cache the ticker data 

	new_ticker_data_event(scope, ticker)
	save_ticker(scope, ticker)






