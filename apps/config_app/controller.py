import streamlit as st

# Config (scope)
from apps.config_app.scope import view_app
from apps.config_app.dropdowns import view_dropdowns
from apps.config_app.scope import view_trials_config
from apps.config_app.scope import view_charts_config
from apps.config_app.results import view_all_results
# Files
from apps.config_app.files import view_folders
# Data
from ticker_index.view.index import view_index
from partials.dataframes.tickers import view_ticker_files
from tickers.view.download import view_download
# Pages
from apps.config_app.apps import view_apps
from apps.config_app.apps import view_single_page
from apps.config_app.apps import view_intra_day_page
from apps.config_app.apps import view_volume_page
from apps.config_app.apps import view_research_page
from apps.config_app.apps import view_screener_page
from partials.dataframes.trials import view_trials_dfs
from partials.dataframes.charts import view_chart_dfs

# Strategies
from strategies.config import view_strategy
# Reports
from ticker_index.download import download_ticker_index_data
from ticker_index.view.industries import view_industries


def render_selected_scope_page(scope):

	scope_page = {
			# Column 1 - Config (scope)
			'application'			:view_app,
			'dropdowns'				:view_dropdowns,
			'trials'				:view_trials_config,
			'charts'				:view_charts_config,
			'results'				:view_all_results,
			# Column 2 - Files
			'view_folders'			:view_folders,
			# Column 3 - Data
			'view_ticker_index'		:view_index,
			'view_ticker_files'		:view_ticker_files,
			'view_download'			:view_download,
			# Column 4 - Pages
			'view_apps'				:view_apps,
			'view_single_page'		:view_single_page,
			'view_intra_day_page'	:view_intra_day_page,
			'view_volume_page'		:view_volume_page,
			'view_research_page'	:view_research_page,
			'view_screener_page'	:view_screener_page,
			'view_trials_dfs'		:view_trials_dfs,
			'view_chart_dfs'		:view_chart_dfs,
			# Column 5 - Strategy
			'view_strategy'			:view_strategy,
			# Column 6 - Reports & Actions
			'import_tickers'		:download_ticker_index_data,
			'view_industries'		:view_industries,
			}

	scope_page[scope.apps['button_for_scope']](scope)

	scope.apps['button_for_scope'] =  None


def set_st_button(scope:dict, button:str):
	scope.apps['button_for_scope'] = button


def render_scope_categories(scope):
	st.header('Configuration Setting')

	col1,col2,col3,col4,col5,col6 = st.columns([2,2,2,2,2,2])
	
	with col1: 
		st.subheader('Config (scope)')
		st.button('Application', on_click=set_st_button, args=(scope, 'application', ))
		st.button('Dropdowns', on_click=set_st_button, args=(scope, 'dropdowns', ))
		st.button('Trials  (column adders)', on_click=set_st_button, args=(scope, 'trials', ))
		st.button('Charts (column adders)', on_click=set_st_button, args=(scope, 'charts', ))
		st.button('Results', on_click=set_st_button, args=(scope, 'results', ))

	with col2: 
		st.subheader('Files')
		st.button('Folders and Paths', on_click=set_st_button, args=(scope, 'view_folders', ))

	with col3: 
		st.subheader('Data')
		no_of_tickers_in_index = str((len(scope.ticker_index)))
		no_of_loaded_dfs = str(len(scope.ticker_files.keys()))
		st.button('Ticker Index Report ( ' + no_of_tickers_in_index + ' )', on_click=set_st_button, args=(scope, 'view_ticker_index', ))
		st.button('Loaded Ticker Data Files ( ' + no_of_loaded_dfs + ' )', on_click=set_st_button, args=(scope, 'view_ticker_files', ))
		st.button('Download', on_click=set_st_button, args=(scope, 'view_download', ))

	with col4: 
		st.subheader('Apps')
		st.button('App', on_click=set_st_button, args=(scope, 'view_apps', ))
		st.button('App > Single', on_click=set_st_button, args=(scope, 'view_single_page', ))
		st.button('App > Intra-Day', on_click=set_st_button, args=(scope, 'view_intra_day_page', ))
		st.button('App > Volume', on_click=set_st_button, args=(scope, 'view_volume_page', ))
		st.button('App > Research', on_click=set_st_button, args=(scope, 'view_research_page', ))
		st.button('App > Screener', on_click=set_st_button, args=(scope, 'view_screener_page', ))
		
		no_of_screener_dfs = str(len(scope.apps['screener']['dfs'].keys()))
		no_of_chart_dfs = str(len(scope.apps['single']['dfs'].keys()))
		st.button('Screener Dataframes ( ' + no_of_screener_dfs + ' )', on_click=set_st_button, args=(scope, 'view_tests_dfs', ))
		st.button('Charting Dataframes ( ' + no_of_chart_dfs + ' )', on_click=set_st_button, args=(scope, 'view_chart_dfs', ))

	with col5: 
		st.subheader('Strategies')
		st.button('Strategy', on_click=set_st_button, args=(scope, 'view_strategy', ))

	with col6:
		st.subheader('Actions and Reports')
		st.button('Import New Tickers', on_click=set_st_button, args=(scope, 'import_tickers', ))
		st.button('Industry Report', on_click=set_st_button, args=(scope, 'view_industries', ))

	st.markdown("""---""")

	if scope.apps['button_for_scope'] != None:
		
		render_selected_scope_page(scope)

