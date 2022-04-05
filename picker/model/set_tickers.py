import streamlit as st



def select_tickers(scope):

	previous_selection = scope.pages['screener']['selectors']['tickers']

	new_selection = st.multiselect(
									label='Add a Ticker or Tickers',
									options=scope.config['dropdowns']['tickers'], 
									default=previous_selection, 
									help='Select a ticker, or multiple tickers from the dropdown. Start typing to jump within list',
									key='3'
									)

	scope.pages['screener']['tickers'] = new_selection