import streamlit as st


def select_a_ticker(scope):

	page = scope.pages['display']
	
	widget_key = 'widget_' + page + '_select_ticker'
	display_name = 'Select a Ticker'
	previous_selection = scope.pages[page]['selectors']['ticker']
	pos_for_previous = scope.config['dropdowns']['ticker'].index(previous_selection)	
	
	st.selectbox ( 
				label		=display_name, 
				options		=scope.config['dropdowns']['ticker'],
				index		=pos_for_previous, 
				help		='Choose a ticker. Start typing to jump down the list',
				on_change	=on_change_ticker_selection,
				args		=(scope, page, widget_key, ),
				key			=widget_key,
				) 


def on_change_ticker_selection(scope, page, widget_key):
	
	changed_value = scope[widget_key]

	# store the selection
	scope.pages[page]['selectors']['ticker'] = changed_value
	scope.pages[page]['search_results'] = {}







