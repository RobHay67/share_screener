# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# External Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
import pandas as pd
import os
import datetime
import streamlit as st

from reports import terminal_heading, report_progress, output_result_to_terminal


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
# SHARE INDEX FILE - loader and Saver
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def load_share_index_file( params ):
	st.info('Loading Share Index File')

	if os.path.exists( params.path_share_index ):
		st.info('attemting to load share_index.csv file from ' +  str(params.path_share_index) )

		share_index = pd.read_csv(  params.path_share_index, 
									dtype=share_index_schema_csv_dtypes(),
									parse_dates=share_index_schema_csv_dates(),
									)
		# share_index['blue_chip'] = share_index['blue_chip'].astype(int)
		share_index['listing_date'] = pd.to_datetime( share_index['listing_date'].dt.date  )
		st.success('loaded')

	else: 
		st.error( str(params.path_share_index) + ' path / file does not exist - creating an empty share_index dataframe' + white )
		dataframe_columns = []
		for column_name in share_index_schema: 
			dataframe_columns.append(column_name)
			share_index = pd.DataFrame(columns=dataframe_columns)
		st.success('successfully created empty share index dataframe')

	share_index.set_index('share_code', inplace=True)

	# remove any delisted stocks here

	params.share_index_file = share_index

def save_share_index_file( params ):
	st.info('saving the share index file')
	saving_df = params.share_index_file.copy()
	saving_df.reset_index(inplace=True)      	 # ensure that the index is saved as a normal column
	saving_df.to_csv( params.path_share_index, index=False )
	st.success('saved share Index file')


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# SHARE INDEX FILE - Downloader + helpers
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def refresh_share_index_file(params):
	st.info('Downloading Share Index information for the ' + params.selected_market)
	if params.selected_market == 'ASX':
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

		st.success('number of downloaded ' + params.selected_market + ' share codes = ' + str(len(downloaded_share_info)))
		update_share_index_with_latest_download(params, downloaded_share_info )
		print_share_index_industries(params)

	else:
		st.error('DOWNLOAD Share data NOT YET CONFIUGURED FOR ' + params.selected_market)
		pass

def update_share_index_with_latest_download(params, downloaded_share_info ):
	st.info( 'Updating the share records in the Share Index file ')
	terminal_heading( params, ('Updating the share records in the Share Index file '+ cyan + ' Updated' + '  /  ' + yellow + 'Added New'), line_filler='-' )

	add_records_counter = 0

	downloaded_share_info = apply_defaults_to_missing_values(params, downloaded_share_info)
	downloaded_share_info.set_index('share_code', inplace=True)
	output_result_to_terminal( params )

	for ticker, row in downloaded_share_info.iterrows(): 
		if ticker not in params.share_index_file.index:
			add_records_counter += 1
			row['opening_time'] = ticker_open_time( params, ticker )
			row['minutes_per_day'] = ticker_trading_mins_per_day( params, ticker )
			row['blue_chip'] = share_index_schema['blue_chip']['default']
			params.share_index_file = params.share_index_file.append(row)
			output_result_to_terminal( params, ticker, result='passed_2' )
		else:
			params.share_index_file.at[ticker, 'company_name'] = row['company_name']
			params.share_index_file.at[ticker, 'listing_date'] = row['listing_date']
			params.share_index_file.at[ticker, 'industry_group'] = row['industry_group']
			params.share_index_file.at[ticker, 'market_cap'] = row['market_cap']
			output_result_to_terminal( params, ticker, result='passed' )
	output_result_to_terminal(params, ( ' - updated ' + cyan + str(params.terminal_count_passed) + white + ' added ' + yellow + str(params.terminal_count_passed_2) + white), final_print=True )
	params.share_index_file = apply_defaults_to_missing_values(params, params.share_index_file)
	params.share_index_file['listing_date'] = pd.to_datetime( params.share_index_file['listing_date'].dt.date  )
	params.share_index_file = params.share_index_file.sort_index()
	report_progress( params, 'number of share codes added to master share index', add_records_counter, colour2=green)
	st.success( 'number of share codes added to master share index = '+ str(add_records_counter))
	save_share_index_file(params)

def apply_defaults_to_missing_values(params, dataframe):
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
def ticker_open_time( params, ticker):
	market = params.selected_market
	share_code_first_letter = ticker[0].upper()
	for group in params.market_info_opening_hours[market].keys():
		if share_code_first_letter in params.market_info_opening_hours[market][group]['letter_range']:
			opening_time = params.market_info_opening_hours[market][group]['opening_time']
	return( opening_time )

def ticker_trading_mins_per_day( params, ticker ):
	market = params.selected_market
	share_code_first_letter = ticker[0].upper()
	for group in params.market_info_opening_hours[market].keys():
		if share_code_first_letter in params.market_info_opening_hours[market][group]['letter_range']:
			trading_minutes_per_day = params.market_info_opening_hours[market][group]['minutes_per_day']
	return trading_minutes_per_day 

def extrapolate_average_trading_volume(params):
	st.info('Extrapolating the Current Volume to the End of day - checking momentum')
	for ticker in params.analysis['ticker_list']:
		# Only expecting one of these BOQ.AX  
		opening_time = params.share_index_file.loc[ticker]['opening_time']
		minutes_per_day = params.share_index_file.loc[ticker]['minutes_per_day']
		open_hour = int(opening_time[:2])
		open_minute = int(opening_time[3:5])
		# Current time
		current_time=datetime.datetime.today()
		open_time=current_time.replace(hour=open_hour, minute=open_minute)

		# minutes difference
		diff_in_seconds = (current_time - open_time).total_seconds()
		minutes_elapsed = divmod(diff_in_seconds, 60)[0]

		# Now extrapolate
		volume_to_date = params.market_info['average_volume']
		average_vol_per_minute = volume_to_date / minutes_elapsed
		remaining_minutes = minutes_per_day - minutes_elapsed
		extrapolated_daily_volume = "{:8,.0f}".format(average_vol_per_minute * minutes_per_day)
		volume_to_date =  "{:8,.0f}".format(volume_to_date)

		# Report and Exit 
		st.error('TODO - we need this to print on the screen')
		print ( white )
		print ( '-'*params.terminal['width'])
		print ( ticker, ' - ', params.share_index_file.loc[ticker]['company_name'])
		print ( '-'*params.terminal['width'])
		print ( 'Opening Time              =', open_time.strftime('%Y-%m-%d %H:%M:%S %p'))
		print ( 'Current Time              =', current_time.strftime('%Y-%m-%d %H:%M:%S %p'))
		print ( '-'*params.terminal['width'])
		print ( 'Total Minutes Elapsed     = ', str(minutes_elapsed))
		print ( 'Current Volume            = ' + green + str(volume_to_date) + white )
		print ( 'Average Volume per Minute = ', int(average_vol_per_minute), '          ( ', str(volume_to_date), ' / ', str(minutes_elapsed), ' )' )
		print ( 'Remaining Minutes         = ', str(remaining_minutes) )
		print ( 'Extrapolated EOD Volume   = ', yellow + str(extrapolated_daily_volume) +white+'        ( '+ str(int(average_vol_per_minute))+' x '+ str(minutes_per_day)+' )' )
		print ( '-'*params.terminal['width'])
		print ( white)
	exit()

# -----------------------------------------------------------------------------------------------------------------------------------
# Share Index Industry Report
# -----------------------------------------------------------------------------------------------------------------------------------
def print_share_index_industries(params):
	st.subheader('Share Index File contains the following Industries')
	industry_group_count = pd.DataFrame(params.share_index_file['industry_group'].value_counts())
	industry_group_count.index.name = 'Industry'
	industry_group_count.columns =['No of Codes']
	st.table(industry_group_count)

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