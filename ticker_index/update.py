import pandas as pd

from ticker_index.schema import default_values
from ticker_index.schema import data_types

from ticker_index.save import save_index
from markets.open_time import open_time
from markets.trading_minutes import trading_minutes

import streamlit as st


def update_ticker_index(scope):

	blue_chip_default_value = scope.ticker_index['schema']['blue_chip']['default']
	number_of_new_records = 0

	apply_defaults_to_missing_values(scope, 'downloaded_df')

	for ticker, row in scope.ticker_index['df_downloaded'].iterrows(): 
		if ticker not in scope.ticker_index['df'].index:
			# add completely new ticker record/row
			number_of_new_records += 1
			new_row = pd.DataFrame([{
				'share_code':ticker,
				'company_name':row['company_name'], 
				'listing_date':row['listing_date'], 
				'industry_group':row['industry_group'], 
				'market_cap':row['market_cap'],
				'opening_time':open_time( scope, ticker ),
				'minutes_per_day':trading_minutes( scope, ticker ),
				'blue_chip':blue_chip_default_value,
				}])
			new_row.set_index('share_code', inplace=True)
			scope.ticker_index['df'] = pd.concat([scope.ticker_index['df'], new_row], axis=0, ignore_index=False)
		else:
			#just update specific values in the ticker_index from the downloaded data
			scope.ticker_index['df'].at[ticker, 'company_name'] = row['company_name']
			scope.ticker_index['df'].at[ticker, 'listing_date'] = row['listing_date']
			scope.ticker_index['df'].at[ticker, 'industry_group'] = row['industry_group']
			scope.ticker_index['df'].at[ticker, 'market_cap'] = row['market_cap']
	
	apply_defaults_to_missing_values(scope, 'ticker_index_df')

	scope.ticker_index['df'] = scope.ticker_index['df'].sort_index()

	# Report on the update
	if number_of_new_records > 0:
		st.toast('Added '+ str(number_of_new_records) + ' to master ticker index', icon = '⚠️')
	else:
		st.toast('Nothing added to master ticker index', icon = 'ℹ️')
	
	save_index(scope)
	

def apply_defaults_to_missing_values(scope, which_df):
	defaults = default_values(scope)
	dtypes = data_types(scope)
	if which_df == 'downloaded_df':
		df = scope.ticker_index['df_downloaded']
	else:
		df = scope.ticker_index['df']

	for field, default_value in defaults.items():
		if field in df.columns:
			if default_value != None:
				if dtypes[field] == 'str':
					df[field] = df[field].fillna(default_value) 

				if dtypes[field] == 'float64':
					df[field] = df[field].fillna(default_value)  
					df[field] = df[field].astype(float) 
				
				if dtypes[field] == 'int64':
					df[field] = df[field].fillna(0).astype(int)

				if dtypes[field] == 'datetime64[ns]':
					df[field] = df[field].fillna(default_value) 
