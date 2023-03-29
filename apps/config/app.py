
import streamlit as st
from datetime import datetime 

from apps.config.three_cols import three_cols
from apps.app_header.page_config import view_app_page_config
from trials.config import trials_config
from charts.config import charts_config



def scope_apps(scope):

	scope.apps = {}
	base_config_apps(scope)
	scope.apps['button_for_scope'] = None
	scope.apps['app_list'] = ['chart', 'intraday', 'volume', 'research', 'screener', 'websites', 'index']
	
	# ==========================================
	# variables for each app from the app list above
	for app in scope.apps['app_list']:
		scope.apps[app] = {}
		scope.apps[app]['search_results'] = {}
		scope.apps[app]['worklist'] = []  # formally known as scope.apps[app]['ticker_list']
		scope.apps[app]['worklist_dropdown'] = []
		scope.apps[app]['tickers_with_add_cols'] = []
		
		scope.apps[app]['selectors'] = {
										'ticker'	: 'select a ticker',
										'tickers'	: [],
										'industries': [],
										'market'	: 'select market', 
										}
		
		scope.apps[app]['render'] = 	{
										'ticker_file':'Show/Hide Data',	# display the ticker files
										'app_config':False,				# display the application config
										'chart_settings':False,			# display the chart settings
										'overlay_settings':False,		# display the overlay settings
										'trial_settings':False,			# display the trial settings
										'strategy':False,				# display the strategy settings
								}


def base_config_apps(scope):
	# Setting can be changed for each user
	# so we need to be able to call when changing user

	scope.apps['row_limit'] = 100
	scope.apps['display_app'] = 'login'


def view_app(scope):

	st.subheader('Application Configuration')
	three_cols( 'Application Configuration stored in', {}, 'scope.config', widget_type='string' )

	st.subheader('Application')
	three_cols( 'Project Description', scope.config['project_description'], 'scope.config.project_description' )
	start_time =  datetime.fromtimestamp(scope.config['project_start_time']).strftime('%Y-%m-%d %H:%M:%S %p')
	three_cols( 'Project Start Time', start_time, 'scope.config.project_start_time' )

	st.subheader('Share Market')
	three_cols( 'Current Share Market', scope.config['share_market'], 'scope.config.share_market' )

	st.subheader('System')
	three_cols( 'Initial Load ?', scope.initial_load, 'initial_load' )
	
	st.write('---')
	view_app_page_config(scope)

