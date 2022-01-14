import streamlit as st






# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Single Ticker Page Helpers
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

def select_a_ticker(scope, page):
	
	# Previous Selection
	previous_ticker_for_page = scope.pages[page]['ticker_list'][0]

	# render the selector defalted to the stored ticker for this page
	selected_ticker = st.selectbox ( 
									label='Select a Ticker', 
									options=scope.dropdown_ticker,
									index=scope.dropdown_ticker.index(previous_ticker_for_page), 
									help='Choose a ticker for analysis. Start typing to jump within list',
									key=page,
									) 
	# Store the selection so we can easily swap pages
	scope.pages[page]['ticker_list'] = [selected_ticker]