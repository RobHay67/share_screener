from config.params.charts import chart_config
from config.params.metrics import metrics_config


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
								'add_chart_data'		: {},
								'market'				: 'select entire market', 
								'industries'			: None, 
								'tickers'				: None,  
									},
					'single'	:{
								'ticker_list'			: ['select a ticker'],
								'chart_df'				: {}, 
								'add_ohlcv_data'		: {},
								'add_metric_data'		: {},
								'add_chart_data'		: {},
								},
					'intraday'	:{
								'ticker_list'			: ['select a ticker'],
								'chart_df'				: {}, 
								'add_ohlcv_data'		: {},
								'add_metric_data'		: {},
								'add_chart_data'		: {},
								},
					'volume'	:{
								'ticker_list'			: ['select a ticker'],
								'chart_df'				: {}, 
								'add_ohlcv_data'		: {},
								'add_metric_data'		: {},
								'add_chart_data'		: {},
								},
					'research'	:{
								'ticker_list'			: ['select a ticker'],
								'chart_df'				: {}, 
								'add_ohlcv_data'		: {},
								'add_metric_data'		: {},
								'add_chart_data'		: {},
								},
					}

	





def scope_page_metrics(scope):

	screener_metrics = {}
	chart_metrics = {}

	for metric in metrics_config.keys():
		screener_metrics[metric] = metrics_config[metric]['active']


	for chart in chart_config.keys():
		# 
		if chart_config[chart]['metrics'] != None:						# Only add charts that require additional columns
																		# Many charts only use OHLCV cols so will never require metrics
			chart_metrics[chart] = chart_config[chart]['active']

	scope.page_metrics_screener = screener_metrics
	scope.page_metrics_chart = chart_metrics


