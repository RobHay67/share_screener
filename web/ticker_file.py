

import streamlit as st



def render_ticker_file(scope, ticker): # WIP
	st.markdown('##### Loaded and / or Downloaded share data.')

	# ticker = scope.ticker['research']

	if ticker in list(scope.share_data_files.keys()):
		ticker_data_file = scope.share_data_files[ticker]
		ticker_data_file.sort_values(by=['date'], inplace=True, ascending=False)
		my_expander = st.expander(label=ticker)
		my_expander.dataframe(ticker_data_file, 2000, 2000)	
	else:
		st.error('Load / Download some ticker data')




