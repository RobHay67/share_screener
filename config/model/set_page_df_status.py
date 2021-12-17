import streamlit as st


# scope.pages[page]['add_ohlcv_data'] 		= { CBA:True, NAB:False }

# scope.pages[screener]['add_metric_data'] 	= { CBA:{ metric_1:True, metric_2:False, metric_3:True}}
# scope.pages[screener]['add_chart_data'] 	= { CBA:{ metric_1:False,metric_2:False, metric_3:False}}
# scope.pages[single]  ['add_metric_data'] 	= { NAB:{ metric_1:True, metric_2:False, metric_3:True}}
# scope.pages[single]  ['add_chart_data'] 	= { NAB:{ metric_1:True, metric_2:False, metric_3:True}}

# so then we can iterate through every page and then every ticker and then every test and tag the relevant T/F
# then the dfs builder will know what it needs to do and can skip all the falses 

from config.model.set_page_metrics_status import set_add_metrics_all
from config.model.set_page_metrics_status import set_add_metrics_ticker

def set_refresh_page_df_all():
	print( 'running set_refresh_page_df_all')
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









def set_refresh_chart_dfs_for_non_screener_pages(scope):
	# One of the Chart Metrics has changed
	for page in scope.pages.keys():
		if page != 'screener':
			for ticker in scope.pages[page]['add_ohlcv_data'].keys():
				scope.pages[page]['add_ohlcv_data'][ticker] = True



def set_refresh_screener_dfs_for_screener_page(scope):
	# One of the Screener Metrics has changed 		TODO - not yet using this one
	for ticker in scope.pages['screener']['add_ohlcv_data'].keys():
		scope.pages['screener']['add_ohlcv_data'][ticker] = True

