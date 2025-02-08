
import logging
import streamlit as st


def button_select_seach_result_ticker(scope, page, ticker):
	logging.debug("button_select_seach_result_ticker")
	widget_key = 'widget_button_' + ticker

	st.button(
				label='Choose', 
				key=widget_key,
				on_click=clicked_search_result_ticker,
				args=(scope, page, ticker, widget_key)
				)


def clicked_search_result_ticker(scope, page, ticker, widget_key):
	logging.warning(f"clicked_search_result_ticker {ticker=}")
	# set selected ticker as the target for the page
	if page == 'screener':
		scope.page[page]['selectors']['tickers'] = [ticker]
	else:
		scope.page[page]['selectors']['ticker'] = ticker

	# Clear Search Results
	scope.page[page]['search_results'] = {}
