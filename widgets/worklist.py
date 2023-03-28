import streamlit as st


def render_worklist(scope):

	app = scope.apps['display_app']

	worklist = scope.apps[app]['worklist_dropdown']
	widget_key = 'widget_' + app + '_worklist_dropdown'
	no_of_tickers = len(worklist)

	if no_of_tickers == 0:widget_label = 'Worklist (Empty)'
	if no_of_tickers == 1:widget_label = 'Worklist (1 Ticker)'
	if no_of_tickers  > 1:widget_label = 'Worklist (' + str(no_of_tickers) + ') Tickers'

	previous_selection = scope.apps[app]['render']['ticker_file']
	pos_for_previous = scope.apps[app]['render']['ticker_file'].index(previous_selection)	

	worklist.insert(0, 'Show/Hide Data')

	selectbox = st.selectbox(
			label		=widget_label, 
			options		=worklist,
			index		=pos_for_previous, 
			on_change	=store_loaded_ticker,
			args		=(scope, app, widget_key ),
			key			=widget_key,
			)

	return selectbox


def store_loaded_ticker(scope, app, widget_key):

	selected_ticker = scope[widget_key]

	# store the selection
	scope.apps[app]['render']['ticker_file'] = selected_ticker	

	st.write(selected_ticker)






# =========================================
# Errors Dropdown list
# =========================================



def render_ticker_load_and_download_errors(scope):
	# Same as render_worklist but only the errirs only 

	app = scope.apps['display_app']

	widget_key = 'widget_' + app + '_load_errors'
	
	ticker_error_list = create_error_list_for_page(scope, app)
	no_of_errors = len(ticker_error_list)

	# Create label for dropdown list
	if no_of_errors == 0:widget_label = '0 Errors'
	if no_of_errors == 1:widget_label = '1 Error'
	if no_of_errors  > 1:widget_label = '(' + str(no_of_errors) + ') Errors'

	selectbox = st.selectbox(
			label		=widget_label, 
			options		=ticker_error_list,
			key			=widget_key,
			)

	return selectbox

def create_error_list_for_page(scope, app):
	# create a list of errors relevant for this app/page
	ticker_error_list = []
	drop_down_list = []
	
	for ticker in scope.missing_tickers['list']:
		if ticker in scope.apps[app]['worklist']:
			ticker_error_list.append(ticker)

	for ticker in ticker_error_list:
		ticker_error_status = ticker + '---'

		if ticker in scope.missing_tickers['cloud']:
			ticker_error_status =  ticker_error_status + scope.missing_tickers['errors'][ticker]['yf']
		elif ticker in scope.missing_tickers['local']:
			ticker_error_status = ticker_error_status + scope.missing_tickers['errors'][ticker]['load']
		else:
			ticker_error_status = ticker_error_status + 'UNDETERMINED ERROR'

		drop_down_list.append(ticker_error_status)

	return drop_down_list



