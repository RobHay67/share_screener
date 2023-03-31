import streamlit as st



def select_industries(scope):

	app = scope.apps['display_app']
	
	widget_key = 'widget_' + app + '_select_industries'
	previous_selection = scope.apps['screener']['selectors']['industries']

	st.multiselect ( 
				label		='Industry(s)', 
				options		=scope.config['dropdowns']['industries'],
				default		=previous_selection, 
				help		='Select all tickers within a particular industry',
				on_change	=on_change_industry_selection,
				args		=(scope, app, widget_key, ),
				key			=widget_key,
				) 


def on_change_industry_selection(scope:dict, app:str, widget_key:str):
	
	changed_value = scope[widget_key]

	# store the selection
	scope.apps[app]['selectors']['tickers'] = []
	scope.apps[app]['selectors']['industries'] = changed_value
	scope.apps[app]['selectors']['market'] = 'select market'
	scope.apps[app]['search_results'] = {}


def industry_report_button(scope):

	widget_key = 'widget_' + 'ticker_index' + '_industry_report'

	button = st.button(
					label = 'Industry Report', 
					use_container_width=True, 
					on_click=industry_report_status, 
					args=(scope, ),
	# 				help='Show a Report by Industry (expandable to show codes)',
					key=widget_key,
					)

	return button



def industry_report_status(scope):

	previous_value = scope.ticker_index['render']['industry_report']
	new_value = True if previous_value == False else False

	scope.ticker_index['render']['industry_report'] = new_value