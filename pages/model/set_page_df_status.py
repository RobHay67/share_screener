import streamlit as st



from pages.model.set_page_metrics_status import set_add_metrics_all, set_add_metrics_ticker


def set_refresh_page_df_all():
	# This executes when the user has changed the number of analysis rows
	#  - ie from 1000 to say 3000 - for simplicity we just reset everything

	for page in st.session_state.pages:
		for ticker in st.session_state.pages[page]['add_ohlcv_data'].keys():
			st.session_state.pages[page]['add_ohlcv_data'][ticker] = True
	
	set_add_metrics_all()					# ensure all of the metrics are recalculated



def set_refresh_page_df_ticker(scope, ticker, refresh_status):
	# Execute when either of the following occurs
	# 	a) Load of Ticker Data
	# 	b) Download of New Ticker Data
		# note: refresh_status allows for True or False. This is handy when say the load or download fails

	for page in scope.pages.keys():												# for every page
		scope.pages[page]['add_ohlcv_data'][ticker] = refresh_status			# set the appropriate status for this ticker
	
	set_add_metrics_ticker(scope, ticker, refresh_status)						# ensure all of the metrics are recalculated







