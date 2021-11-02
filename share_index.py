# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# External Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
import pandas as pd
import os
import datetime
import streamlit as st

from web import output_results_to_browser


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Share Index file Schema
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
share_index_schema ={
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

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Browser Render Controller
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def render_share_index_page(scope):

	st.title('Maintain the Share Index File')

	# share_index_message = str((len(scope.share_index_file)))
	
	st.success(('Share Index contains ( ' + str((len(scope.share_index_file))) + ' ) tickers'))
	col1,col2,col3 = st.columns([3,3,3])
	with col1: show_share_index = st.button('Display the Share Index File')
	with col2: show_industries = st.button('Industry Summary')
	with col3: download_share_index = st.button('Update List of Valid Tickers')

	st.markdown("""---""")
	
	if download_share_index:
		st.subheader('Downloading Share Data from https://asx.api.markitdigital.com and adding to the Share Index File')
		refresh_share_index_file(st.session_state)
	
	if show_share_index:
		st.subheader('Share Index File')
		st.dataframe(scope.share_index_file, 2000, 1200)

	if show_industries:
		print_share_index_industries(scope)


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# SHARE INDEX FILE - loader and Saver
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def load_share_index_file( scope ):
	st.title('Loading Share Index File')

	if os.path.exists( scope.path_share_index ):
		st.info('loading share_index.csv file from ' +  str(scope.path_share_index) )

		share_index = pd.read_csv(  scope.path_share_index, 
									dtype=share_index_schema_csv_dtypes(),
									parse_dates=share_index_schema_csv_dates(),
									)
		# share_index['blue_chip'] = share_index['blue_chip'].astype(int)
		share_index['listing_date'] = pd.to_datetime( share_index['listing_date'].dt.date  )
		st.success('successfully loaded the share index file')
		share_index.set_index('share_code', inplace=True)
		# remove any delisted stocks here
		scope.share_index_file = share_index
	else: 
		st.error( 'Share Index File does not exist at path > ' + str(scope.path_share_index) )
		st.info( 'creating an empty share_index dataframe' )
		dataframe_columns = []
		for column_name in share_index_schema: 
			dataframe_columns.append(column_name)
			share_index = pd.DataFrame(columns=dataframe_columns)
		st.success('successfully created empty share index dataframe')
		share_index.set_index('share_code', inplace=True)
		# remove any delisted stocks here
		scope.share_index_file = share_index
		save_share_index_file(scope)
		st.markdown("""---""")
		st.error('Click on the Share Index button to update the Share Index')

def save_share_index_file( scope ): # DONE
	st.subheader('Save Share Index File')
	saving_df = scope.share_index_file.copy()
	saving_df.reset_index(inplace=True)      	 # ensure that the index is saved as a normal column
	saving_df.to_csv( scope.path_share_index, index=False )
	st.success('successfully saved share Index file')

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# SHARE INDEX FILE - Downloader + helpers
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def refresh_share_index_file(scope):
	st.info('Downloading Share Index information for the ' + scope.share_market)
	if scope.share_market == 'ASX':
		url = 'https://asx.api.markitdigital.com/asx-research/1.0/companies/directory/file?'
		column_names = ['share_code', 'company_name', 'listing_date', 'industry_group', 'market_cap' ]
		downloaded_share_info = pd.read_csv( 	url, 
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
		downloaded_share_info['share_code'] = downloaded_share_info['share_code'] + '.AX'
		downloaded_share_info['listing_date'] = pd.to_datetime( downloaded_share_info['listing_date'].dt.date  )

		# format the industry group field - remove redundant values
		downloaded_share_info['industry_group'] = downloaded_share_info['industry_group'].fillna('zz_industry_group')
		downloaded_share_info['industry_group'] = downloaded_share_info['industry_group'].str.replace(', ', '_' )
		downloaded_share_info['industry_group'] = downloaded_share_info['industry_group'].str.replace(' ', '_' )
		downloaded_share_info['industry_group'] = downloaded_share_info['industry_group'].str.replace('&', 'and' )
		downloaded_share_info['industry_group'] = downloaded_share_info['industry_group'].str.lower()

		st.success('number of downloaded ' + scope.share_market + ' share codes = ' + str(len(downloaded_share_info)))
		update_share_index_with_latest_download(scope, downloaded_share_info )
	else:
		st.error('DOWNLOAD Share data NOT YET CONFIUGURED FOR ' + scope.share_market)
		pass

def update_share_index_with_latest_download(scope, downloaded_share_info ):
	st.info( 'Updating the share records in the Share Index file ')

	add_records_counter = 0

	downloaded_share_info = apply_defaults_to_missing_values(scope, downloaded_share_info)
	downloaded_share_info.set_index('share_code', inplace=True)
	output_results_to_browser( scope, passed='Updated these Shares > ', passed_2='Added these Shares > ', failed='not applicable > ' )

	for ticker, row in downloaded_share_info.iterrows(): 
		# 
		if ticker not in scope.share_index_file.index:
			add_records_counter += 1
			row['opening_time'] = ticker_open_time( scope, ticker )
			row['minutes_per_day'] = ticker_trading_mins_per_day( scope, ticker )
			row['blue_chip'] = share_index_schema['blue_chip']['default']
			scope.share_index_file = scope.share_index_file.append(row)
			output_results_to_browser( scope, ticker, result='passed_2' )
		else:
			scope.share_index_file.at[ticker, 'company_name'] = row['company_name']
			scope.share_index_file.at[ticker, 'listing_date'] = row['listing_date']
			scope.share_index_file.at[ticker, 'industry_group'] = row['industry_group']
			scope.share_index_file.at[ticker, 'market_cap'] = row['market_cap']
			output_results_to_browser( scope, ticker, result='passed' )
	output_results_to_browser(scope, 'Finished', final_print=True )
	scope.share_index_file = apply_defaults_to_missing_values(scope, scope.share_index_file)
	scope.share_index_file['listing_date'] = pd.to_datetime( scope.share_index_file['listing_date'].dt.date  )
	scope.share_index_file = scope.share_index_file.sort_index()
	message = 'number of share codes added to master share index = '+ str(add_records_counter)
	st.warning( message) if add_records_counter > 0 else st.info( message)
	save_share_index_file(scope)
	scope.ticker_list_needs_updating = True

def apply_defaults_to_missing_values(scope, dataframe):
	defaults = share_index_schema_defaults()
	dtypes = share_index_schema_dtypes()

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
# Share Index file Schema - Helpers
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def share_index_schema_dtypes():
	dtypes={}
	for field, schema in share_index_schema.items():
		dtypes[field] = schema['dtype']
	return dtypes

def share_index_schema_defaults():
	defaults={}
	for field, schema in share_index_schema.items():
		defaults[field] = schema['default']
	return defaults

def share_index_schema_csv_dtypes():
	dtypes={}
	for field, schema in share_index_schema.items():
		if schema['dtype'] != 'datetime64[ns]': 
			dtypes[field] = schema['dtype']
	return dtypes

def share_index_schema_csv_dates():
	dates_to_parse = []
	for field, schema in share_index_schema.items():
		if schema['dtype'] == 'datetime64[ns]': 
			dates_to_parse.append(field)
	return dates_to_parse

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ticker Helpers
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def ticker_open_time( scope, ticker):
	market = scope.share_market
	share_code_first_letter = ticker[0].upper()
	for group in scope.market_opening_hours[market].keys():
		if group != 'timezone':
			if share_code_first_letter in scope.market_opening_hours[market][group]['letter_range']:
				opening_time = scope.market_opening_hours[market][group]['opening_time']
	return( opening_time )

def ticker_trading_mins_per_day( scope, ticker ):
	market = scope.share_market
	share_code_first_letter = ticker[0].upper()
	for group in scope.market_opening_hours[market].keys():
		if group != 'timezone':
			if share_code_first_letter in scope.market_opening_hours[market][group]['letter_range']:
				trading_minutes_per_day = scope.market_opening_hours[market][group]['minutes_per_day']
	return trading_minutes_per_day 

# def extrapolate_average_trading_volume(scope):
# 	st.info('Extrapolating the Current Volume to the End of day - checking momentum')
# 	for ticker in scope.analysis['ticker_list']:
# 		# Only expecting one of these BOQ.AX  
# 		opening_time = scope.share_index_file.loc[ticker]['opening_time']
# 		minutes_per_day = scope.share_index_file.loc[ticker]['minutes_per_day']
# 		open_hour = int(opening_time[:2])
# 		open_minute = int(opening_time[3:5])
# 		# Current time
# 		current_time=datetime.datetime.today()
# 		open_time=current_time.replace(hour=open_hour, minute=open_minute)

# 		# minutes difference
# 		diff_in_seconds = (current_time - open_time).total_seconds()
# 		minutes_elapsed = divmod(diff_in_seconds, 60)[0]

# 		# Now extrapolate
# 		volume_to_date = scope.market_info['average_volume']
# 		average_vol_per_minute = volume_to_date / minutes_elapsed
# 		remaining_minutes = minutes_per_day - minutes_elapsed
# 		extrapolated_daily_volume = "{:8,.0f}".format(average_vol_per_minute * minutes_per_day)
# 		volume_to_date =  "{:8,.0f}".format(volume_to_date)

# 		# Report and Exit 
# 		st.error('TODO - we need this to print on the screen')
# 		print ( white )
# 		print ( '-'*scope.terminal['width'])
# 		print ( ticker, ' - ', scope.share_index_file.loc[ticker]['company_name'])
# 		print ( '-'*scope.terminal['width'])
# 		print ( 'Opening Time              =', open_time.strftime('%Y-%m-%d %H:%M:%S %p'))
# 		print ( 'Current Time              =', current_time.strftime('%Y-%m-%d %H:%M:%S %p'))
# 		print ( '-'*scope.terminal['width'])
# 		print ( 'Total Minutes Elapsed     = ', str(minutes_elapsed))
# 		print ( 'Current Volume            = ' + green + str(volume_to_date) + white )
# 		print ( 'Average Volume per Minute = ', int(average_vol_per_minute), '          ( ', str(volume_to_date), ' / ', str(minutes_elapsed), ' )' )
# 		print ( 'Remaining Minutes         = ', str(remaining_minutes) )
# 		print ( 'Extrapolated EOD Volume   = ', yellow + str(extrapolated_daily_volume) +white+'        ( '+ str(int(average_vol_per_minute))+' x '+ str(minutes_per_day)+' )' )
# 		print ( '-'*scope.terminal['width'])
# 		print ( white)
# 	exit()

# -----------------------------------------------------------------------------------------------------------------------------------
# Share Index Industry Report
# -----------------------------------------------------------------------------------------------------------------------------------
def print_share_index_industries(scope):
	st.subheader('Share Index File contains the following Industries')
	industry_group_count = pd.DataFrame(scope.share_index_file['industry_group'].value_counts().rename_axis('Industry').reset_index(name='No of Codes'))
	industry_group_count = industry_group_count.sort_values(by='Industry')
	st.dataframe(industry_group_count, 2000, 1200)



# -----------------------------------------------------------------------------------------------------------------------------------
# Colours
# -----------------------------------------------------------------------------------------------------------------------------------
red         = '\033[91m'
green       = '\033[92m'
yellow      = '\033[93m'
blue        = '\033[94m'
purple      = '\033[95m'
cyan        = '\033[96m'
white 		= '\033[0m'