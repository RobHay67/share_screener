from pages.view.header import render_page_title		
from pages.picker.controller import render_ticker_picker
from pages.screener.results import render_test_results
from pages.screener.tests import render_screener_tests



from pages.view.screener_example import example_settings			#TODO fleshing out some ideas - delete when happy


def render_screener_page(scope):

	render_page_title(scope, 'Ticker Screener')

	render_ticker_picker(scope)
	
	render_test_results(scope)

	render_screener_tests(scope)


	# TODO we want to be able to jumpt to single stock analysis from any list - that migth be cool!!!

	example_settings(scope)
	
