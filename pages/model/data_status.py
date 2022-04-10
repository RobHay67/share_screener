
# import streamlit as st


# Set the Refresh Status for objects within the pages - helps to control whats needs to be updated, and what does not

# add ohlcv data - all pages								ohlc_data
# add chart data - all pages except the screener page		page_data	singles_pages
# add metric data - only the Screener page					page_data	screener_page


def set_page_data_status(scope, shares=False, charts=None, tests=None, tickers='all', status=True, caller='unknown' ):
	# status = Usually True, but when downloading we sometime need to turn the refresh off if the download fails

	width=70
	print('='*width)
	print('\033[95mRunning < set_page_data_status > function\033[0m')
	print('\033[96mcaller = ' + caller + '\033[0m')
	print('-'*width)
	print('')

	for page in scope.pages['page_list']:
		print('-'*width)
		print('page = ', page)
		print('-'*width)
		# Establish list of tickers for this page (stremalines the whole function)
		ohlcv_tickers, tests_tickers, chart_tickers = list_of_ticker_for_page(scope, page, tickers)

		if shares:
			print('-'*width)
			print('add_ohlcv_data', page)
			print('-'*width)
			for ticker in ohlcv_tickers: 
				if ticker in scope.pages[page]['add_ohlcv_data'].keys():
					print(ticker, ' before add_ohlcv_data = ', scope.pages[page]['add_ohlcv_data'][ticker])
				else:
					print(ticker, ' before add_ohlcv_data = does not exist in ')
				scope.pages[page]['add_ohlcv_data'][ticker] = status
				
				print(ticker, ' after  > add_ohlcv_data =', scope.pages[page]['add_ohlcv_data'][ticker] )
			print('-'*width)

		if tests != None:
			if page == 'screener':
				for ticker in tests_tickers: 
					metrics_template = scope.pages['templates']['add_metric_data'].copy()				# take a copy of our default dictionary
					if tests=='all':																	# Every Chart needs to be updated
						scope.pages[page]['add_metric_data'][ticker] = chart_template
					else:																				# Updating a single chart only
						scope.pages[page]['add_metric_data'][ticker][tests] = True						# Set Refresh = True for this test

		if charts != None:
			if page != 'screener':
				for ticker in chart_tickers: 
					chart_template = scope.pages['templates']['add_chart_data'].copy()					# take a copy of our default dictionary
					if charts=='all':																	# Every Chart needs to be updated
						scope.pages[page]['add_chart_data'][ticker] = chart_template
					else:																				# Updating a single chart only
						scope.pages[page]['add_chart_data'][ticker][charts] = True						# Set Refresh = True for this char

	print('='*width)


def list_of_ticker_for_page(scope, page, tickers):
	if tickers == 'all':
		ohlcv_tickers = list(scope.pages[page]['add_ohlcv_data'].keys())
		if page == 'screener': 
			tests_tickers = list(scope.pages[page]['add_metric_data'].keys())
			chart_tickers = None
		else: 
			chart_tickers = list(scope.pages[page]['add_chart_data'].keys())
			tests_tickers = None
	else:
		# A single ticker has been provided so return this single ticker in a list
		ohlcv_tickers = [tickers]
		tests_tickers = [tickers]
		chart_tickers = [tickers]

	return ohlcv_tickers, tests_tickers, chart_tickers






# set_page_data_status(scope, shares=True, charts='all', tests='all' )
# def redo_ohlc_data_all_pages_all_tickers(scope:dict):
# 	# This executes when the user has changed the number of analysis rows
# 	#  - ie from 1000 to say 3000 - for simplicity we just reset everything

# 	for page in st.session_state.pages['page_list']:
# 		for ticker in st.session_state.pages[page]['add_ohlcv_data'].keys():
# 			st.session_state.pages[page]['add_ohlcv_data'][ticker] = True

# 		if page == 'screener':																	# Screener Page Only
# 			metrics_template = st.session_state.pages_template_add_metric_data.copy()			# take a copy of our template of metric active status
# 			for ticker in st.session_state.pages[page]['add_metric_data'].keys():				# iterate through tickers
# 				st.session_state.pages[page]['add_metric_data'][ticker] = metrics_template		# set the current metric active status for ticker
# 		if page != 'screener':																	# for non screen pages (charts only)
# 			chart_template = st.session_state.pages_template_add_chart_data.copy()				# take a copy of our default dictionary
# 			for ticker in st.session_state.pages[page]['add_chart_data'].keys():				# iterate through tickers
# 				st.session_state.pages[page]['add_chart_data'][ticker]  = chart_template		# set the current metric active status for this ticker


# set_page_data_status(scope, shares=True, charts=True, tests=True, tickers='CBA', status=TRUE or FALSE )
# def redo_ohlc_data_all_pages_one_ticker(scope, ticker, refresh_status):							# refresh_status = True or False
# 	# Execute when either of the following occurs
# 	# 	a) Load of Ticker Data
# 	# 	b) Download of New Ticker Data
# 		# note: refresh_status allows for True or False. This is handy when say the load or download fails
# 		# problem = we dont know if this ticker exists or not yet


# 	for page in scope.pages['page_list']:										# for every page
# 		scope.pages[page]['add_ohlcv_data'][ticker] = refresh_status			# set the appropriate status for this ticker

# 		if page == 'screener':															# Screener Page Only
# 			metrics_template = scope.pages['templates']['add_metric_data'].copy()		# take a copy of our default dictionary
# 			scope.pages[page]['add_metric_data'][ticker] = metrics_template				# set the current metric active status for this ticker
# 		if page != 'screener':															# for non screener pages (charts only)
# 			chart_template = scope.pages['templates']['add_chart_data'].copy()			# take a copy of our default dictionary
# 			scope.pages[page]['add_chart_data'][ticker]  = chart_template				# set the current metric active status for this ticker

# set_page_data_status(scope, charts='chart name')
# def redo_page_data_singles_pages_all_tickers(scope, chart):
# 	# One of the Chart Metrics has changed i.e. made active or changed a value from say 21 to 34
# 	for page in scope.pages['page_list']:
# 		if page != 'screener':													# all chart relevant pages
# 			for ticker in scope.pages[page]['add_chart_data'].keys():			# iterate through each ticker
# 				scope.pages[page]['add_chart_data'][ticker][chart] = True		# Set Refresh = True



# set_page_data_status(scope, test='test name')
# def redo_page_data_screener_page_all_tickers(scope, test):
# 	# One of the Screener Metrics has changed i.e. made active or changed a value from say 21 to 34
# 	for page in scope.pages['page_list']:
# 		if page == 'screener':													# Only the Screener Page
# 			for ticker in scope.pages[page]['add_metric_data'].keys():			# iterate through each ticker
# 				scope.pages[page]['add_metric_data'][ticker][test] = True		# Set Refresh = True

















# only uised by the above function - see if we can combine this then
# def redo_page_data_all_pages_all_tickers():
# 	# This executes when the user has changed the number of analysis rows
# 	#  - ie from 1000 to say 3000 - for simplicity we just reset everything

# 	# for page in st.session_state.pages['page_list']:														# iterate through every page
# 		if page == 'screener':																		# Screener Page Only
# 			metrics_template = st.session_state.pages_template_add_metric_data.copy()			# take a copy of our template of metric active status
# 			for ticker in st.session_state.pages[page]['add_metric_data'].keys():					# iterate through tickers
# 				st.session_state.pages[page]['add_metric_data'][ticker] = metrics_template		# set the current metric active status for ticker
# 		if page != 'screener':																		# for non screen pages (charts only)
# 			chart_template = st.session_state.pages_template_add_chart_data.copy()							# take a copy of our default dictionary
# 			for ticker in st.session_state.pages[page]['add_chart_data'].keys():					# iterate through tickers
# 				st.session_state.pages[page]['add_chart_data'][ticker]  = chart_template			# set the current metric active status for this ticker
				

# only uised by the above function - see if we can combine this then
# def redo_page_data_all_pages_one_ticker(scope, ticker, refresh_status):
# 	# Execute when either of the following occurs
# 	# 	a) Load of Ticker Data
# 	# 	b) Download of New Ticker Data
# 	# note: refresh_status allows for True or False. This is handy when say the load or download fails
# 	# problem = we dont know if this ticker exists or not yet

# 	for page in scope.pages['page_list']:														# iterate through every page
# 		if page == 'screener':															# Screener Page Only
# 			metrics_template = scope.pages['templates']['add_metric_data'].copy()		# take a copy of our default dictionary
# 			scope.pages[page]['add_metric_data'][ticker] = metrics_template				# set the current metric active status for this ticker
# 		if page != 'screener':															# for non screener pages (charts only)
# 			chart_template = scope.pages['templates']['add_chart_data'].copy()			# take a copy of our default dictionary
# 			scope.pages[page]['add_chart_data'][ticker]  = chart_template				# set the current metric active status for this ticker
