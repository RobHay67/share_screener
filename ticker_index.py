# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# External Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
import pandas as pd
import os
import datetime
import streamlit as st

from web_results import render_results


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ticker Index file Schema
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
ticker_index_schema ={
						'share_code'		:{'dtype':'str'				, 'default':None},
						'company_name'		:{'dtype':'str'				, 'default':'zz_missing_company_name'},
						'industry_group'	:{'dtype':'str'				, 'default':'zz_missing_industry_group'},
						'listing_date'		:{'dtype':'datetime64[ns]'	, 'default':pd.to_datetime('2000-01-01')},
						'market_cap'		:{'dtype':'float64'			, 'default':0.0},
						'opening_time'		:{'dtype':'str'				, 'default':None},
						'minutes_per_day'	:{'dtype':'float64'			, 'default':None},
						'blue_chip'			:{'dtype':'str'				, 'default':'zz_not_yet_tagged'},
						'yahoo_status'		:{'dtype':'str'				, 'default':None},
						'missing_dates'		:{'dtype':'object'			, 'default':None},
						'delisted_date'		:{'dtype':'datetime64[ns]'	, 'default':None},
						'trading_halt_dates':{'dtype':'object'			, 'default':None},
					}

# ==============================================================================================================================================================
# Browser Render Controller : Display Ticker Index, Count of tickers by Industry and Update the Ticker Index
# ==============================================================================================================================================================
def render_ticker_index_page(scope):

	st.title('Maintain the Ticker Index File')
	col1,col2,col3,col4,col5 = st.columns([2,2,2,2,4])
	# col1,col2 = st.columns([2,10])
	with col1: st.success(('Ticker Index contains ( ' + str((len(scope.ticker_index_file))) + ' ) tickers'))
	# col1,col2,col3,col4 = st.columns([2,2,2,6])
	with col2: download_ticker_index = st.button('Update Ticker Index File')
	with col3: show_ticker_index = st.button('Show the Ticker Index File')
	with col4: show_industries = st.button('Show Industry Summary')
	
	st.markdown("""---""")
	
	if download_ticker_index:
		st.subheader('Downloading Ticker Master Data from https://asx.api.markitdigital.com and adding to the Ticker Index File')
		refresh_ticker_index_file(st.session_state)
	
	if show_ticker_index:
		st.subheader('Ticker Index File')
		st.dataframe(scope.ticker_index_file, 2000, 1200)

	if show_industries:
		print_industries_in_ticker_index(scope)


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# TICKER INDEX FILE - loader and Saver
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def load_ticker_index_file( scope ):
	st.title('Loading Ticker Index File')

	if os.path.exists( scope.path_ticker_index ):
		st.info('loading ticker_index.csv file from ' +  str(scope.path_ticker_index) )

		ticker_index = pd.read_csv(  scope.path_ticker_index, 
									dtype=ticker_index_schema_csv_dtypes(),
									parse_dates=ticker_index_schema_csv_dates(),
									)
		# ticker_index['blue_chip'] = ticker_index['blue_chip'].astype(int)
		ticker_index['listing_date'] = pd.to_datetime( ticker_index['listing_date'].dt.date  )
		st.success('successfully loaded the ticker index file')
		ticker_index.set_index('share_code', inplace=True)
		# remove any delisted stocks here
		scope.ticker_index_file = ticker_index
		scope.update_lists_for_dropdowns = True
	else: 
		st.error( 'Ticker Index File does not exist at path > ' + str(scope.path_ticker_index) )
		st.info( 'creating an empty ticker_index dataframe' )
		dataframe_columns = []
		for column_name in ticker_index_schema: 
			dataframe_columns.append(column_name)
			ticker_index = pd.DataFrame(columns=dataframe_columns)
		st.success('successfully created empty Ticker Index dataframe')
		ticker_index.set_index('share_code', inplace=True)
		# remove any delisted stocks here
		scope.ticker_index_file = ticker_index
		save_ticker_index_file(scope)
		st.markdown("""---""")
		st.error('Click on the Ticker Index button to update the Ticker Index')

def save_ticker_index_file( scope ): # DONE
	# st.subheader('Save Ticker Index File')
	saving_df = scope.ticker_index_file.copy()
	saving_df.reset_index(inplace=True)      	 # ensure that the index is saved as a normal column
	saving_df.to_csv( scope.path_ticker_index, index=False )
	st.success('saved Ticker Index file')

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# TICKER INDEX FILE - Downloader + helpers
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def refresh_ticker_index_file(scope):
	st.info('Downloading Ticker Index information for the ' + scope.share_market)
	if scope.share_market == 'ASX':
		url = 'https://asx.api.markitdigital.com/asx-research/1.0/companies/directory/file?'
		column_names = ['share_code', 'company_name', 'listing_date', 'industry_group', 'market_cap' ]
		downloaded_ticker_info = pd.read_csv( 	url, 
												skiprows=1, 
												names=column_names, 
												header=0, 
												dtype={
													'share_code':'str',
													'company_name':'str',
													'industry_group':'str',
													'market_cap':'float',
												},
												parse_dates=['listing_date'])
		downloaded_ticker_info['share_code'] = downloaded_ticker_info['share_code'] + '.AX'
		downloaded_ticker_info['listing_date'] = pd.to_datetime( downloaded_ticker_info['listing_date'].dt.date  )

		# format the industry group field - remove redundant values
		downloaded_ticker_info['industry_group'] = downloaded_ticker_info['industry_group'].fillna('zz_industry_group')
		downloaded_ticker_info['industry_group'] = downloaded_ticker_info['industry_group'].str.replace(', ', '_' )
		downloaded_ticker_info['industry_group'] = downloaded_ticker_info['industry_group'].str.replace(' ', '_' )
		downloaded_ticker_info['industry_group'] = downloaded_ticker_info['industry_group'].str.replace('&', 'and' )
		downloaded_ticker_info['industry_group'] = downloaded_ticker_info['industry_group'].str.lower()

		st.success('number of downloaded ' + scope.share_market + ' ticker codes = ' + str(len(downloaded_ticker_info)))
		update_ticker_index_with_latest_download(scope, downloaded_ticker_info )
		scope.update_lists_for_dropdowns = True
	else:
		st.error('DOWNLOAD Ticker data NOT YET CONFIGURED FOR ' + scope.share_market)
		pass

def update_ticker_index_with_latest_download(scope, downloaded_ticker_info ):
	st.info( 'Updating the records in the Ticker Index file ')

	add_records_counter = 0

	downloaded_ticker_info = apply_defaults_to_missing_values(scope, downloaded_ticker_info)
	downloaded_ticker_info.set_index('share_code', inplace=True)
	render_results( scope, passed='Updating these Tickers > ', passed_2='Adding these Tickers > ', failed='not applicable > ' )

	for ticker, row in downloaded_ticker_info.iterrows(): 
		# 
		if ticker not in scope.ticker_index_file.index:
			add_records_counter += 1
			row['opening_time'] = ticker_open_time( scope, ticker )
			row['minutes_per_day'] = ticker_trading_mins_per_day( scope, ticker )
			row['blue_chip'] = ticker_index_schema['blue_chip']['default']
			scope.ticker_index_file = scope.ticker_index_file.append(row)
			render_results( scope, ticker, result='passed_2' )
		else:
			scope.ticker_index_file.at[ticker, 'company_name'] = row['company_name']
			scope.ticker_index_file.at[ticker, 'listing_date'] = row['listing_date']
			scope.ticker_index_file.at[ticker, 'industry_group'] = row['industry_group']
			scope.ticker_index_file.at[ticker, 'market_cap'] = row['market_cap']
			render_results( scope, ticker, result='passed' )
	render_results(scope, 'Finished', final_print=True )
	scope.ticker_index_file = apply_defaults_to_missing_values(scope, scope.ticker_index_file)
	scope.ticker_index_file['listing_date'] = pd.to_datetime( scope.ticker_index_file['listing_date'].dt.date  )
	scope.ticker_index_file = scope.ticker_index_file.sort_index()
	message = 'number of ticker codes added to master ticker index = '+ str(add_records_counter)
	st.warning( message) if add_records_counter > 0 else st.info( message)
	save_ticker_index_file(scope)
	scope.ticker_list_needs_updating = True

def apply_defaults_to_missing_values(scope, dataframe):
	defaults = ticker_index_schema_defaults()
	dtypes = ticker_index_schema_dtypes()

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

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ticker Index file Schema - Helpers
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def ticker_index_schema_dtypes():
	dtypes={}
	for field, schema in ticker_index_schema.items():
		dtypes[field] = schema['dtype']
	return dtypes

def ticker_index_schema_defaults():
	defaults={}
	for field, schema in ticker_index_schema.items():
		defaults[field] = schema['default']
	return defaults

def ticker_index_schema_csv_dtypes():
	dtypes={}
	for field, schema in ticker_index_schema.items():
		if schema['dtype'] != 'datetime64[ns]': 
			dtypes[field] = schema['dtype']
	return dtypes

def ticker_index_schema_csv_dates():
	dates_to_parse = []
	for field, schema in ticker_index_schema.items():
		if schema['dtype'] == 'datetime64[ns]': 
			dates_to_parse.append(field)
	return dates_to_parse

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ticker Helpers
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def ticker_open_time( scope, ticker):
	market = scope.share_market
	ticker_code_first_letter = ticker[0].upper()
	for group in scope.market_opening_hours[market].keys():
		if group != 'timezone':
			if ticker_code_first_letter in scope.market_opening_hours[market][group]['letter_range']:
				opening_time = scope.market_opening_hours[market][group]['opening_time']
	return( opening_time )

def ticker_trading_mins_per_day( scope, ticker ):
	market = scope.share_market
	ticker_code_first_letter = ticker[0].upper()
	for group in scope.market_opening_hours[market].keys():
		if group != 'timezone':
			if ticker_code_first_letter in scope.market_opening_hours[market][group]['letter_range']:
				trading_minutes_per_day = scope.market_opening_hours[market][group]['minutes_per_day']
	return trading_minutes_per_day 

# -----------------------------------------------------------------------------------------------------------------------------------
# Ticker Index Industry Report
# -----------------------------------------------------------------------------------------------------------------------------------
def print_industries_in_ticker_index(scope):
	st.subheader('Ticker Index File contains the following Industries')
	industry_group_count = pd.DataFrame(scope.ticker_index_file['industry_group'].value_counts().rename_axis('Industry').reset_index(name='No of Codes'))
	industry_group_count = industry_group_count.sort_values(by='Industry')
	st.dataframe(industry_group_count, 2000, 1200)
