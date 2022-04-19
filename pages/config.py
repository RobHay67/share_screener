# from config.tests import tests_config
from config.tests.config import tests_config
from charts.config import charts_config

# TODO - whenever we add a ticker to ohlcv, we need to also add it to refresh add_cols!!


def scope_pages(scope):

	scope.pages = {}

	scope.pages['row_limit'] = 100
	scope.pages['button_for_scope'] = None
	scope.pages['display_page'] = 'home_page'				# Page to display with a default for the initial first load
	scope.pages['page_list'] = pages

	
	scope_page_templates(scope)								# add this initial default state for the screener and chart pages

	# ==========================================
	# Page Specific Configuration
	for page in pages:
		print(page)
		scope.pages[page] = {}
		# scope.pages[page]['ticker_list'] = ['select a ticker'] if page != 'screener' else []
		scope.pages[page]['ticker_list'] = []
		scope.pages[page]['replace_df'] = {}
		scope.pages[page]['column_adders'] = {}
		scope.pages[page]['dfs'] = {}
		# scope.pages[page]['data'] = {
		# 									'df'		: {},
		# 									'renew_df'	: {},
		# 									'expanders'	: {},
		# 								}
		scope.pages[page]['data'] = {}



		# scope.pages[page]['tickers']['df'] = {}
		# scope.pages[page]['renew'] = { 
		# 								'ticker_data'	: {},
		# 								'expanders'		: {},
		# 								}
		scope.pages[page]['selectors'] = {
											'market'	: 'select entire market', 
											'industries': [],
											'tickers'	: [],
											'ticker'	: 'select a ticker',
											}

	# Store any test results (from the screner page) in these objects
	scope.pages['tests'] = {}
	scope.pages['tests']['results'] = {}
	scope.pages['tests']['df'] = {}


pages = ['single', 'intraday', 'volume', 'research', 'screener']



def scope_page_templates(scope):

	# Construct a template (dict) of each test and chart that require additional columns
	# and store as templates to be used by subsequent functions.
	# This significantly simplifies later processs which can just refer to these
	# dictionaries to understand what needs to be update or not


	scope.pages['templates'] = {}


	# -------------------------------------------------------------------------
	# Tests
	# determine the active status of each test in the tests_config dictionary

	active_status_tests = {}

	for test in tests_config.keys():
		active_status_tests[test] = tests_config[test]['active']
	
	scope.pages['templates']['tests'] = active_status_tests



	# -------------------------------------------------------------------------
	# Charts
	# determine the active status of each chart in the charts_config dictionary

	active_status_charts = {}

	for chart in charts_config.keys():
		# check that the chart requires addional columns 
		# many charts only use OHLCV cols so will never require additional columns	
		if charts_config[chart]['add_columns'] != None:
			active_status_charts[chart] = charts_config[chart]['active']
	
	scope.pages['templates']['charts'] = active_status_charts




