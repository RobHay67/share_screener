from pages.view.header import render_page_title		
from pages.view.screener_example import example_settings			#TODO fleshing out some ideas
# from screener.view.buttons import execute_screening_button
from pages.screener.view.test_results import view_test_results
from pages.screener.view.tests import view_tests
from pages.picker.controller import render_ticker_picker


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Mult Ticker Analysis
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def render_screener_page(scope):
	# render_page_title(scope, 'Ticker Screener', 'screener')
	render_page_title(scope, 'Ticker Screener')

	render_ticker_picker(scope)

	# execute_screening = execute_screening_button(scope)
	
	view_test_results(scope)


	view_tests(scope)


	example_settings(scope)


	

	# TODO we migth be able to jumpt to single stock analysis from any list - that migth be cool!!!




