import pandas as pd

from config.model.set_results import store_results

from config.params.index_schema import default_values
from config.params.index_schema import data_types
from config.params.index_schema import schema

from index.model.save import save_index
from config.params.markets import open_time
from config.params.markets import trading_minutes

from index.view.update_messages import message_updating
from index.view.update_messages import message_warning

def update_index(scope, downloaded_ticker_info ):
	message_updating()

	add_records_counter = 0

	downloaded_ticker_info = apply_defaults_to_missing_values(scope, downloaded_ticker_info)
	downloaded_ticker_info.set_index('share_code', inplace=True)
	
	store_results( 	scope, 
					passed='Updating these Tickers > ', 
					passed_2='Adding these Tickers > ', 
					failed='not applicable > ' 
					)

	for ticker, row in downloaded_ticker_info.iterrows(): 
		# 
		if ticker not in scope.ticker_index.index:
			add_records_counter += 1
			row['opening_time'] = open_time( scope, ticker )
			row['minutes_per_day'] = trading_minutes( scope, ticker )
			row['blue_chip'] = schema['blue_chip']['default']
			scope.ticker_index = scope.ticker_index.append(row)
			store_results( scope, ticker, result='passed_2' )
		else:
			scope.ticker_index.at[ticker, 'company_name'] = row['company_name']
			scope.ticker_index.at[ticker, 'listing_date'] = row['listing_date']
			scope.ticker_index.at[ticker, 'industry_group'] = row['industry_group']
			scope.ticker_index.at[ticker, 'market_cap'] = row['market_cap']
			store_results( scope, ticker, result='passed' )
	store_results(scope, 'Finished', final_print=True )
	
	scope.ticker_index = apply_defaults_to_missing_values(scope, scope.ticker_index)
	scope.ticker_index['listing_date'] = pd.to_datetime( scope.ticker_index['listing_date'].dt.date  )
	scope.ticker_index = scope.ticker_index.sort_index()
	
	message = 'number of ticker codes added to master ticker index = '+ str(add_records_counter)

	message_warning(add_records_counter, message)
	
	save_index(scope)
	
	scope.ticker_list_needs_updating = True


def apply_defaults_to_missing_values(scope, dataframe):
	defaults = default_values(schema)
	dtypes = data_types(schema)

	for field, default_value in defaults.items():
		if field in dataframe.columns:
			if default_value != None:
				if dtypes[field] == 'str':
					dataframe[field] = dataframe[field].fillna(default_value) 

				if dtypes[field] == 'float64':
					dataframe[field] = dataframe[field].fillna(default_value)  
					dataframe[field] = dataframe[field].astype(float) 
				
				if dtypes[field] == 'int64':
					dataframe[field] = dataframe[field].fillna(0).astype(int)

				if dtypes[field] == 'datetime64[ns]':
					dataframe[field] = dataframe[field].fillna(default_value) 

	return dataframe