import streamlit as st



def select_tickers(scope):

	page = scope.pages['display_page']
	widget_key = 'widget_' + page + '_select_tickers'



	previous_selection = scope.pages[page]['selectors']['tickers']

	scope.pages[page]['selectors']['tickers'] = st.multiselect(
																label='Add a Ticker or Tickers',
																options=scope.config['dropdowns']['tickers'], 
																default=previous_selection, 
																help='Select a ticker, or multiple tickers from the dropdown. Start typing to jump within list',
																key=widget_key
																)

	# scope.pages['screener']['selectors']['tickers'] = new_selection

