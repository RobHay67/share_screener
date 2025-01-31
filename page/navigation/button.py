import logging
import streamlit as st


def button_page_link(scope, page, ticker):
	logging.debug("button_page_link")
	widget_key = 'widget_navigate_to_' + page + '_page_for_' + ticker

	if st.button(
				label=scope.config['page_schema'][page]['icon'],
				key=widget_key,
				use_container_width=True,
				type='secondary',
				):
		
		match page:
			case 'screener':
				scope.page[page]['selectors']['tickers'] = [ticker]
				scope.page[page]['selectors']['industries'] = []
				scope.page[page]['selectors']['market'] = 'select market'
				scope.page[page]['search_results'] = {}	
			case _:
				scope.page[page]['selectors']['ticker'] = ticker
		
		st.switch_page(scope.config['page_schema'][page]['path'])
	


