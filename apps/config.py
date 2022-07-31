from tests.config import tests_config
from charts.config import charts_config




def scope_apps(scope):

	scope.apps = {}

	scope.apps['row_limit'] = 100
	scope.apps['button_for_scope'] = None
	scope.apps['display_app'] = 'login'					# app to display with a default for the initial first load
	scope.apps['app_list'] = ['single', 'intraday', 'volume', 'research', 'screener']
	
	
	scope_page_templates(scope)								# add this initial default state for the screener and chart pages

	# ==========================================
	# app Specific Configuration
	for app in scope.apps['app_list']:
		scope.apps[app] = {}
		scope.apps[app]['search_results'] = {}  # TODO - should this be here - isnt it in config or somewhere else
		scope.apps[app]['ticker_list'] = []
		scope.apps[app]['replace_dfs'] = {}
		scope.apps[app]['replace_cols'] = {}

		# TODO - move this back to the data modile
		scope.apps[app]['dfs'] = {}
		scope.apps[app]['data'] = {}
		scope.apps[app]['selectors'] = {
											'market'	: 'select entire market', 
											'industries': [],
											'tickers'	: [],
											'ticker'	: 'select a ticker',
											}

	# Store any test results (from the screner app) in these objects
	scope.apps['tests'] = {}
	scope.apps['tests']['results'] = {}
	scope.apps['tests']['df'] = {}




def scope_page_templates(scope):

	# Construct a template (dict) of each test and chart that require additional columns
	# and store as templates to be used by subsequent functions.
	# This significantly simplifies later processs which can just refer to these
	# dictionaries to understand what needs to be update or not


	scope.apps['templates'] = {}


	# -------------------------------------------------------------------------
	# Tests
	# determine the active status of each test in the tests_config dictionary

	active_status_tests = {}

	# iterate through each test in the scope

	for test in tests_config.keys():
		active_status_tests[test] = tests_config[test]['active']
	
	# Update Templates for each app with the default status - this will be over-ridden by the user settings
	scope.apps['templates']['tests'] = active_status_tests



	# -------------------------------------------------------------------------
	# Charts
	# determine the active status of each chart in the charts_config dictionary

	active_status_charts = {}

	for chart in charts_config.keys():
		# check that the chart requires addional columns 
		# ( many charts only use OHLCV cols so will never require additional columns )
		if charts_config[chart]['add_columns'] != None:
			active_status_charts[chart] = charts_config[chart]['active']
	
	# Update Templates for each app with the default status - this will be over-ridden by the user settings
	scope.apps['templates']['charts'] = active_status_charts





