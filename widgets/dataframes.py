# Function to provide a list of the loaded ticker
# - for each app/page
# - or all loaded tickers if scope page



import streamlit as st

# ==================================
# Tickers Files loaded for the Page
# ==================================


def page_df_loaded_ticker_files(scope, app):

	ticker_list = []

	if app in ['screener', 'chart']:
		ticker_list = scope.apps[app]['worklist'].copy()
		ticker_list = [t for t in ticker_list if t not in scope.missing_tickers['list']]

	if app == 'scope':
		ticker_list = list(scope.tickers.keys())

	ticker_list.insert(0, 'Show/Hide Data')

	return ticker_list


def dataframe_dropdown_list(scope):
	
	app = scope.apps['display_app']
	no_of_dfs = 0
	rows_total = 0
	widget_key = 'widget_' + app + '_df'

	page_ticker_list = page_df_loaded_ticker_files(scope, app)

	# Number of rows
	for ticker in page_ticker_list:
		if ticker != 'Show/Hide Data':
			df_row_count = int(len(scope.tickers[ticker]['df']))
			rows_total += df_row_count

	no_of_dfs 	= len(page_ticker_list)-1
	widget_label_count = ' files ' if no_of_dfs == 1 else ' files ('
	widget_label 	= ('Loaded ' + str(no_of_dfs) + widget_label_count + str(rows_total) + ' rows)')

	previous_selection = scope.apps[app]['render']['ticker_file']
	pos_for_previous = scope.apps[app]['render']['ticker_file'].index(previous_selection)	

	selectbox = st.selectbox(
				label		=widget_label, 
				options		=page_ticker_list,
				index		=pos_for_previous, 
				on_change	=store_loaded_ticker,
				args		=(scope, app, widget_key ),
				key			=widget_key,
				)
	return selectbox


def store_loaded_ticker(scope, app, widget_key):

	selected_ticker = scope[widget_key]

	# st.header(selected_ticker)

	# store the selection
	scope.apps[app]['render']['ticker_file'] = selected_ticker	

# ==================================
# Tickers with Added Columns
# ==================================

def page_df_with_add_columns(scope, app):

	page_ticker_list = []

	if app in ['screener', 'chart']:
		page_ticker_list = scope.apps[app]['tickers_with_add_cols'].copy()

	page_ticker_list.insert(0, 'Show/Hide Data')

	return page_ticker_list


def page_dataframe_dropdown_list(scope):
	
	app = scope.apps['display_app']
	no_of_dfs = 0
	rows_total = 0
	widget_key = 'widget_' + app + '_page_df'

	page_ticker_list = page_df_with_add_columns(scope, app)

	# Number of rows
	for ticker in page_ticker_list:
		if ticker != 'Show/Hide Data':
			df_row_count = int(len(scope.tickers[ticker]['df']))
			rows_total += df_row_count

	no_of_dfs 	= len(page_ticker_list)-1
	widget_label_count = ' files ' if no_of_dfs == 1 else ' files ('
	widget_label 	= ('Page ' + str(no_of_dfs) + widget_label_count + str(rows_total) + ' rows)')

	previous_selection = scope.apps[app]['render']['ticker_file']
	pos_for_previous = scope.apps[app]['render']['ticker_file'].index(previous_selection)	

	selectbox = st.selectbox(
				label		=widget_label, 
				options		=page_ticker_list,
				index		=pos_for_previous, 
				on_change	=store_ticker_with_add_cols,
				args		=(scope, app, widget_key ),
				key			=widget_key,
				)
	return selectbox

def store_ticker_with_add_cols(scope, app, widget_key):

	selected_ticker = scope[widget_key]
	scope.apps[app]['render']['col_added_df'] = selected_ticker	











# TODO - not sure that these are needed anymore - might be able to
# deprecate or delete these functions
# keep handy for a template for the minute
def reset_page_render(scope):
	st.button(
			label='Hide Additional Info', 
			use_container_width=True,
			on_click=reset_render_status, 
			args=(scope,)
			)



def reset_render_status(scope):
	app = scope.apps['display_app']

	scope.apps[app]['render']['tickers'] = False
	scope.apps[app]['render']['charts'] = False
	scope.apps[app]['render']['trials'] = False




