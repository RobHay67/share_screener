import streamlit as st

from ticker.load import load_single_ticker_file, load_multiple_ticker_files
from ticker.download import load_and_download_ticker_data
from ticker.analysis_df import establish_analysis_df

from system.ticker_files import view_a_ticker_file, view_all_loaded_ticker_files
from system.analysis import view_an_analysis_file, view_all_analysis_files







# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Single Ticker Loader
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def single_loader(scope, page):

	col1,col2,col3,col4,col5,col6 = st.columns([2.0, 2.0, 1.5, 1.5, 2.0, 3.0])
	with col1: select_a_ticker(scope, page)

	ticker = scope.selected[page]['ticker_list'][0]
	
	if ticker != 'select a ticker':	
		download_button_msg = 'Download ' + str(int(scope.download_days)) + ' day'
		if scope.download_days > 1: download_button_msg += 's'

		with col4: load_tickers 	= st.button( 'Load This File')
		with col4: download_tickers = st.button(download_button_msg)
		with col6: st.button('Clear any messages')
		

		if load_tickers : 
			scope.download_industries = ['random_tickers']									# used for y_finance downloading
			load_single_ticker_file(scope, ticker)											

		if download_tickers:
			scope.download_industries = ['random_tickers']									# used for y_finance downloading
			load_and_download_ticker_data(scope)

		if ticker in list(scope.ticker_data_files.keys()):
			no_of_loaded_rows = len(scope.ticker_data_files[ticker])
			establish_analysis_df(scope, ticker, no_of_loaded_rows)
			no_of_analysis_rows = len(scope.selected[scope.display_page]['analysis_df'][ticker])

			with col5: show_ticker_data = st.button(('Loaded Rows = ' + str(no_of_loaded_rows)))
			with col5: show_analysis_data = st.button(('Analysis Rows = ' + str(no_of_analysis_rows)))
			

			if show_ticker_data:
				view_a_ticker_file(scope, ticker)

			if show_analysis_data:
				view_an_analysis_file(scope)

			# Render the Company Name
			col1,col2,col3,col4 = st.columns([7.0, 1.7, 0.3, 3.0])
			with col1: st.header( scope.ticker_index.loc[ticker]['company_name'] )

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Multi Ticker Loader
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def multi_loader(scope):
	
	col1,col2,col3,col4,col5,col6 = st.columns([2,3,2,1.2,2,1.8])

	with col1: select_a_market(scope)
	with col2: select_industries(scope)
	with col3: select_tickers(scope)
	
	if scope.selected['multi']['market'] != 'select entire market' or (len(scope.selected['multi']['industries']) != 0) or len(scope.selected['multi']['tickers']) != 0:
		total_loaded_rows, total_analysis_rows = 0, 0
		
		download_button_msg = 'Download ' + str(int(scope.download_days)) + ' day'
		if scope.download_days > 1: download_button_msg += 's'

		with col4: load_tickers 	= st.button( 'Load These Files')
		with col4: download_tickers = st.button(download_button_msg)
		with col6: st.button('Clear any Messages')

		update_multi_ticker_list(scope)

		if load_tickers : 
			# scope.download_industries is establised by the update_multi_ticker_list() function
			load_multiple_ticker_files(scope)

		if download_tickers:
			# scope.download_industries is establised by the update_multi_ticker_list() function
			load_and_download_ticker_data(scope)

		# iterate through loaded ticker list and call the establish_analysis_df method 
		list_of_loaded_files = list(scope.ticker_data_files.keys())
		no_of_loaded_files = len(list_of_loaded_files)

		for ticker in list_of_loaded_files:
			no_of_loaded_rows = len(scope.ticker_data_files[ticker])
			establish_analysis_df(scope, ticker, no_of_loaded_rows)

			no_of_analysis_rows = len(scope.selected['multi']['analysis_df'][ticker])

			total_loaded_rows += no_of_loaded_rows
			total_analysis_rows += no_of_analysis_rows

		no_of_analysis_files = len(scope.selected['multi']['analysis_df'])

		with col5: show_ticker_files   = st.button(('Loaded Files   = ' + str(no_of_loaded_files)   + ' rows = ' + str(total_loaded_rows)))
		with col5: show_analysis_files = st.button(('Analysis Files = ' + str(no_of_analysis_files) + ' rows = ' + str(total_analysis_rows)))


		if show_ticker_files:
			view_all_loaded_ticker_files(scope)

		if show_analysis_files:
			view_all_analysis_files(scope)



# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Single Ticker Page Helpers
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def select_a_ticker(scope, page):
	
	# Previous Selection
	previous_ticker_for_page = scope.selected[page]['ticker_list'][0]

	# render the selector defalted to the stored ticker for this page
	selected_ticker = st.selectbox ( 
									label='Select a Ticker', 
									options=scope.dropdown_ticker,
									index=scope.dropdown_ticker.index(previous_ticker_for_page), 
									help='Choose a ticker for analysis. Start typing to jump within list',
									key=page,
									) 
	# Store the selection so we can easily swap pages
	scope.selected[page]['ticker_list'] = [selected_ticker]

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Multi Page - Selectors
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def select_a_market(scope):

	previous_selection = scope.selected['multi']['market']

	selected_market = st.selectbox(
									label='Add a Market to Ticker List',
									options=scope.dropdown_markets, 
									index=scope.dropdown_markets.index(previous_selection), 
									help='Select an Entire Share Market for Analysis',
									key='1'
									)

	scope.selected['multi']['market'] = selected_market

def select_industries(scope):

	selected_industries = st.multiselect(
									label='Add an Industry or Industries',
									options=scope.dropdown_industries, 
									default=scope.selected['multi']['industries'], 
									help='Quickly Select all tickers in a particular industry',
									key='2'
									)

	scope.selected['multi']['industries'] = selected_industries

def select_tickers(scope):

	selected_tickers = st.multiselect(
									label='Add a Ticker or Tickers',
									options=scope.dropdown_tickers, 
									default=scope.selected['multi']['tickers'], 
									help='Select a ticker, or multiple tickers from the dropdown. Start typing to jump within list',
									key='3'
									)

	scope.selected['multi']['tickers'] = selected_tickers

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Multi Page - Ticker List Constructor
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

def update_multi_ticker_list(scope):
	
	ticker_list = []
	relevant_industries = []
	
	# ################################################################################
	# Most detailed takes precedence
	# ################################################################################

	# Selected a ticker or tickers
	if len(scope.selected['multi']['tickers']) != 0:
		for ticker in scope.selected['multi']['tickers']:
			ticker_list.append(ticker)
			relevant_industries = ['random_tickers']
		pass
	# Selected an Industry
	elif len(scope.selected['multi']['industries']) != 0:
		for industry in scope.selected['multi']['industries']:
			tickers_in_industry_df = scope.ticker_index[scope.ticker_index['industry_group'] == industry ]
			tickers_in_industry = tickers_in_industry_df.index.tolist()
			ticker_list += tickers_in_industry 
			relevant_industries.append(industry)
		pass
	
	# Selected an entire share market
	elif scope.selected['multi']['market'] != 'select entire market':
		tickers_in_market = scope.ticker_index.index.values.tolist()
		ticker_list = tickers_in_market
		relevant_industries = ( list(scope.ticker_index['industry_group'].unique() ))
	
	scope.selected['multi']['ticker_list'] = ticker_list
	scope.download_industries = relevant_industries










# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Helpers for All Pages - Options and Buttons
# -------------------------------------------------------------------------------------------------------------------------------------------------------------


# def no_of_loaded_rows(scope, ticker):

# 	min_value,max_value,default_value,no_of_rows=0,0,0,0	

# 	# Count the rows in loaded dataframe
# 	if ticker in list(scope.ticker_data_files.keys()):
# 		min_value = 1
# 		no_of_rows = len(scope.ticker_data_files[ticker])
# 		max_value = no_of_rows if no_of_rows > 0 else 0
# 		default_value = 300 if max_value > 300 else max_value		
	
# 	return min_value,max_value,default_value,no_of_rows


