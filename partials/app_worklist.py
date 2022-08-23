import streamlit as st
import pandas as pd

def render_worklist(scope):
	# Render an button or an expander object that shows the 
	# current state of the tickers for the current app worklist

	app = scope.apps['display_app']
	ticker_list = scope.apps[app]['worklist']
	no_of_tickers = len(ticker_list)

	if no_of_tickers == 1:
		ticker = ticker_list[0]
		render_button_for_ticker(scope, ticker)

	if no_of_tickers > 1:
		button_description = 'Work List (' + str(no_of_tickers) + ')'
		my_worklist = st.expander(label=button_description, expanded=False )
		
		with my_worklist:
			st.write('Load and Download Errors')
			for ticker in ticker_list:
				render_button_for_ticker(scope, ticker)


def render_errors(scope):

	app = scope.apps['display_app']
	ticker_list = scope.missing_tickers['list']
	no_of_tickers = len(ticker_list)
	
	if no_of_tickers == 0:
		st.success('no errors')
	else:
		button_description = 'Errors (' + str(no_of_tickers) + ')'
		my_errors = st.expander(label=button_description, expanded=False )
		
		with my_errors:
			st.write('List of Errors (only)')
			for ticker in ticker_list:
				render_button_for_ticker(scope, ticker)



def render_button_for_ticker(scope, ticker):
	# Cloud Errors over-ride local error. If we 
	# cant download from cloud, there probably wont be
	# a local file anyway.

	if ticker in scope.missing_tickers['cloud']:
		download_error = ticker + '  ---- ' + scope.missing_tickers['errors'][ticker]['yf']
		st.error(download_error)
	elif ticker in scope.missing_tickers['local']:
		load_error = ticker + '  ---- ' + scope.missing_tickers['errors'][ticker]['load']
		st.warning(load_error)
	else:
		st.success(ticker)




