

def scope_pages(scope):

	scope.page_to_display = 'home_page'				# The homepage to display on first load
													# This also stores the current active page

	# Page Specific Variables
	scope.pages={
					'screener'	:{
								'ticker_list'			: [], 
								'screener_df'			: {}, 
								'refresh_ticker_df'		: {},
								'market'				: 'select entire market', 
								'industries'			: None, 
								'tickers'				: None,  
									},
					'single'	:{
								'ticker_list'			: ['select a ticker'],
								'chart_df'				: {}, 
								'refresh_ticker_df'		: {},
								},
					'intraday'	:{
								'ticker_list'			: ['select a ticker'],
								'chart_df'				: {}, 
								'refresh_ticker_df'		: {},
								},
					'volume'	:{
								'ticker_list'			: ['select a ticker'],
								'chart_df'				: {}, 
								'refresh_ticker_df'		: {},
								},
					'research'	:{
								'ticker_list'			: ['select a ticker'],
								'chart_df'				: {}, 
								'refresh_ticker_df'		: {},
								},
					}




