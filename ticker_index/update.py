import pandas as pd

from ticker_index.schema import default_values
from ticker_index.schema import data_types
from ticker_index.schema import schema

from ticker_index.save import save_index
from markets.open_time import open_time
from markets.trading_minutes import trading_minutes

from apps.messages.ticker_index import message_updating, message_warning


def update_index(scope, downloaded_df ):
	message_updating()

	number_of_new_records = 0

	downloaded_df = apply_defaults_to_missing_values(downloaded_df)
	downloaded_df.set_index('share_code', inplace=True)
	

	for ticker, row in downloaded_df.iterrows(): 
		if ticker not in scope.ticker_index['df'].index:
			# add new ticker record
			number_of_new_records += 1
			row['opening_time'] = open_time( scope, ticker )
			row['minutes_per_day'] = trading_minutes( scope, ticker )
			row['blue_chip'] = schema['blue_chip']['default']
			scope.ticker_index['df'] = scope.ticker_index['df'].append(row)
		else:
			scope.ticker_index['df'].at[ticker, 'company_name'] = row['company_name']
			scope.ticker_index['df'].at[ticker, 'listing_date'] = row['listing_date']
			scope.ticker_index['df'].at[ticker, 'industry_group'] = row['industry_group']
			scope.ticker_index['df'].at[ticker, 'market_cap'] = row['market_cap']
	
	scope.ticker_index['df'] = apply_defaults_to_missing_values(scope.ticker_index['df'])
	scope.ticker_index['df']['listing_date'] = pd.to_datetime( scope.ticker_index['df']['listing_date'].dt.date  )
	scope.ticker_index['df'] = scope.ticker_index['df'].sort_index()
	
	message = 'number of ticker codes added to master ticker index = '+ str(number_of_new_records)

	message_warning(number_of_new_records, message)
	
	save_index(scope)
	


def apply_defaults_to_missing_values(dataframe):
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