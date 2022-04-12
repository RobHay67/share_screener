
# import streamlit as st


# Set the Refresh Status for objects within the pages - helps to control whats needs to be updated, and what does not

# add ohlcv data - all pages								ohlc_data
# add chart data - all pages except the screener page		page_data	singles_pages
# add metric data - only the Screener page					page_data	screener_page




# def set_page_renew_status(scope, ticker_data=False, charts=None, tests=None, tickers='all', status=True, caller='unknown' ):
def set_page_renew_status(scope, ticker_data=False, expanders=None, tickers='all', status=True, caller='unknown' ):
	# status = Usually True, but when downloading we sometime need to turn the refresh off if the download fails

	width=70
	print('='*width)
	print('\033[95mRunning < set_page_renew_status > function\033[0m')
	print('\033[96mcaller = ' + caller + '\033[0m')
	print('-'*width)
	print('')
	print ('expanders = ', expanders)
	

	for page in scope.pages['page_list']:
		# Establish list of tickers for this page (stremalines the whole function)
		ohlcv_tickers, expander_tickers = list_of_tickers_for_page(scope, page, tickers)
		config_group = 'tests' if page == 'screener' else 'charts'

		if ticker_data:
			for ticker in ohlcv_tickers: 
				scope.pages[page]['renew']['ticker_data'][ticker] = status

		if expanders != None:
			for ticker in expander_tickers: 
				# take a copy of our default config for this type of expander
				expander_template = scope.pages['templates'][config_group].copy()				
				if expanders=='all':
					# Every EXPANDER requires a data refresh																		
					scope.pages[page]['renew']['expanders'][ticker] = expander_template
				else:
					# A single EXPANDER requires a data refresh									
					scope.pages[page]['renew']['expanders'][ticker][expanders] = True



	print('\033[0m')
	# print('='*width)


def list_of_tickers_for_page(scope, page, tickers):
	if tickers == 'all':
		ohlcv_tickers = list(scope.pages[page]['renew']['ticker_data'].keys())
		expander_tickers = list(scope.pages[page]['renew']['expanders'].keys())
	else:
		# A single ticker has been provided so return this single ticker in a list
		ohlcv_tickers = [tickers]
		expander_tickers = [tickers]

	return ohlcv_tickers, expander_tickers






# set_page_renew_status(scope, ticker_data=True, charts='all', tests='all' )
# def redo_ohlc_data_all_pages_all_tickers(scope:dict):
# 	# This executes when the user has changed the number of analysis rows
# 	#  - ie from 1000 to say 3000 - for simplicity we just reset everything

# 	for page in st.session_state.pages['page_list']:
# 		for ticker in st.session_state.pages[page]['renew']['ticker_data'].keys():
# 			st.session_state.pages[page]['renew']['ticker_data'][ticker] = True

# 		if page == 'screener':																	# Screener Page Only
# 			metrics_template = st.session_state.pages_template_add_metric_data.copy()			# take a copy of our template of metric active status
# 			for ticker in st.session_state.pages[page]['renew']['tests'].keys():				# iterate through tickers
# 				st.session_state.pages[page]['renew']['tests'][ticker] = metrics_template		# set the current metric active status for ticker
# 		if page != 'screener':																	# for non screen pages (charts only)
# 			chart_template = st.session_state.pages_template_add_chart_data.copy()				# take a copy of our default dictionary
# 			for ticker in st.session_state.pages[page]['renew']['expanders'].keys():				# iterate through tickers
# 				st.session_state.pages[page]['renew']['expanders'][ticker]  = chart_template		# set the current metric active status for this ticker


# set_page_renew_status(scope, ticker_data=True, charts=True, tests=True, tickers='CBA', status=TRUE or FALSE )
# def redo_ohlc_data_all_pages_one_ticker(scope, ticker, refresh_status):							# refresh_status = True or False
# 	# Execute when either of the following occurs
# 	# 	a) Load of Ticker Data
# 	# 	b) Download of New Ticker Data
# 		# note: refresh_status allows for True or False. This is handy when say the load or download fails
# 		# problem = we dont know if this ticker exists or not yet


# 	for page in scope.pages['page_list']:										# for every page
# 		scope.pages[page]['renew']['ticker_data'][ticker] = refresh_status			# set the appropriate status for this ticker

# 		if page == 'screener':															# Screener Page Only
# 			metrics_template = scope.pages['templates']['test'].copy()		# take a copy of our default dictionary
# 			scope.pages[page]['renew']['tests'][ticker] = metrics_template				# set the current metric active status for this ticker
# 		if page != 'screener':															# for non screener pages (charts only)
# 			chart_template = scope.pages['templates']['expanders'].copy()			# take a copy of our default dictionary
# 			scope.pages[page]['renew']['expanders'][ticker]  = chart_template				# set the current metric active status for this ticker

# set_page_renew_status(scope, charts='chart name')
# def redo_page_data_singles_pages_all_tickers(scope, chart):
# 	# One of the Chart Metrics has changed i.e. made active or changed a value from say 21 to 34
# 	for page in scope.pages['page_list']:
# 		if page != 'screener':													# all chart relevant pages
# 			for ticker in scope.pages[page]['renew']['expanders'].keys():			# iterate through each ticker
# 				scope.pages[page]['renew']['expanders'][ticker][chart] = True		# Set Refresh = True



# set_page_renew_status(scope, test='test name')
# def redo_page_data_screener_page_all_tickers(scope, test):
# 	# One of the Screener Metrics has changed i.e. made active or changed a value from say 21 to 34
# 	for page in scope.pages['page_list']:
# 		if page == 'screener':													# Only the Screener Page
# 			for ticker in scope.pages[page]['renew']['tests'].keys():			# iterate through each ticker
# 				scope.pages[page]['renew']['tests'][ticker][test] = True		# Set Refresh = True

















# only uised by the above function - see if we can combine this then
# def redo_page_data_all_pages_all_tickers():
# 	# This executes when the user has changed the number of analysis rows
# 	#  - ie from 1000 to say 3000 - for simplicity we just reset everything

# 	# for page in st.session_state.pages['page_list']:														# iterate through every page
# 		if page == 'screener':																		# Screener Page Only
# 			metrics_template = st.session_state.pages_template_add_metric_data.copy()			# take a copy of our template of metric active status
# 			for ticker in st.session_state.pages[page]['renew']['tests'].keys():					# iterate through tickers
# 				st.session_state.pages[page]['renew']['tests'][ticker] = metrics_template		# set the current metric active status for ticker
# 		if page != 'screener':																		# for non screen pages (charts only)
# 			chart_template = st.session_state.pages_template_add_chart_data.copy()							# take a copy of our default dictionary
# 			for ticker in st.session_state.pages[page]['renew']['expanders'].keys():					# iterate through tickers
# 				st.session_state.pages[page]['renew']['expanders'][ticker]  = chart_template			# set the current metric active status for this ticker
				

# only uised by the above function - see if we can combine this then
# def redo_page_data_all_pages_one_ticker(scope, ticker, refresh_status):
# 	# Execute when either of the following occurs
# 	# 	a) Load of Ticker Data
# 	# 	b) Download of New Ticker Data
# 	# note: refresh_status allows for True or False. This is handy when say the load or download fails
# 	# problem = we dont know if this ticker exists or not yet

# 	for page in scope.pages['page_list']:														# iterate through every page
# 		if page == 'screener':															# Screener Page Only
# 			metrics_template = scope.pages['templates']['test'].copy()		# take a copy of our default dictionary
# 			scope.pages[page]['renew']['tests'][ticker] = metrics_template				# set the current metric active status for this ticker
# 		if page != 'screener':															# for non screener pages (charts only)
# 			chart_template = scope.pages['templates']['expanders'].copy()			# take a copy of our default dictionary
# 			scope.pages[page]['renew']['expanders'][ticker]  = chart_template				# set the current metric active status for this ticker



		# if expanders != None:
		# 	if page != 'screener':
		# 		for ticker in expander_tickers: 
		# 			# take a copy of our default dictionary
		# 			chart_template = scope.pages['templates'][config_group].copy()
		# 			print(chart_template)
		# 			if expanders=='all':
		# 				# Every CHART requires a data refresh												
		# 				scope.pages[page]['renew']['expanders'][ticker] = chart_template
		# 			else:
		# 				# A single CHART requires a data refresh													
		# 				scope.pages[page]['renew']['expanders'][ticker][expanders] = True