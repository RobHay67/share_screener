
import streamlit as st


def ticker_button(scope, page, ticker):

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
		scope.pages[page]['selectors']['tickers'] = [ticker]
	else:
		scope.pages[page]['selectors']['ticker'] = ticker

	# Clear Search Results
	scope.pages[page]['search_results'] = {}
