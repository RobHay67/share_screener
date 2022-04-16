import streamlit as st



def select_industries(scope):

	page = scope.pages['display_page']
	
	widget_key = 'widget_' + page + '_select_industries'
	previous_selection = scope.pages['screener']['selectors']['industries']

	st.multiselect ( 
				label		='Add an Industry or Industries', 
				options		=scope.config['dropdowns']['industries'],
				default		=previous_selection, 
				help		='Select all tickers within a particular industry',
				on_change	=on_change_industry_selection,
				args		=(scope, page, widget_key, ),
				key			=widget_key,
				) 


def on_change_industry_selection(scope:dict, page:str, widget_key:str):
	
	changed_value = scope[widget_key]

	# store the selection
	scope.pages[page]['selectors']['industries'] = changed_value


