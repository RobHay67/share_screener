import streamlit as st





def select_a_market(scope):

	page = scope.pages['display']
	
	widget_key = 'widget_' + page + '_select_market'
	previous_selection = scope.pages[page]['selectors']['market']
	pos_for_previous = scope.pages['dropdowns']['markets'].index(previous_selection)	

	st.selectbox ( 
				label		='Market',
				options		=scope.pages['dropdowns']['markets'],
				index		=pos_for_previous, 
				help		='Select an Entire Share Market for Analysis',
				on_change	=on_change_market_selection,
				args		=(scope, page, widget_key, ),
				key			=widget_key,
				) 


def on_change_market_selection(scope, page, widget_key):
	
	changed_value = scope[widget_key]

	# store the selection
	scope.pages[page]['selectors']['tickers'] = []
	scope.pages[page]['selectors']['industries'] = []
	scope.pages[page]['selectors']['market'] = changed_value
	scope.pages[page]['search_results'] = {}