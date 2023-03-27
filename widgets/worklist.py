import streamlit as st


def render_worklist(scope):

	app = scope.apps['display_app']

	worklist = scope.apps[app]['worklist_dropdown']
	widget_key = 'widget_' + app + '_worklist_dropdown'
	no_of_tickers = len(worklist)

	if no_of_tickers == 0:
		widget_label = 'Empty Worklist'

	if no_of_tickers == 1:
		widget_label = 'Worklist (1 Ticker)'

	if no_of_tickers > 1:
		widget_label = 'Work List (' + str(no_of_tickers) + ') Tickers'

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
	ticker_status = ticker + ' '

	if ticker in scope.missing_tickers['cloud']:
		ticker_status =  ticker_status + scope.missing_tickers['errors'][ticker]['yf']
	elif ticker in scope.missing_tickers['local']:
		ticker_status = ticker_status + scope.missing_tickers['errors'][ticker]['load']
	else:
		if ticker in list(scope.tickers.keys()): 
			ticker_df = scope.tickers[ticker]['df']

			no_of_rows = ' (' + str(len(ticker_df)) +') '
			# Date Range
			min_date = ticker_df['date'].min()
			max_date = ticker_df['date'].max()
			# min_date = str(min_date).split()[0]
			# max_date = str(max_date).split()[0]
			min_date = str(min_date.strftime("%d-%b-%Y"))
			max_date = str(max_date.strftime("%d-%b-%Y"))

			ticker_status = ticker_status + no_of_rows + min_date + ' - ' + max_date 
		else:
			ticker_status = ticker_status + 'not loaded'
	
	return ticker_status




