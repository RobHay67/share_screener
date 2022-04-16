import streamlit as st



def select_tickers(scope):

	page = scope.pages['display_page']
	
	widget_key = 'widget_' + page + '_select_tickers'
	previous_selection = scope.pages['screener']['selectors']['tickers']
	# pos_for_previous = scope.config['dropdowns']['ticker'].index(previous_selection)	

	st.multiselect ( 
				label		='Add a Ticker or Tickers',
				options		=scope.config['dropdowns']['tickers'],
				default		=previous_selection, 
				help		='Select a ticker, or multiple tickers from the dropdown. Start typing to jump within list',
				on_change	=on_change_tickers_selection,
				args		=(scope, page, widget_key, ),
				key			=widget_key,
				) 


def on_change_tickers_selection(scope:dict, page:str, widget_key:str):
	
	changed_value = scope[widget_key]

	# store the selection
	scope.pages[page]['selectors']['tickers'] = changed_value







# def select_tickers(scope):

# 	# page = scope.pages['display_page']
# 	# widget_key = 'widget_' + page + '_select_tickers'



# 	previous_selection = scope.pages[page]['selectors']['tickers']

# 	scope.pages[page]['selectors']['tickers'] = st.multiselect(
# 																label='Add a Ticker or Tickers',
# 																options=scope.config['dropdowns']['tickers'], 
# 																default=previous_selection, 
# 																help='Select a ticker, or multiple tickers from the dropdown. Start typing to jump within list',
# 																key=widget_key
# 																)

# 	# scope.pages['screener']['selectors']['tickers'] = new_selection

