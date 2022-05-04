import streamlit as st





def select_a_market(scope):

	page = scope.pages['display_page']
	
	widget_key = 'widget_' + page + '_select_market'
	previous_selection = scope.pages['screener']['selectors']['market']
	pos_for_previous = scope.config['dropdowns']['markets'].index(previous_selection)	

	st.selectbox ( 
				label		='Add a Market to Ticker List',
				options		=scope.config['dropdowns']['markets'],
				index		=pos_for_previous, 
				help		='Select an Entire Share Market for Analysis',
				on_change	=on_change_market_selection,
				args		=(scope, page, widget_key, ),
				key			=widget_key,
				) 


def on_change_market_selection(scope:dict, page:str, widget_key:str):
	
	changed_value = scope[widget_key]

	# store the selection
	scope.pages[page]['selectors']['market'] = changed_value




