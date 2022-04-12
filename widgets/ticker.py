import streamlit as st


def select_a_ticker(scope):

	page = scope.pages['display_page']
	
	widget_key = 'widget_' + page + '_select_ticker'
	previous_selection = scope.pages[page]['selectors']['ticker']
	pos_for_previous = scope.config['dropdowns']['ticker'].index(previous_selection)	

	st.selectbox ( 
				label		='Select a Ticker', 
				options		=scope.config['dropdowns']['ticker'],
				index		=pos_for_previous, 
				help		='Choose a ticker. Start typing to jump down the list',
				on_change	=on_change_ticker_selection,
				args		=(scope, page, widget_key, ),
				key			=widget_key,
				) 


def on_change_ticker_selection(scope:dict, page:str, widget_key:str):
	
	changed_value = scope[widget_key]

	# store the selection in the selectors.ticker scope value
	scope.pages[page]['selectors']['ticker'] = changed_value



	# ticker_list = scope.pages[page]['ticker_list']

	# if changed_value != None:
	# 	if changed_value

	# ticker_list = [ changed_value ] if changed_value != 'select a ticker' else [None]

	# Update the ticker list for this page
	# if changed_value not in scope.pages[page]['ticker_list']:
	# 	scope.pages[page]['ticker_list'].append(changed_value)




	# # Update the ticker list for this page
	# scope.pages[page]['ticker_list'] = ticker_list

