import streamlit as st


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
