from testing.config import tests_config
from charts.config import charts_config

# TODO - whenever we add a ticker to ohlcv, we need to also add it to refresh metrics!!


def scope_pages(scope):

	scope.pages = {}

	scope.pages['row_limit'] = 100
	scope.pages['button_for_scope'] = None
	scope.pages['display_page'] = 'home_page'				# Page to display with a default for the initial first load
	scope.pages['page_list'] = list(pages_config.keys())

	scope.pages['templates'] = {}
	scope_page_templates(scope)								# add this initial default state for the screener and chart metrics

	# Actual View Page Specific Variables
	for page, config in pages_config.items():
		scope.pages[page] = config




pages_config = {
		'single': {
					'ticker_list'			: ['select a ticker'],
					'chart_df'				: {}, 
					'refresh_df'			: { 
												'ohlcv':{},
												'charts':{},
											  },
					},
		'intraday': {
					'ticker_list'			: ['select a ticker'],
					'chart_df'				: {}, 
					'refresh_df'			: { 
												'ohlcv':{},
												'charts':{},
											  },
					},
		'volume': {
					'ticker_list'			: ['select a ticker'],
					'chart_df'				: {}, 
					'refresh_df'			: { 
												'ohlcv':{},
												'charts':{},
											  },
					},
		'research': {
					'ticker_list'			: ['select a ticker'],
					'chart_df'				: {}, 
					'refresh_df'			: { 
												'ohlcv':{},
												'charts':{},
											  },
					},
		'screener': {
					'ticker_list'			: [], 
					'screener_df'			: {}, 
					'refresh_df'			: { 
												'ohlcv':{},
												'tests':{},
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
	# Construct a template (dict) of each metric and chart that require additional columns and 
	# store as templates to be used later by for other functions.
	#
	# this greatly simplifies those later functions - which can quickly refer to a single object.


	metric_active_status = {}
	chart_active_status = {}

	for metric in tests_config.keys():
		metric_active_status[metric] = tests_config[metric]['active']


	for chart in charts_config.keys():
		if charts_config[chart]['metrics'] != None:						# Only add charts that require additional columns
																		# Many charts only use OHLCV cols so will never require metrics
			chart_active_status[chart] = charts_config[chart]['active']

	scope.pages['templates']['tests'] = metric_active_status
	scope.pages['templates']['charts'] = chart_active_status




