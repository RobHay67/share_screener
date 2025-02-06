import logging
import streamlit as st



def select_industries(scope):
	logging.debug("_select_industries")
	page = scope.display['page']
	
	widget_key = 'widget_' + page + '_select_industries'
	previous_selection = scope.page[page]['selectors']['industries']

	st.multiselect ( 
				label		='Industry(s)', 
				options		=scope.config['dropdowns']['industries'],
				default		=previous_selection, 
				help		='Select all tickers within a particular industry',
				on_change	=on_change_industry_selection,
				args		=(scope, page, widget_key, ),
				key			=widget_key,
				) 


def on_change_industry_selection(scope, page, widget_key):
	logging.debug("on_change_industry_selection")
	changed_value = scope[widget_key]

	# store the selection
	scope.page[page]['selectors']['tickers'] = []
	scope.page[page]['selectors']['industries'] = changed_value
	scope.page[page]['selectors']['market'] = 'select market'
	scope.page[page]['search_results'] = {}






