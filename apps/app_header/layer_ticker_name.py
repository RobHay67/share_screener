import streamlit as st

from tickers.latest_price import latest_ticker_price



def selected_ticker_name_layer(scope):

	app = scope.apps['display_app']

	if app != 'screener':
		# non screener app - there will  be 1 ticker in worklist
		if len(scope.apps[app]['worklist'])==1:
			# we have a ticker to work with
		
			ticker = scope.apps[app]['worklist'][0]
			ticker_name = scope.config['ticker_search'][ticker]
			ticker_latest_price_df = latest_ticker_price(scope, ticker)
				
			col1,col2 = st.columns([8.0, 4.0])  #12

			with col1:st.subheader(ticker_name)
			with col2:st.dataframe(ticker_latest_price_df, use_container_width=True)
			


