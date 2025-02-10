import logging
import streamlit as st



def select_industries(scope):
	logging.debug("select_industries")
	page = scope.display['page']
	
	widget_key = 'widget_' + page + '_select_industries'
	previous_selection = scope.page[page]['selectors']['industries']

	st.multiselect ( 
				label		='Industry(s)', 
				options		=scope.config['dropdowns']['industries'],
				default		=previous_selection, 
				help		='Select all tickers within a particular industry',
				on_change	=changed_industry_selection,
				args		=(scope, page, widget_key, ),
				key			=widget_key,
				) 


def changed_industry_selection(scope, page, widget_key):
	logging.warning("changed_industry_selection")
	selected_industries = scope[widget_key]
	
	# store the selection
	scope.page[page]['selectors']['tickers'] = []
	scope.page[page]['selectors']['industries'] = selected_industries
	scope.page[page]['selectors']['market'] = None
	scope.page[page]['search_results'] = {}

	# Update the selected_tickers list
	ticker_list=[]
	for industry in selected_industries:
		tickers_in_industry_df = scope.ticker_index['df'][scope.ticker_index['df']['industry_group'] == industry ]
		tickers_in_industry_list = tickers_in_industry_df.index.tolist()
		ticker_list += tickers_in_industry_list
	ticker_list.sort()
	scope.page[page]['list_selected_tickers'] = ticker_list

	# update the list of tickers to load
	scope.page[page]['list_load_tickers'] = []
	already_loaded_list = list(scope.tickers.keys())
	for ticker in ticker_list:
		if ticker not in already_loaded_list:
			if ticker not in scope.ticker_schema['missing']['local']: # Tried and failed to load this one
				scope.page[page]['list_load_tickers'].append(ticker)



