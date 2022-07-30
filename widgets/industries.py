import streamlit as st



def select_industries(scope):

	app = scope.apps['display_app']
	
	widget_key = 'widget_' + app + '_select_industries'
	previous_selection = scope.apps['screener']['selectors']['industries']

	st.multiselect ( 
				label		='Add an Industry or Industries', 
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
	scope.apps[app]['selectors']['industries'] = changed_value


