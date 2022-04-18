import streamlit as st



def select_tickers(scope):

	page = scope.pages['display_page']
	
	widget_key = 'widget_' + page + '_select_tickers'
	previous_selection = scope.pages['screener']['selectors']['tickers']
	display_name = 'Add a Ticker or Tickers',

	st.multiselect ( 
				label		=display_name,
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





