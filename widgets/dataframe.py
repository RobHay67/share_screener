# Function to provide a list of the loaded ticker
# - for each app/page
# - or all loaded tickers if scope page



import streamlit as st



def loaded_page_ticker_list(scope, app):

	ticker_list = []

	if app in ['screener', 'chart']:
		ticker_list = scope.apps[app]['worklist']
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

	page_ticker_list = loaded_page_ticker_list(scope, app)

	# Number of rows
	for ticker in page_ticker_list:
		if ticker != 'Show/Hide Data':
			df_row_count = int(len(scope.tickers[ticker]['df']))
			rows_total += df_row_count

	no_of_dfs 	= len(page_ticker_list)
	widget_label_count = ' files ' if no_of_dfs == 1 else ' files ('
	widget_label 	= ('Loaded ' + str(no_of_dfs) + widget_label_count + str(rows_total) + ' rows)')

	previous_selection = scope.apps[app]['render']['ticker_file']
	pos_for_previous = scope.apps[app]['render']['ticker_file'].index(previous_selection)	

	selectbox = st.selectbox(
				label		=widget_label, 
				options		=page_ticker_list,
				index		=pos_for_previous, 
				on_change	=tag_to_display_df,
				args		=(scope, app, widget_key ),
				key			=widget_key,
				)
	return selectbox

def tag_to_display_df(scope, app, widget_key):

	selected_ticker = scope[widget_key]

	# store the selection
	scope.apps[app]['render']['ticker_file'] = selected_ticker	













# TODO - not sure that these are needed anymore - might be able to
# deprecate or delete these functions
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




