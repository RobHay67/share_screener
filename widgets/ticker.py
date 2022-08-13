import streamlit as st


def select_a_ticker(scope, ticker=None):

	app = scope.apps['display_app']
	
	widget_key = 'widget_' + app + '_select_ticker'
	display_name = 'Select a Ticker'
	previous_selection = scope.apps[app]['selectors']['ticker']
	pos_for_previous = scope.config['dropdowns']['ticker'].index(previous_selection)	

	st.selectbox ( 
				label		=display_name, 
				options		=scope.config['dropdowns']['ticker'],
				index		=pos_for_previous, 
				help		='Choose a ticker. Start typing to jump down the list',
				on_change	=on_change_ticker_selection,
				args		=(scope, app, widget_key, ),
				key			=widget_key,
				) 


def on_change_ticker_selection(scope:dict, app:str, widget_key:str):
	
	changed_value = scope[widget_key]

	# store the selection
	scope.apps[app]['selectors']['ticker'] = changed_value
	scope.apps[app]['search_results'] = {}







