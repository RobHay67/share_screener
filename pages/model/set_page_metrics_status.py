import streamlit as st



def set_add_metrics_all():
	# This executes when the user has changed the number of analysis rows
	#  - ie from 1000 to say 3000 - for simplicity we just reset everything

	for page in st.session_state.pages['page_list']:														# iterate through every page
		if page == 'screener':																		# Screener Page Only
			metrics_template = st.session_state.pages_template_add_metric_data.copy()			# take a copy of our template of metric active status
			for ticker in st.session_state.pages[page]['add_metric_data'].keys():					# iterate through tickers
				st.session_state.pages[page]['add_metric_data'][ticker] = metrics_template		# set the current metric active status for ticker
		if page != 'screener':																		# for non screen pages (charts only)
			chart_template = st.session_state.pages_template_add_chart_data.copy()							# take a copy of our default dictionary
			for ticker in st.session_state.pages[page]['add_chart_data'].keys():					# iterate through tickers
				st.session_state.pages[page]['add_chart_data'][ticker]  = chart_template			# set the current metric active status for this ticker
				

def set_add_metrics_ticker(scope, ticker, refresh_status):
	# Execute when either of the following occurs
	# 	a) Load of Ticker Data
	# 	b) Download of New Ticker Data
	# note: refresh_status allows for True or False. This is handy when say the load or download fails

	# problem = we dont know if this ticker exists or not yet

	for page in scope.pages['page_list']:														# iterate through every page
		if page == 'screener':															# Screener Page Only
			metrics_template = scope.pages['templates']['add_metric_data'].copy()		# take a copy of our default dictionary
			scope.pages[page]['add_metric_data'][ticker] = metrics_template				# set the current metric active status for this ticker
		if page != 'screener':															# for non screener pages (charts only)
			chart_template = scope.pages['templates']['add_chart_data'].copy()			# take a copy of our default dictionary
			scope.pages[page]['add_chart_data'][ticker]  = chart_template				# set the current metric active status for this ticker
				


def set_refresh_chart_data(scope, chart):
	# One of the Chart Metrics has changed i.e. made active or changed a value from say 21 to 34
	for page in scope.pages['page_list']:
		if page != 'screener':													# all chart relevant pages
			for ticker in scope.pages[page]['add_chart_data'].keys():			# iterate through each ticker
				scope.pages[page]['add_chart_data'][ticker][chart] = True		# Set Refresh = True
				



def set_refresh_metric_data(scope, test):
	# One of the Screener Metrics has changed i.e. made active or changed a value from say 21 to 34
	for page in scope.pages['page_list']:
		if page == 'screener':													# all chart relevant pages
			for ticker in scope.pages[page]['add_metric_data'].keys():			# iterate through each ticker
				scope.pages[page]['add_metric_data'][ticker][test] = True		# Set Refresh = True


