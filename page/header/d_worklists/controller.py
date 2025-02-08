import logging
import streamlit as st
from page.header.d_worklists.dropdown_worklist import dropdown_worklist
from page.header.d_worklists.dropdown_errors import dropdown_load_and_download_ticker_errors


def worklist_selectors(scope):
	logging.info("worklist_selectors")
	page = scope.display['page']

	if scope.page[page]['replace_worklist']:
		worklist_for_page = []

		for ticker in scope.page[page]['list_loaded_tickers']:
			ticker_name = scope.config['ticker_search'][ticker]
			ticker_length = len(ticker)
			padding = 10 - ticker_length
			pad_string = '-'*padding
			ticker_status = ticker + pad_string

			if ticker in scope.ticker_schema['missing']['cloud']:
				ticker_status =  ticker_status + scope.ticker_schema['missing']['errors'][ticker]['yf']
			elif ticker in scope.ticker_schema['missing']['local']:
				ticker_status = ticker_status + scope.ticker_schema['missing']['errors'][ticker]['load']
			else:
				if ticker in list(scope.tickers.keys()): 
					ticker_df = scope.tickers[ticker]['df']
					no_of_rows = ' (' + str(len(ticker_df)) +') '
					# Date Range
					min_date = ticker_df['date'].min()
					max_date = ticker_df['date'].max()
					min_date = str(min_date.strftime("%d-%b-%Y"))
					max_date = str(max_date.strftime("%d-%b-%Y"))
					ticker_status = ticker_status + min_date + ' < > ' + max_date + no_of_rows + ' rows ---' + ' ' + ticker_name
				else:
					ticker_status = ticker_status + 'not loaded'
			worklist_for_page.append(ticker_status)
		worklist_for_page.insert(0, 'Show/Hide Data')
		scope.page[page]['list_page_worklist'] = worklist_for_page


	if page in ['screener', 'chart', 'intraday', 'volume', 'research']:
		col1,col2 = st.columns([7.0, 3.0])  #12
		with col1:dropdown_worklist(scope)
		with col2:dropdown_load_and_download_ticker_errors(scope)
	




