from pages.ticker_loader.header import render_page_title		
from pages.ticker_loader.controller import render_ticker_loader
from pages.screener.results import render_test_results
from pages.screener.tests import render_screener_tests

from pages.ticker_loader.search_results import render_search_results


from pages.screener.screener_example import example_settings			#TODO fleshing out some ideas - delete when happy


def render_screener_page(scope):

	render_page_title(scope, 'Ticker Screener')

	render_ticker_loader(scope)
	

	if len(scope.pages['screener']['search_results']) == 0:

		render_test_results(scope)

		render_screener_tests(scope)

		example_settings(scope)
	
	else:

		render_search_results(scope)

	# TODO we want to be able to jumpt to single stock analysis from any list - that migth be cool!!!
