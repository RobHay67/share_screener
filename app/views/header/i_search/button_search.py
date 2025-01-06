
import streamlit as st


def seach_for_ticker_button(scope, page, ticker):

	widget_key = ticker + '_button'

	st.button(
				label='Choose', 
				key=widget_key,
				on_click=select_search_result_ticker,
				args=(scope, page, ticker, widget_key)
				)


def select_search_result_ticker(scope, page, ticker, widget_key):

	# set selected ticker as the target for the page
	if page == 'screener':
		scope.page[page]['selectors']['tickers'] = [ticker]
	else:
		scope.page[page]['selectors']['ticker'] = ticker

	# Clear Search Results
	scope.page[page]['search_results'] = {}
