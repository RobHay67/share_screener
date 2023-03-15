import streamlit as st

# Config (scope)
from apps.config_app.scope import view_app
from apps.config_app.dropdowns import view_dropdowns
from apps.config_app.scope import view_trials_config
from apps.config_app.scope import view_charts_config
# Files
from apps.config_app.files import view_folders
# Data
# from partials.reports.index import render_ticker_index
from apps.config_app.download import view_download
# Strategies
# from strategies.config import view_strategy
# Reports
# from ticker_index.download import download_ticker_index_data
# from partials.reports.industries import view_industries


def render_selected_scope_page(scope):

	scope_page = {
			# Column 1 - Config (scope)
			'application'			:view_app,
			'dropdowns'				:view_dropdowns,
			'trials'				:view_trials_config,
			'charts'				:view_charts_config,
			# Column 2 - Files
			'view_folders'			:view_folders,
			# Column 3 - Data
			# 'view_ticker_index'		:render_ticker_index,
			'view_download'			:view_download,
			# Column 5 - Strategy
			# 'view_strategy'			:view_strategy,
			# Column 6 - Reports & Actions
			# 'import_tickers'		:download_ticker_index_data,
			# 'view_industries'		:view_industries,
			}

	scope_page[scope.apps['button_for_scope']](scope)

	scope.apps['button_for_scope'] =  None


def set_st_button(scope:dict, button:str):
	scope.apps['button_for_scope'] = button


def render_scope_categories(scope):
	st.subheader('Configuration Setting')

	col1,col2,col3,col4,col5,col6 = st.columns([2,2,2,2,2,2])
	
	with col1: 
		# st.subheader('Config (scope)')
		st.button('Application', use_container_width=True, on_click=set_st_button, args=(scope, 'application', ))
		st.button('Dropdowns', use_container_width=True, on_click=set_st_button, args=(scope, 'dropdowns', ))
		st.button('Trials  (column adders)', use_container_width=True, on_click=set_st_button, args=(scope, 'trials', ))
		st.button('Charts (column adders)', use_container_width=True, on_click=set_st_button, args=(scope, 'charts', ))

	with col2: 
		# st.subheader('Files')
		st.button('Folders and Paths', use_container_width=True, on_click=set_st_button, args=(scope, 'view_folders', ))

	with col3: 
		# st.subheader('Data')
		# no_of_tickers_in_index = str((len(scope.ticker_index)))
		# no_of_loaded_dfs = str(len(scope.tickers.keys()))
		# st.button('Ticker Index Report ( ' + no_of_tickers_in_index + ' )', on_click=set_st_button, args=(scope, 'view_ticker_index', ))
		# st.button('Ticker Data Files   ( ' + no_of_loaded_dfs + ' )', on_click=set_st_button, args=(scope, 'render_ticker_dfs', ))
		st.button('Download Dictionaries', use_container_width=True, on_click=set_st_button, args=(scope, 'view_download', ))

	# with col4: 
	# 	st.subheader('Apps')		
	# 	no_of_chart_dfs = str(len(scope.apps['chart']['mined_tickers']))
	# 	no_of_trial_dfs = str(len(scope.apps['screener']['mined_tickers']))
		# st.button('Chart Dataframes ( ' + no_of_chart_dfs + ' )', on_click=set_st_button, args=(scope, 'render_chart_dfs', ))
		# st.button('Trial Dataframes ( ' + no_of_trial_dfs + ' )', on_click=set_st_button, args=(scope, 'render_trial_dfs', ))

	# with col5: 
	# 	st.subheader('Strategies')
	# 	st.button('Strategy', on_click=set_st_button, args=(scope, 'view_strategy', ))

	# with col6:
		# st.subheader('Actions and Reports')
		# st.button('Download Ticker Info from Share Market', on_click=set_st_button, args=(scope, 'import_tickers', ))
		# st.button('Industry Report', on_click=set_st_button, args=(scope, 'view_industries', ))

	st.markdown("""---""")

	if scope.apps['button_for_scope'] != None:
		
		render_selected_scope_page(scope)

