# streamlit run app.py



import pandas as pd
import yfinance as yf
import streamlit as st
st.set_page_config(layout="wide")
import datetime as dt
import plotly.graph_objects as go
from plotly.subplots import make_subplots



from params import set_session_variables, construct_list_of_share_codes
from share_index import refresh_share_index_file
from volume import average_volume
# ======================================================================================================================================================
#
project_description = 'Share Trading Application - Trading Strategy Discovery Tool'
#
# ======================================================================================================================================================

set_session_variables(st.session_state, project_description)

# print ( st.session_state)


#----------------------------------- Build Web Interface
# Establish Initial List

def update_ticker_list():
	st.session_state.update_ticker_list = True


# ================================================================================================ Sidebar


# ------------------------------------------------------------------------------------------------ Share Data
st.sidebar.header('Share Market and Tickers')
market = st.sidebar.selectbox('Select Market', st.session_state.available_markets, on_change=update_ticker_list)
industry = st.sidebar.multiselect('Select Industry', st.session_state.available_industries, on_change=update_ticker_list, help='This is help')
tickers = st.sidebar.multiselect('Select Ticker(s)', st.session_state.available_tickers, on_change=update_ticker_list) 

if st.session_state.update_ticker_list:
	st.session_state.selected_market = market
	st.session_state.selected_industry = industry
	st.session_state.selected_tickers = tickers
	construct_list_of_share_codes(st.session_state)
# ------------------------------------------------------------------------------------------------ Download Share Data
st.sidebar.header('Download New Share Data')
refresh_tickers = st.sidebar.button('Update List of Valid Tickers')
no_of_days = st.sidebar.number_input('Number of Days to Download', min_value=1, max_value=10, value=1, key='0')    
download_tickers = st.sidebar.button('Download OHLC Data')

if refresh_tickers:
	refresh_share_index_file(st.session_state)

# ------------------------------------------------------------------------------------------------ Quick Volume Calculator
st.sidebar.header('Daily Volume Analysis')
volume_today = st.sidebar.button('Daily Volume Analysis')

if volume_today:
	average_volume(st)


# ------------------------------------------------------------------------------------------------ Application Parameters
param_group = st.sidebar.selectbox(
									'Application Parameters',
									(
										'< select group >',
										'........................................................',
										'Ticker Lists',
										'Industries',
										'........................................................',
										'Share Index File', 
										'Share Data Files', 
										'.......................................parameters',
										'Streamlit',
										'.......................................parameters',
										'Application',
										'Market', 
										'Folders', 
										'Strategy', 
										'Charting', 
										'Terminal',
										)
)

if param_group == 'Ticker Lists':
	st.header('Ticker Lists')
	
	st.subheader('Update the Ticker List ?')
	st.code('update_ticker_list')
	st.write(st.session_state.update_ticker_list)

	#TODO - Rob - we need to show the actual ticker list here

	st.subheader('Loaded Ticker List')
	st.code('share_data_loaded_list')
	st.write(st.session_state.share_data_loaded_list)

	st.subheader('Missing Ticker List')
	st.code('share_data_missing_list')
	st.write(st.session_state.share_data_missing_list)

if param_group == 'Industries': # DONE
	st.header('Share Index File contains the following Industries')
	industry_group_count = pd.DataFrame(st.session_state.share_index_file['industry_group'].value_counts())
	industry_group_count.index.name = 'Industry'
	industry_group_count.columns =['No of Codes']
	st.table(industry_group_count)

if param_group == 'Share Index File': # DONE
	st.header('Share Index File')
	st.code('share_index_file')
	st.dataframe(st.session_state.share_index_file, 2000, 1200)

if param_group == 'Share Data Files':
	st.header('Share Data Files')
	#TODO - does this need to be a table - we need to load some data before checking
	# TODO - Rob - I dont think the lists belong in this section
	
	st.subheader('Share Data Files (loaded)')
	st.code('share_data_files')
	st.write(st.session_state.share_data_files)

if param_group == 'Streamlit': # DONE
	st.header('Streamlit Application Variables')

	st.subheader('Initial Run / load < initial_run >')
	st.code('initial_run')
	st.write(st.session_state.initial_run)

	st.subheader('List of Available Markets Generated for Steamlit')
	st.code('available_markets')
	st.write(st.session_state.available_markets)

	st.subheader('List of Available Industries Generated for Steamlit')
	st.code('available_industries')
	st.write(st.session_state.available_industries)

	st.subheader('List of Available Tickers Generated for Steamlit')
	st.code('available_tickers')
	st.write(st.session_state.available_tickers)

if param_group == 'Application': # DONE
	st.header('Application Parameters')

	st.subheader('Project Description')
	st.code('project_description')
	st.write(st.session_state.project_description)

	st.subheader('Project Start Time')
	st.code('project_start_time')
	st.write(st.session_state.project_start_time)

if param_group == 'Market': # DONE
	st.header('Market Parameters')

	st.subheader('Available Markets')
	st.code('available_markets')
	st.dataframe(st.session_state.available_markets, 2000, 1200)

	st.subheader('Selected Market')
	st.code('selected_market')
	st.write(st.session_state.selected_market)

	st.subheader('Market Share Suffix')
	st.code('market_suffix')
	st.dataframe(st.session_state.market_suffix, 2000, 1200)

	st.subheader('Public Holidays')
	st.code('market_public_holidays')
	st.write(st.session_state.market_public_holidays)

	st.subheader('Opening Hours')
	st.code('market_opening_hours')
	st.write(st.session_state.market_opening_hours)

if param_group == 'Folders': #DONE
	st.header('Folders and Paths')

	st.subheader('Project Folder')
	st.code('folder_project')
	st.write(st.session_state.folder_project)

	st.subheader('Share Data Folder')
	st.code('folder_share_data')
	st.write(st.session_state.folder_share_data)

	st.subheader('Results Analysis Folder')
	st.code('folder_results_analysis')
	st.write(st.session_state.folder_results_analysis)

	st.subheader('Website Output Folder')
	st.code('folder_website')
	st.write(st.session_state.folder_website)

	st.subheader('Path for Share Index File')
	st.code('path_share_index')
	st.write(st.session_state.path_share_index)

	st.subheader('Path for Website Output File')
	st.code('path_website_file')
	st.write(st.session_state.path_website_file)

	st.subheader('Path for Share Data File')
	st.code('path_share_data_file')
	st.write(st.session_state.path_share_data_file)

if param_group == 'Strategy': #DONE
	st.header('Strategy Parameters')

	st.subheader('Strategy Name')
	st.code('strategy_name')
	st.write(st.session_state.strategy_name)

	st.subheader('Print Header')
	st.code('strategy_print_header')
	st.write(st.session_state.strategy_print_header)

	st.subheader('Price Columns')
	st.code('strategy_price_columns')
	st.dataframe(st.session_state.strategy_price_columns, 2000, 1200)

	st.subheader('Print Count')
	st.code('strategy_print_count')
	st.write(st.session_state.strategy_print_count)

	st.subheader('Build Header')
	st.code('strategy_build_header')
	st.write(st.session_state.strategy_build_header)

	st.subheader('Header')
	st.code('strategy_header')
	st.write(st.session_state.strategy_header)

	st.subheader('Print Line')
	st.code('strategy_print_line')
	st.write(st.session_state.strategy_print_line)

	st.subheader('Json Dicitionary')
	st.code('strategy_json_dict')
	st.write(st.session_state.strategy_json_dict)

	st.subheader('Results Dataframe')
	st.code('strategy_results')
	st.dataframe(st.session_state.strategy_results, 2000, 1200)

if param_group == 'Charting': # DONE
	st.header('Charting Parameters')

	st.subheader('Chart Line')
	st.code('chart_lines')
	st.write(st.session_state.chart_lines)
	
	st.subheader('Chart MACD on Price')
	st.code('chart_macd_on_price')
	st.write(st.session_state.chart_macd_on_price)

	st.subheader('Chart MACD on Volume')
	st.code('chart_macd_on_volume')
	st.write(st.session_state.chart_macd_on_volume)

if param_group == 'Terminal': # DONE
	st.header('Terminal Parameters')

	st.subheader('Terminal Audit')
	st.code('terminal_audit')
	st.write(st.session_state.terminal_audit)

	st.subheader('Terminal Width')
	st.code('terminal_width')
	st.write(st.session_state.terminal_width)

	st.subheader('Terminal Print Width')
	st.code('terminal_print_width')
	st.write(st.session_state.terminal_print_width)

	st.subheader('Terminal Count Passed')
	st.code('terminal_count_passed')
	st.write(st.session_state.terminal_count_passed)

	st.subheader('Terminal Count_2 Passed')
	st.code('terminal_count_passed_2')
	st.write(st.session_state.terminal_count_passed_2)

	st.subheader('Terminal Count Failed')
	st.code('terminal_count_failed')
	st.write(st.session_state.terminal_count_failed)









# ------------------------------------------------------------------------------------------------ Perform Analysis

select_page = st.sidebar.radio(
		"Choose select_page",
		(
			# 'Todays Volume', 
			# 'Ticker Each Day', 
			# 'Volume Analysis', 
			'Fliss Simple', 
			'Johnny Bravo', 
			'MACD', 
			'MACD All Combos',


		)
	) 



# ================================================================================================ Variables

# ------------------------------------------------------------------------------------------------ Analysis
if select_page=='Analysis Settings':
	no_of_days = st.number_input("Number of days in analysis", value=365)
	trade_value = st.number_input("trade value", value=10000.00, format="%.2f")
	trade_cost = st.number_input("trade cost", value=32.15, format="%.2f")
	st.subheader('Selected Options - from the drop downs') 
	col1,col2 = st.columns([5,4])
	with col1: 
		st.write('Selected Market')
		st.write('Selected Industry')
		st.write('Selected Tickers')
	with col2: 
		st.write(st.session_state.selected_market)
		st.write(st.session_state.selected_industry)
		st.write(st.session_state.selected_tickers)
	st.subheader('Ticker List <ticker_list>') 
	st.write('Update the Ticker List ?', str(st.session_state.update_ticker_list))
	st.write(st.session_state.ticker_list)

# ------------------------------------------------------------------------------------------------ Share Index

#----------------------------------- Update Values


	# fundInfo = {
	# 		'Enterprise Value (USD)': info['enterpriseValue'],
	# 		'Enterprise To Revenue Ratio': info['enterpriseToRevenue'],
	# 		'Enterprise To Ebitda Ratio': info['enterpriseToEbitda'],
	# 		'Net Income (USD)': info['netIncomeToCommon'],
	# 		'Profit Margin Ratio': info['profitMargins'],
	# 		'Forward PE Ratio': info['forwardPE'],
	# 		'PEG Ratio': info['pegRatio'],
	# 		'Price to Book Ratio': info['priceToBook'],
	# 		'Forward EPS (USD)': info['forwardEps'],
	# 		'Beta ': info['beta'],
	# 		'Book Value (USD)': info['bookValue'],
	# 		'Dividend Rate (%)': info['dividendRate'], 
	# 		'Dividend Yield (%)': info['dividendYield'],
	# 		'Five year Avg Dividend Yield (%)': info['fiveYearAvgDividendYield'],
	# 		'Payout Ratio': info['payoutRatio']
	# 	}
	
	# fundDF = pd.DataFrame.from_dict(fundInfo, orient='index')
	# fundDF = fundDF.rename(columns={0: 'Value'})
	# st.subheader('Fundamental Info') 
	# st.table(fundDF)







# special_session_variables=[
# 							'available_markets', 'available_industries', 'available_tickers', # these are in the drop_down lists
# 							'ticker_list', 'update_ticker_list', 'selected_market', 'selected_industry', 'selected_tickers',
# 							'share_index_file',
# 							'share_data_files',
# 							'share_data_loaded_list', 'share_data_missing_list', 'share_data_schema', 'share_data_usecols', 'share_data_dtypes', 'share_data_dates',
# 							'market_suffix', 'market_public_holidays', 'market_opening_hours',
# 							'folder_project', 'folder_share_data', 'folder_results_analysis', 'folder_website',
# 							'path_share_index', 'path_website_file', 'path_share_data_file',
# 							'strategy_build_header', 'strategy_header', 'strategy_json_dict', 'strategy_name', 'strategy_price_columns', 
# 							'strategy_print_count', 'strategy_print_header', 'strategy_print_line', 'strategy_results',
# 							'chart_lines', 'chart_macd_on_price', 'chart_macd_on_volume', 
# 							]

# if param_group == 'Other':
# 	st.header('Session Variables')
# 	col1,col2 = st.columns([2,5])

# 	list_of_params = (list(st.session_state))
# 	list_of_params.sort()
# 	for session_var in list_of_params:
# 		if session_var not in special_session_variables:
# 			st.subheader(session_var)
# 			st.write(st.session_state[session_var])