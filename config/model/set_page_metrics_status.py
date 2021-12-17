# scope.pages[screener]['add_metric_data'] 	= { CBA:{ metric_1:True, metric_2:False, metric_3:True}}
# scope.pages[screener]['add_chart_data'] 	= { CBA:{ metric_1:False,metric_2:False, metric_3:False}}
# scope.pages[single]  ['add_metric_data'] 	= { NAB:{ metric_1:True, metric_2:False, metric_3:True}}
# scope.pages[single]  ['add_chart_data'] 	= { NAB:{ metric_1:True, metric_2:False, metric_3:True}}



import streamlit as st




def set_add_metrics_all():
	# This executes when the user has changed the number of analysis rows
	#  - ie from 1000 to say 3000 - for simplicity we just reset everything

	print(st.session_state.page_metrics_chart)

	for page in st.session_state.pages.keys():													# iterate through every page
		if page == 'screener':																	# Screener Page Only
			metrics_dictionary = st.session_state.page_metrics_screener.copy()					# take a copy of our default dictionary
			for ticker in st.session_state.pages[page]['add_metric_data'].keys():				# iterate through tickers
				st.session_state.pages[page]['add_metric_data'][ticker] = metrics_dictionary	# set the current metric active status for ticker
		if page != 'screener':																	# for non screen pages (charts only)
			chart_dictionary = st.session_state.page_metrics_chart.copy()						# take a copy of our default dictionary
			for ticker in st.session_state.pages[page]['add_chart_data'].keys():				# iterate through tickers
				st.session_state.pages[page]['add_chart_data'][ticker]  = chart_dictionary		# set the current metric active status for this ticker
				

def set_add_metrics_ticker(scope, ticker, refresh_status):
	# Execute when either of the following occurs
	# 	a) Load of Ticker Data
	# 	b) Download of New Ticker Data
	# note: refresh_status allows for True or False. This is handy when say the load or download fails

	# problem = we dont know if this ticker exists or not yet

	for page in scope.pages.keys():												# iterate through every page
		if page == 'screener':													# Screener Page Only
			metrics_dictionary = scope.page_metrics_screener.copy()				# take a copy of our default dictionary
			scope.pages[page]['add_metric_data'][ticker] = metrics_dictionary	# set the current metric active status for this ticker
		if page != 'screener':													# for non screen pages (charts only)
			chart_dictionary = scope.page_metrics_chart.copy()					# take a copy of our default dictionary
			scope.pages[page]['add_chart_data'][ticker]  = chart_dictionary		# set the current metric active status for this ticker
				



