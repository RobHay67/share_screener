from config.params.charts import chart_config
from config.params.metrics import metrics_config




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
								'refresh_ticker_data'	: {},
								'refresh_metrics'		: {},
								'market'				: 'select entire market', 
								'industries'			: None, 
								'tickers'				: None,  
									},
					'single'	:{
								'ticker_list'			: ['select a ticker'],
								'chart_df'				: {}, 
								'refresh_ticker_data'	: {},
								'refresh_metrics'		: {},
								},
					'intraday'	:{
								'ticker_list'			: ['select a ticker'],
								'chart_df'				: {}, 
								'refresh_ticker_data'	: {},
								'refresh_metrics'		: {},
								},
					'volume'	:{
								'ticker_list'			: ['select a ticker'],
								'chart_df'				: {}, 
								'refresh_ticker_data'	: {},
								'refresh_metrics'		: {},
								},
					'research'	:{
								'ticker_list'			: ['select a ticker'],
								'chart_df'				: {}, 
								'refresh_ticker_data'	: {},
								'refresh_metrics'		: {},
								},
					}

	





def scope_page_metrics(scope):

	screener_metrics = {}
	chart_metrics = {}

	for metric in metrics_config.keys():
		screener_metrics[metric] = metrics_config[metric]['active']


	for chart in chart_config.keys():
		# Only add charts that require additional columns
		# Many of the charts just use the OHLCV columns so will not require recalculation of their metrics
		if chart_config[chart]['metrics'] != None:
			chart_metrics[chart] = chart_config[chart]['active']

	scope.page_metrics_screener = screener_metrics
	scope.page_metrics_chart = chart_metrics




