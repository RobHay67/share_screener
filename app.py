# streamlit run app.py



import pandas as pd
import yfinance as yf
import streamlit as st
st.set_page_config(layout="wide")
import datetime as dt
import plotly.graph_objects as go
from plotly.subplots import make_subplots



from params import set_session_variables, construct_list_of_share_codes
from share_index import refresh_share_index_file, print_share_index_industries

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
st.sidebar.title('Share Data')
market = st.sidebar.selectbox('Select Market', st.session_state.available_markets, on_change=update_ticker_list)
industry = st.sidebar.multiselect('Select Industry', st.session_state.available_industries, on_change=update_ticker_list)
tickers = st.sidebar.multiselect('Select Ticker(s)', st.session_state.available_tickers, on_change=update_ticker_list) 

if st.session_state.update_ticker_list:
	st.session_state.selected_market = market
	st.session_state.selected_industry = industry
	st.session_state.selected_tickers = tickers
	construct_list_of_share_codes(st.session_state)
# ------------------------------------------------------------------------------------------------ Download Share Data
st.sidebar.title('Download Share Data')
refresh_tickers = st.sidebar.button('Update List of Valid Tickers')
no_of_days = st.sidebar.number_input('Number of Days to Download', min_value=1, max_value=10, value=1, key='0')    
download_tickers = st.sidebar.button('Download NOW')

if refresh_tickers:
	refresh_share_index_file(st.session_state)

# ------------------------------------------------------------------------------------------------ Quick Volume Calculator
st.sidebar.title('Daily Volume Analysis')
volume_today = st.sidebar.button('Daily Volume Analysis')

if volume_today:
	average_volume(st)

# ------------------------------------------------------------------------------------------------ Reports
st.sidebar.title('Reports')
industry_report = st.sidebar.button('Industry List')

if industry_report:
	print_share_index_industries(st.session_state)





# ------------------------------------------------------------------------------------------------ Application Parameters
param_group = st.sidebar.selectbox(
	'Application Parameters',
	('< select group >', 'Share Index', 'Share Data Files', 'Market Information', 'Folders', 'Strategy Settings', 'Charting', 'Other')
)

special_session_variables=[
							'available_markets', 'available_industries', 'available_tickers', # these are in the drop_down lists
							'ticker_list', 'update_ticker_list', 'selected_market', 'selected_industry', 'selected_tickers',
							'share_index_file',
							'share_data_files',
							'share_data_loaded_list', 'share_data_missing_list', 'share_data_schema', 'share_data_usecols', 'share_data_dtypes', 'share_data_dates',
							'market_info_markets', 'market_info_public_holidays', 'market_info_opening_hours',
							'folder_project', 'folder_share_data', 'folder_results_analysis', 'folder_website',
							'path_share_index', 'path_website_file', 'path_share_data_file',
							'strategy_build_header', 'strategy_header', 'strategy_json_dict', 'strategy_name', 'strategy_price_columns', 
							'strategy_print_count', 'strategy_print_header', 'strategy_print_line', 'strategy_results',
							'chart_lines', 'chart_macd_on_price', 'chart_macd_on_volume', 
							]

if param_group == 'Share Index':
	st.header('Session Variables - Share Index')
	st.dataframe(st.session_state.share_index_file, 2000, 1200)

if param_group == 'Share Data Files':
	st.header('Session Variables - Share Data Files')

	col1,col2 = st.columns([5,4])
	with col1: 
		st.write('Share Data File      - <share_data_files>')
		st.write('Loaded Tickers List  - <share_data_loaded_list>')
		st.write('Missing Tickers List - <share_data_missing_list>')
	with col2: 
		st.write(st.session_state.share_data_files)
		st.write(st.session_state.share_data_loaded_list)
		st.write(st.session_state.share_data_missing_list)

if param_group == 'Market Information':
	st.header('Session Variables - Market Info')

	st.subheader('Markets')
	st.dataframe(st.session_state.market_info_markets, 2000, 1200)

	st.subheader('Opening Hours')
	st.dataframe(st.session_state.market_info_opening_hours, 2000, 1200)


	st.subheader('Public Holidays')
	# st.dataframe(st.session_state.market_info_public_holidays, 2000, 1200)
	st.write(st.session_state.market_info_public_holidays)

if param_group == 'Folders':
	st.header('Session Variables - Folders and Paths')
	col1,col2 = st.columns([2,5])
	with col1: 
		st.write("folder_project")
		st.write('folder_share_data')
		st.write('folder_results_analysis')
		st.write('folder_website')
		st.write('path_share_index')
		st.write('path_website_file')
		st.write('path_share_data_file')
	with col2: 
		st.write(st.session_state.folder_project)
		st.write(st.session_state.folder_share_data)
		st.write(st.session_state.folder_results_analysis)
		st.write(st.session_state.folder_website)
		st.write(st.session_state.path_share_index)
		st.write(st.session_state.path_website_file)
		st.write(st.session_state.path_share_data_file)

if param_group == 'Strategy Settings':
	st.header('Session Variables - Strategy')

	st.subheader('Strategy Name')
	st.write(st.session_state.strategy_name)

	st.subheader('Print Header')
	st.write(st.session_state.strategy_print_header)

	st.subheader('Price Columns')
	st.dataframe(st.session_state.strategy_price_columns, 2000, 1200)

	st.subheader('Print Count')
	st.write(st.session_state.strategy_print_count)

	st.subheader('Build Header')
	st.write(st.session_state.strategy_build_header)

	st.subheader('Header')
	st.write(st.session_state.strategy_header)

	st.subheader('Print Line')
	st.write(st.session_state.strategy_print_line)

	st.subheader('Json Dicitionary')
	st.write(st.session_state.strategy_json_dict)

	st.subheader('Results Dataframe')
	st.dataframe(st.session_state.strategy_results, 2000, 1200)

if param_group == 'Charting':
	st.header('Session Variables - Charting')
	st.subheader('Have not yet sets these up - this is just a placeholder Name')

if param_group == 'Other':
	st.header('Session Variables')
	col1,col2 = st.columns([2,5])

	list_of_params = (list(st.session_state))
	list_of_params.sort()
	for session_var in list_of_params:
		if session_var not in special_session_variables:
			st.subheader(session_var)
			st.write(st.session_state[session_var])


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


	        #  NaN, 'share_index_schema': {'share_code': {'dtype': 'str', 'default': None}, 'company_name': {'dtype': 'str', 'default': 'zz_missing_company_name'}, 'industry_group': {'dtype': 'str', 'default': 'zz_missing_industry_group'}, 'listing_date': {'dtype': 'datetime64[ns]', 'default': '2000-01-01'}, 'market_cap': {'dtype': 'float64', 'default': 0.0}, 'opening_time': {'dtype': 'str', 'default': None}, 'minutes_per_day': {'dtype': 'float64', 'default': None}, 'blue_chip': {'dtype': 'str', 'default': 'zz_not_yet_tagged'}, 'yahoo_status': {'dtype': 'str', 'default': None}, 'missing_dates': {'dtype': 'object', 'default': None}, 'delisted_date': {'dtype': 'datetime64[ns]', 'default': None}, 'trading_halt_dates': {'dtype': 'object', 'default': None}}, 'share_data_files': {}, 'share_data_loaded_list': [], 'share_data_missing_list': [], 'share_data_schema': {1: {'col_name': 'date', 'index_col': True, 'data_type': 'datetime64[ns]'}, 2: {'col_name': 'open', 'index_col': False, 'data_type': 'float64'}, 3: {'col_name': 'high', 'index_col': False, 'data_type': 'float64'}, 4: {'col_name': 'low', 'index_col': False, 'data_type': 'float64'}, 5: {'col_name': 'close', 'index_col': False, 'data_type': 'float64'}, 6: {'col_name': 'volume', 'index_col': False, 'data_type': 'int64'}, 0: {'col_name': 'ticker', 'index_col': False, 'data_type': None}}, 'share_data_usecols': ['date', 'open', 'high', 'low', 'close', 'volume'], 'share_data_dtypes': {'open': 'float64', 'high': 'float64', 'low': 'float64', 'close': 'float64', 'volume': 'int64'}, 'share_data_dates': ['date'], 'market_info_markets': {'ASX': {'ticker_suffix': '.AX'}, 'USA': {'ticker_suffix': '.US'}}, 'market_info_public_holidays': {'ASX': ['2021-12-28', '2021-12-27', '2021-06-14', '2021-04-25', '2021-04-05', '2021-04-02', '2021-01-26', '2021-01-01', '2020-12-28', '2020-12-25', '2020-06-08', '2020-04-13', '2020-04-10', '2020-01-27', '2020-01-01'], 'USA': ['2021-12-27']}, 'market_info_opening_hours': {'ASX': {'group_1': {'letter_range': ['1', '2', '3', '4', '5', '8', '9', 'A', 'B'], 'opening_time': '10:00:00', 'minutes_per_day': 360}, 'group_2': {'letter_range': ['C', 'D', 'E', 'F'], 'opening_time': '10:02:00', 'minutes_per_day': 357.75}, 'group_3': {'letter_range': ['G', 'H', 'I', 'J', 'K', 'L', 'M'], 'opening_time': '10:05:00', 'minutes_per_day': 355.5}, 'group_4': {'letter_range': ['N', 'O', 'P', 'Q', 'R'], 'opening_time': '10:07:00', 'minutes_per_day': 353.25}, 'group_5': {'letter_range': ['S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 'opening_time': '10:09:00', 'minutes_per_day': 351}}, 'USA': {'group_1': {'letter_range': ['1', '2', '3', '4', '5', '8', '9', 'A', 'B'], 'opening_time': '10:00:00', 'minutes_per_day': 360}}}, 'strategy_name': ('update in params',), 'strategy_print_header': True, 'strategy_price_columns': ['open', 'high', 'low', 'close'], 'strategy_print_count': 0, 'strategy_build_header': True, 'strategy_header': {1: '', 2: '', 3: '', 4: ''}, 'strategy_print_line': '', 'strategy_json_dict': {'shares': {}, 'columnNames': []}, 'strategy_results': {}, 'path_share_data_file': ('not yet set',), 'chart_lines': [], 'chart_macd_on_price': {}, 'chart_macd_on_volume': {}}