import streamlit as st

from tickers.latest_price import latest_ticker_price



def selected_ticker_name_layer(scope):

	page = scope.display_page

	if page != 'screener':
		# non screener page - there will  be 1 ticker in worklist
		if len(scope.pages[page]['worklist'])==1:
			# we have a ticker to work with
		
			ticker = scope.pages[page]['worklist'][0]
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
			


