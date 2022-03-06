from metrics.config import metrics_config
from charts.config import chart_config

# TODO - whenever we add a ticker to add_ohlcv_data, we need to also add it to refresh metrics!!




def scope_pages(scope):

	scope.page_to_display = 'home_page'				# The homepage to display on first load
													# This also stores the current active page
	scope.page_row_limit = 100

	scope_page_metrics(scope)						# add this initial default state for the screener and chart metrics

	# Page Specific Variables
	scope.pages={
					'screener'	:{
								'ticker_list'			: [], 
								'screener_df'			: {}, 
								'add_ohlcv_data'		: {},
								'add_metric_data'		: {},
								# 'add_chart_data'		: {},
								'market'				: 'select entire market', 
								'industries'			: None, 
								'tickers'				: None,  
									},
					'single'	:{
								'ticker_list'			: ['select a ticker'],
								'chart_df'				: {}, 
								'add_ohlcv_data'		: {},
								# 'add_metric_data'		: {},
								'add_chart_data'		: {},
								},
					'intraday'	:{
								'ticker_list'			: ['select a ticker'],
								'chart_df'				: {}, 
								'add_ohlcv_data'		: {},
								# 'add_metric_data'		: {},
								'add_chart_data'		: {},
								},
					'volume'	:{
								'ticker_list'			: ['select a ticker'],
								'chart_df'				: {}, 
								'add_ohlcv_data'		: {},
								# 'add_metric_data'		: {},
								'add_chart_data'		: {},
								},
					'research'	:{
								'ticker_list'			: ['select a ticker'],
								'chart_df'				: {}, 
								'add_ohlcv_data'		: {},
								# 'add_metric_data'		: {},
								'add_chart_data'		: {},
								},
					}

	





def scope_page_metrics(scope):
	# Construct a template (dict) of each metric and chart that require additional columns and 
	# store as templates to be used later by for other functions.
	#
	# this greatly simplifies those later functions - which can quickly refer to a single object.


	metric_active_status = {}
	chart_active_status = {}

	for metric in metrics_config.keys():
		metric_active_status[metric] = metrics_config[metric]['active']


	for chart in chart_config.keys():
		if chart_config[chart]['metrics'] != None:						# Only add charts that require additional columns
																		# Many charts only use OHLCV cols so will never require metrics
			chart_active_status[chart] = chart_config[chart]['active']

	scope.pages_template_add_metric_data = metric_active_status
	scope.pages_template_add_chart_data = chart_active_status


