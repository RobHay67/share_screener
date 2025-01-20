import streamlit as st

from app.views.header.d_ticker_files.progress_bar_load_tickers import load_tickers_progress_bar	
from app.views.header.d_ticker_files.progress_bar_add_cols import add_extra_cols_progress_bar
from app.scope.model.worklists.long_desc import refresh_worklist_long_description


# Function to show status of ticker data
# - progress bar while loading files (as can be time consuming)
# - status once all files are loaded
# - status if there is nothing too load.

# Add and Replace extra columns for the Page Dataframes
# - refresh the page df (completely)
# - Refresh specific df columns (activate or change col_adders settings)
# - utilised the scope.tickers object to track what needs to be done


def show_ticker_load_and_col_adding(scope):
	page = scope.config['display']
	col1,col2 = st.columns([6.0, 6.0])  #12.0
	if page in ['chart', 'intraday', 'volume', 'screener',]:
		with col1:
			# loads ticker data as well
			load_tickers_progress_bar(scope, ) 
			refresh_worklist_long_description(scope)
		with col2:
			# for volume we dont need to do this step
			if page != 'volume':
				add_extra_cols_progress_bar(scope, page)      # will add/update the columns as well!





