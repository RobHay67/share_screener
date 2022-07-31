import streamlit as st

# Config (scope)
from apps.scope.scope import view_app
from apps.scope.dropdowns import view_dropdowns
from apps.scope.scope import view_tests_config
from apps.scope.scope import view_charts_config
from apps.scope.results import view_all_results
# Files
from apps.scope.files import view_folders
# Data
from data.index.view.index import view_index
from data.tickers.view.dataframes import view_ticker_files
from data.tickers.view.download import view_download
# Pages
from apps.scope.apps import view_apps
from apps.scope.apps import view_single_page
from apps.scope.apps import view_intra_day_page
from apps.scope.apps import view_volume_page
from apps.scope.apps import view_research_page
from apps.scope.apps import view_screener_page
from apps_parts.dataframes.tests import view_tests_dfs
from apps_parts.dataframes.charts import view_chart_dfs

# Strategies
from strategies.config import view_strategy
# Reports
from data.index.download import download_ticker_index_data
from data.index.view.industries import view_industries


def render_selected_scope_page(scope):

	scope_page = {
			# Column 1 - Config (scope)
			'application'			:view_app,
			'dropdowns'				:view_dropdowns,
			'tests'					:view_tests_config,
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
			'view_tests_dfs'		:view_tests_dfs,
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
		st.subheader('Config (scope)') # TODO
		st.button('Application', on_click=set_st_button, args=(scope, 'application', ))
		st.button('Dropdowns', on_click=set_st_button, args=(scope, 'dropdowns', ))
		st.button('Tests  (column adders)', on_click=set_st_button, args=(scope, 'tests', ))
		st.button('Charts (column adders)', on_click=set_st_button, args=(scope, 'charts', ))
		st.button('Results', on_click=set_st_button, args=(scope, 'results', ))

	with col2: 
		st.subheader('Files') # DONE
		st.button('Folders and Paths', on_click=set_st_button, args=(scope, 'view_folders', ))

	with col3: 
		st.subheader('Data') # TODO
		no_of_tickers_in_index = str((len(scope.data['ticker_index'])))
		no_of_loaded_dfs = str(len(scope.data['ticker_files'].keys()))
		st.button('Ticker Index Report ( ' + no_of_tickers_in_index + ' )', on_click=set_st_button, args=(scope, 'view_ticker_index', ))
		st.button('Loaded Ticker Data Files ( ' + no_of_loaded_dfs + ' )', on_click=set_st_button, args=(scope, 'view_ticker_files', ))
		st.button('Download', on_click=set_st_button, args=(scope, 'view_download', ))

	with col4: 
		st.subheader('Pages') # DONE
		st.button('Pages', on_click=set_st_button, args=(scope, 'view_apps', ))
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
		st.subheader('Strategies') # TODO
		st.button('Strategy', on_click=set_st_button, args=(scope, 'view_strategy', ))

	with col6:
		st.subheader('Actions and Reports') # TODO
		st.button('Import New Tickers', on_click=set_st_button, args=(scope, 'import_tickers', ))
		st.button('Industry Report', on_click=set_st_button, args=(scope, 'view_industries', ))

	st.markdown("""---""")

	if scope.apps['button_for_scope'] != None:
		
		render_selected_scope_page(scope)

