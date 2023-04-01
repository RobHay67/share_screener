import streamlit as st



def render_active_charts_or_tests(scope):

	app = scope.apps['display_app']
	
	if app in ['screener', 'chart']:

		widget_key = 'widget_' + app + '_active_list_dropdown'
		widget_label = 'Number of active '

		if app == 'screener':
			active_list = scope.trial_config['active_list']
			widget_label = widget_label+'trials / tests = '+str(len(active_list))
		if app =='chart':
			active_list = scope.chart_config['active_list']
			widget_label = widget_label+'charts = '+str(len(active_list))

		print(widget_label)

		st.selectbox(
				label		=widget_label, 
				options		=active_list,
				key			=widget_key,
				)


def render_worklist_dropdown(scope):

	app = scope.apps['display_app']

	worklist = scope.apps[app]['worklist_dropdown']
	widget_key = 'widget_' + app + '_worklist_dropdown'
	no_of_tickers = len(worklist)-1 # as a default is inserted at the top

	if no_of_tickers  < 1:widget_label = 'Worklist (Empty)'
	if no_of_tickers == 1:widget_label = 'Worklist (1 Ticker)'
	if no_of_tickers  > 1:widget_label = 'Worklist (' + str(no_of_tickers) + ') Tickers'

	previous_selection = scope.apps[app]['render']['ticker_file']
	pos_for_previous = scope.apps[app]['render']['ticker_file'].index(previous_selection)	

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


def render_ticker_load_and_download_errors(scope):
	# =========================================
	# Errors Dropdown list
	# =========================================

	
	# Same as render_worklist_dropdown but only the errirs only 

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



