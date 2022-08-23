import streamlit as st

# Config (scope)
from apps.config_app.scope import view_app
from apps.config_app.dropdowns import view_dropdowns
from apps.config_app.scope import view_trials_config
from apps.config_app.scope import view_charts_config
# Files
from apps.config_app.files import view_folders
# Data
from partials.reports.index import render_ticker_index
from apps.config_app.download import view_download


# Pages
from apps.config_app.apps import view_apps
from apps.config_app.apps import view_single_page
from apps.config_app.apps import view_intra_day_page
from apps.config_app.apps import view_volume_page
from apps.config_app.apps import view_research_page
from apps.config_app.apps import view_screener_page

from partials.reports.dfs import render_ticker_dfs
from partials.reports.dfs import render_chart_dfs
from partials.reports.dfs import render_trial_dfs

# Strategies
from strategies.config import view_strategy
# Reports
from ticker_index.download import download_ticker_index_data
from partials.reports.industries import view_industries


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
			'view_ticker_index'		:render_ticker_index,
			'render_ticker_dfs'		:render_ticker_dfs,
			'view_download'			:view_download,
			# Column 4 - Pages
			'view_apps'				:view_apps,
			'view_single_page'		:view_single_page,
			'view_intra_day_page'	:view_intra_day_page,
			'view_volume_page'		:view_volume_page,
			'view_research_page'	:view_research_page,
			'view_screener_page'	:view_screener_page,
			'view_ticker_dfs'		:render_ticker_dfs,
			'render_trial_dfs'		:render_trial_dfs,
			'render_chart_dfs'		:render_chart_dfs,
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

	with col2: 
		st.subheader('Files')
		st.button('Folders and Paths', on_click=set_st_button, args=(scope, 'view_folders', ))

	with col3: 
		st.subheader('Data')
		no_of_tickers_in_index = str((len(scope.ticker_index)))
		no_of_loaded_dfs = str(len(scope.tickers.keys()))
		st.button('Ticker Index Report ( ' + no_of_tickers_in_index + ' )', on_click=set_st_button, args=(scope, 'view_ticker_index', ))
		st.button('Ticker Data Files   ( ' + no_of_loaded_dfs + ' )', on_click=set_st_button, args=(scope, 'render_ticker_dfs', ))
		st.button('Download', on_click=set_st_button, args=(scope, 'view_download', ))

	with col4: 
		st.subheader('Apps')
		st.button('App', on_click=set_st_button, args=(scope, 'view_apps', ))
		st.button('App > Single', on_click=set_st_button, args=(scope, 'view_single_page', ))
		st.button('App > IntraDay', on_click=set_st_button, args=(scope, 'view_intra_day_page', ))
		st.button('App > Volume', on_click=set_st_button, args=(scope, 'view_volume_page', ))
		st.button('App > Research', on_click=set_st_button, args=(scope, 'view_research_page', ))
		st.button('App > Screener', on_click=set_st_button, args=(scope, 'view_screener_page', ))
		
		no_of_chart_dfs = str(len(scope.apps['single']['mined_tickers']))
		no_of_trial_dfs = str(len(scope.apps['screener']['mined_tickers']))
		st.button('Chart Dataframes ( ' + no_of_chart_dfs + ' )', on_click=set_st_button, args=(scope, 'render_chart_dfs', ))
		st.button('Trial Dataframes ( ' + no_of_trial_dfs + ' )', on_click=set_st_button, args=(scope, 'render_trial_dfs', ))

	with col5: 
		st.subheader('Strategies')
		st.button('Strategy', on_click=set_st_button, args=(scope, 'view_strategy', ))

	with col6:
		st.subheader('Actions and Reports')
		st.button('Download Ticker Info from Share Market', on_click=set_st_button, args=(scope, 'import_tickers', ))
		st.button('Industry Report', on_click=set_st_button, args=(scope, 'view_industries', ))

	st.markdown("""---""")

	if scope.apps['button_for_scope'] != None:
		
		render_selected_scope_page(scope)

