import streamlit as st


def ticker_load_and_download_errors_dropdown(scope):
	# =========================================
	# Errors Dropdown list
	# =========================================

	
	# Same as render_worklist_dropdown but only the errirs only 

	page = scope.config['display']

	widget_key = 'widget_' + page + '_load_errors'
	
	ticker_error_list = create_error_list_for_page(scope, page)
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

def create_error_list_for_page(scope, page):
	# create a list of errors relevant for this page/page
	ticker_error_list = []
	drop_down_list = []
	
	for ticker in scope.ticker_config['missing']['list']:
		if ticker in scope.page[page]['worklist']:
			ticker_error_list.append(ticker)

	for ticker in ticker_error_list:
		ticker_error_status = ticker + '---'

		if ticker in scope.ticker_config['missing']['cloud']:
			ticker_error_status =  ticker_error_status + scope.ticker_config['missing']['errors'][ticker]['yf']
		elif ticker in scope.ticker_config['missing']['local']:
			ticker_error_status = ticker_error_status + scope.ticker_config['missing']['errors'][ticker]['load']
		else:
			ticker_error_status = ticker_error_status + 'UNDETERMINED ERROR'

		drop_down_list.append(ticker_error_status)

	return drop_down_list

