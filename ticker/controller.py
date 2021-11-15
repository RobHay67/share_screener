import streamlit as st

from ticker.multi_ticker_list import update_multi_ticker_list
from ticker.load import load_single_ticker_file, load_multiple_ticker_files
from ticker.download import load_and_download_ticker_data
from ticker.files import render_ticker_file, render_ticker_files


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Single Ticker Loader
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def single_loader(scope, page):

	col1,col2,col3,col4,col5,col6 = st.columns([2.0, 2.0, 1.5, 1.5, 2.0, 3.0])
	with col1: select_a_ticker(scope, page)

	ticker = scope.selected[page]['ticker_list'][0]
	
	if ticker != 'select a ticker':	
		with col3: download_days_input(scope)
		with col4: load_tickers 	= st.button( 'Load File')
		with col4: download_tickers = st.button(('Add ' + str(int(scope.download_days)) + ' day'))
		with col5: st.button('Clear temp messages')

		if load_tickers : 
			scope.download_industries = ['random_tickers']									# used for y_finance downloading
			load_single_ticker_file(scope, ticker)											

		if download_tickers:
			scope.download_industries = ['random_tickers']									# used for y_finance downloading
			load_and_download_ticker_data(scope)

		min_value, max_value, default_value, no_of_rows = no_of_loaded_rows(scope, ticker)

		with col5: show_ticker_data = st.button(('Loaded Rows = ' + str(no_of_rows)))

		if show_ticker_data:
			render_ticker_file(scope, ticker)

		# Render the Company Name and an Analysis Row Limit controller
		col1,col2,col3,col4 = st.columns([7.0, 1.7, 0.3, 3.0])
		with col1: st.header( scope.ticker_index.loc[ticker]['company_name'] )
		with col2: limit_analysis(scope, min_value, max_value, default_value)
		with col3: scope.analysis_apply_limit = st.radio( 	"apply",
															('True','False'))
		
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Multi Ticker Loader
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def multi_loader(scope):
	
	col1,col2,col3,col4,col5,col6 = st.columns([2,3,2,1.2,2,1.8])

	# TODO - store this information with the ticker_lists ????
	with col1: select_a_market(scope)
	with col2: select_industries(scope)
	with col3: select_tickers(scope)
	
	if scope.selected['multi']['market'] != 'select entire market' or (len(scope.selected['multi']['industries']) != 0) or len(scope.selected['multi']['tickers']) != 0:
		
		update_multi_ticker_list(scope)

		with col4: load_tickers 	= st.button( 'Load Files')
		with col4: download_tickers = st.button(('Add  ' + str(int(scope.download_days)) + ' days'))
		with col5: st.button('Clear Messages')

		if load_tickers : 
			# scope.download_industries is establised by the update_multi_ticker_list() function
			load_multiple_ticker_files(scope)

		if download_tickers:
			# scope.download_industries is establised by the update_multi_ticker_list() function
			load_and_download_ticker_data(scope)

		with col5: show_ticker_files = st.button(('Loaded Files = ' + str(len(scope.ticker_data_files.keys()))))

		if show_ticker_files:
			render_ticker_files(scope)

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
# Helpers for All Pages - Options and Buttons
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def download_days_input(scope):

	# default_value = int(scope.download_days)	# could not get this to work

	# render the number input widget
	input_download_days = st.number_input( 
								'download days', 
								min_value=1, 
								max_value=6000, 
								value=5, 						# Default Value to display (would revert on every second try)
								key='1'
								)   

	# Store the selection for smoother transition between pages
	scope.download_days = input_download_days

def no_of_loaded_rows(scope, ticker):

	min_value,max_value,default_value,no_of_rows=0,0,0,0	

	# Count the rows in loaded dataframe
	if ticker in list(scope.ticker_data_files.keys()):
		min_value = 1
		no_of_rows = len(scope.ticker_data_files[ticker])
		max_value = no_of_rows if no_of_rows > 0 else 0
		default_value = 300 if max_value > 300 else max_value		
	
	return min_value,max_value,default_value,no_of_rows

def limit_analysis(scope, min_value, max_value, default_value):

	input_analysis_days = st.number_input( 	
								'limit analysis to X rows', 
								min_value=min_value, 
								max_value=max_value, 
								value=default_value,
								key='2'
								)  

	# Store the selection for smoother transition between pages
	scope.analysis_limit_share_data = input_analysis_days
