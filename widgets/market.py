import streamlit as st





def select_a_market(scope):

	app = scope.apps['display_app']
	
	widget_key = 'widget_' + app + '_select_market'
	previous_selection = scope.apps['screener']['selectors']['market']
	pos_for_previous = scope.config['dropdowns']['markets'].index(previous_selection)	

	st.selectbox ( 
				label		='Add a Market to Ticker List',
				options		=scope.config['dropdowns']['markets'],
				index		=pos_for_previous, 
				help		='Select an Entire Share Market for Analysis',
				on_change	=on_change_market_selection,
				args		=(scope, app, widget_key, ),
				key			=widget_key,
				) 


def on_change_market_selection(scope:dict, app:str, widget_key:str):
	
	changed_value = scope[widget_key]

	# store the selection
	scope.apps[app]['selectors']['market'] = changed_value




