import logging
import streamlit as st

from page.header.c_ticker_files.progress_bar_load_tickers import progress_bar_load_tickers	
from page.header.c_ticker_files.progress_bar_add_cols import progress_bar_add_columns



# Function to show status of ticker data
# - progress bar while loading files (as can be time consuming)
# - status once all files are loaded
# - status if there is nothing too load.

# Add and Replace extra columns for the Page Dataframes
# - refresh the page df (completely)
# - Refresh specific df columns (activate or change col_adders settings)
# - utilised the scope.tickers object to track what needs to be done


def router_progress_bars(scope):
	logging.info("router_progress_bars")
	page = scope.display['page']
	col1,col2 = st.columns([6.0, 6.0])  #12.0
	if page in ['chart', 'intraday', 'volume', 'screener',]:
		with col1:
			# loads ticker data as well
			progress_bar_load_tickers(scope) 
		with col2:
			# for the volume page we dont need to do this step
			if page != 'volume':
				# will add/update the columns as well!
				progress_bar_add_columns(scope, page)      





