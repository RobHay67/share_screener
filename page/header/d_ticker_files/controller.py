import logging
import streamlit as st

from page.header.d_ticker_files.progress_bar_load_tickers import show_progress_bar_for_loading_tickers	
from page.header.d_ticker_files.progress_bar_add_cols import show_progress_bar_for_adding_extra_columns
from page.scope.model.worklists.long_desc import build_worklist_with_long_description


# Function to show status of ticker data
# - progress bar while loading files (as can be time consuming)
# - status once all files are loaded
# - status if there is nothing too load.

# Add and Replace extra columns for the Page Dataframes
# - refresh the page df (completely)
# - Refresh specific df columns (activate or change col_adders settings)
# - utilised the scope.tickers object to track what needs to be done


def show_progress_load_and_add_cols(scope):
	logging.debug("show_progress_load_and_add_cols")
	page = scope.display['page']
	col1,col2 = st.columns([6.0, 6.0])  #12.0
	if page in ['chart', 'intraday', 'volume', 'screener',]:
		with col1:
			# loads ticker data as well
			show_progress_bar_for_loading_tickers(scope) 
			build_worklist_with_long_description(scope)
		with col2:
			# for the volume pagewe dont need to do this step
			if page != 'volume':
				show_progress_bar_for_adding_extra_columns(scope, page)      # will add/update the columns as well!





