import streamlit as st
import pandas as pd


def render_worklist(scope):
	# Render a button and/or an expander object that shows the 
	# current state of the tickers for the current app worklist

	app = scope.apps['display_app']
	ticker_list = scope.apps[app]['worklist']
	no_of_tickers = len(ticker_list)
	widget_key = 'widget_' + app + '_worklist'
	worklist = []

	if no_of_tickers == 0:
		widget_label = 'Empty Worklist'
		
	if no_of_tickers == 1:
		widget_label = '1 Ticker'
		worklist.append(ticker_load_status(scope, ticker_list[0]))

	if no_of_tickers > 1:
		widget_label = 'Work List (' + str(no_of_tickers) + ')'
		for ticker in ticker_list:
			worklist.append(ticker_load_status(scope, ticker))
		
	selectbox = st.selectbox(
			label		=widget_label, 
			options		=worklist,
			key			=widget_key,
			)
	
	return selectbox


def render_errors(scope):
	# Render errors only 

	app = scope.apps['display_app']
	widget_key = 'widget_' + app + '_load_errors'
	error_list = []

	# create a list of errors relevant for this app
	for ticker in scope.missing_tickers['list']:
		if ticker in scope.apps[app]['worklist']:
			error_list.append(ticker)
	no_of_errors = len(error_list)

	if no_of_errors == 0:widget_label = '0 Errors'
	if no_of_errors == 1:widget_label = '1 Error'
	if no_of_errors  > 1:widget_label = '(' + str(no_of_errors) + ') Errors'

	selectbox = st.selectbox(
			label		=widget_label, 
			options		=error_list,
			key			=widget_key,
			)

	return selectbox



def ticker_load_status(scope, ticker):
	# Cloud Errors over-ride local error. If we 
	# cant download from cloud, there probably wont be
	# a local file anyway.
	ticker_status = ticker + ' > '

	if ticker in scope.missing_tickers['cloud']:
		ticker_status =  ticker_status + scope.missing_tickers['errors'][ticker]['yf']
	elif ticker in scope.missing_tickers['local']:
		ticker_status = ticker_status + scope.missing_tickers['errors'][ticker]['load']
	else:
		ticker_status = ticker_status + 'ok'
	
	return ticker_status





# ===================================
# Old code that build an amazing list of buttons

# def render_worklist(scope):
# 	# Render a button and/or an expander object that shows the 
# 	# current state of the tickers for the current app worklist

# 	app = scope.apps['display_app']
# 	ticker_list = scope.apps[app]['worklist']
# 	no_of_tickers = len(ticker_list)

# 	if no_of_tickers == 1:
# 		render_button_for_ticker(scope, ticker_list[0])

# 	if no_of_tickers > 1:
# 		button_description = 'Work List (' + str(no_of_tickers) + ')'
# 		my_worklist = st.expander(label=button_description, expanded=False )
		
# 		with my_worklist:
# 			st.write('Load and Download Errors')
# 			for ticker in ticker_list:
# 				render_button_for_ticker(scope, ticker)




# def render_button_for_ticker(scope, ticker):
# 	# Cloud Errors over-ride local error. If we 
# 	# cant download from cloud, there probably wont be
# 	# a local file anyway.

# 	if ticker in scope.missing_tickers['cloud']:
# 		download_error = ticker + '  ---- ' + scope.missing_tickers['errors'][ticker]['yf']
# 		st.error(download_error)
# 	elif ticker in scope.missing_tickers['local']:
# 		load_error = ticker + '  ---- ' + scope.missing_tickers['errors'][ticker]['load']
# 		st.warning(load_error)
# 	else:
# 		st.success(ticker)


