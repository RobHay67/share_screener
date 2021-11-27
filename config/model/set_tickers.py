import streamlit as st



def select_tickers(scope):

	previous_selection = scope.pages['multi']['tickers']

	new_selection = st.multiselect(
									label='Add a Ticker or Tickers',
									options=scope.dropdown_tickers, 
									default=previous_selection, 
									help='Select a ticker, or multiple tickers from the dropdown. Start typing to jump within list',
									key='3'
									)

	scope.pages['multi']['tickers'] = new_selection