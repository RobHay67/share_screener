import logging
import streamlit as st

from tickers.helpers.latest_price import latest_ticker_price



def add_ticker_name(scope):
	logging.info("add_ticker_name")
	page = scope.display['page']

	if page != 'screener':
		# non screener page - there will  be 1 ticker in worklist
		if len(scope.page[page]['list_selected_tickers'])==1:
			# we have a ticker to work with
		
			ticker = scope.page[page]['list_selected_tickers'][0]
			ticker_name = scope.config['ticker_search'][ticker].title()
			ticker_latest_price_df = latest_ticker_price(scope, ticker)
				
			col1,col2,col3 = st.columns([1.0,6.0, 5.0])  #12

			with col1:
				st.subheader(":blue["+ticker+"]")
			with col2:
				st.write('')
				st.write(":blue["+ticker_name+"]")
			with col3:
				st.dataframe(ticker_latest_price_df, use_container_width=True)
			


