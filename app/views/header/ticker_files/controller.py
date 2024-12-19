import streamlit as st


from app.views.header.format import md_for_header
from app.views.header.ticker_files.progress_bar import progress_bar_loading_tickers	
from app.views.header.ticker_files.button import download_button
from y_finance.controller import download_ticker_data



# Function to show status of data
# - progress bar while loading files (as can be time consuming)
# - status once all files are loaded
# - status if there is nothing too load.
# - button to press to download more data




def load_ticker_files(scope):

	page = scope.pages['display']

	if page in ['chart', 'intraday', 'volume', 'screener',  ]:
		col1,col2,col3 = st.columns([1.5, 9.0, 1.5])  #12.0
		with col1:
			md_for_header('Ticker Files (loaded)')
		with col2:
			progress_bar_loading_tickers(scope, ) # loads ticker data as well
		with col3:
			requested_to_download_ticker_data = download_button(scope)

		if requested_to_download_ticker_data:
			download_ticker_data(scope)
