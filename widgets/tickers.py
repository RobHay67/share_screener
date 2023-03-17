import streamlit as st



def select_tickers(scope):

	app = scope.apps['display_app']
	
	widget_key = 'widget_' + app + '_select_tickers'
	previous_selection = scope.apps['screener']['selectors']['tickers']
	display_name = 'Ticker(s)'

	st.multiselect ( 
				label		=display_name,
				options		=scope.config['dropdowns']['tickers'],
				default		=previous_selection, 
				help		='Select a ticker, or multiple tickers from the dropdown. Start typing to jump within list',
				on_change	=on_change_tickers_selection,
				args		=(scope, app, widget_key, ),
				key			=widget_key,
				) 


def on_change_tickers_selection(scope:dict, app:str, widget_key:str):
	
	changed_value = scope[widget_key]

	# store the selection
	scope.apps[app]['selectors']['tickers'] = changed_value
	scope.apps[app]['selectors']['industries'] = []
	scope.apps[app]['selectors']['market'] = 'select market'
	scope.apps[app]['search_results'] = {}