from testing.config import tests_config
from charts.config import charts_config

# TODO - whenever we add a ticker to ohlcv, we need to also add it to refresh metrics!!


def scope_pages(scope):

	scope.pages = {}

	scope.pages['row_limit'] = 100
	scope.pages['button_for_scope'] = None
	scope.pages['display_page'] = 'home_page'				# Page to display with a default for the initial first load
	scope.pages['page_list'] = list(pages_config.keys())

	
	scope_page_templates(scope)								# add this initial default state for the screener and chart metrics


	# TODO - add the page selectors right here - 
	# Need to check how they work for the single pages and combine methodology with the screener selectors


	# Scope out the Page Specific Variables
	for page, config in pages_config.items():
		scope.pages[page] = config

	# TODO scope out the screener results config - this might even need to be a level higher - not sure just yet





pages_config = {
		'single': {
					'ticker_list'			: ['select a ticker'],
					'df'					: {}, 
					'renew'					: { 
												'ticker_data':{},
												'expanders':{},
											  },
					},
		'intraday': {
					'ticker_list'			: ['select a ticker'],
					'df'					: {}, 
					'renew'					: { 
												'ticker_data':{},
												'expanders':{},
											  },
					},
		'volume': {
					'ticker_list'			: ['select a ticker'],
					'df'					: {}, 
					'renew'					: { 
												'ticker_data':{},
												'expanders':{},
											  },
					},
		'research': {
					'ticker_list'			: ['select a ticker'],
					'df'					: {}, 
					'renew'					: { 
												'ticker_data':{},
												'expanders':{},
											  },
					},
		'screener': {
					'ticker_list'			: [], 
					'df'					: {}, 
					'renew'					: { 
												'ticker_data':{},
												'expanders':{},
											  },
					'test_results'			: {},
					'test_results_df'		: {},
					'selectors'				: {
												'market'				: 'select entire market', 
												'industries'			: None, 
												'tickers'				: None,  
												}
					},
}



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
		# many charts only use OHLCV cols so will never require metrics	
		if charts_config[chart]['add_columns'] != None:
			active_status_charts[chart] = charts_config[chart]['active']
	
	scope.pages['templates']['charts'] = active_status_charts




