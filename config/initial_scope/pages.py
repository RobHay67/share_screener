

def scope_pages(scope):

	scope.page_to_display = 'home_page'				# The homepage to display on first load
													# This also stores the current active page

	# Page Specific Variables
	scope.pages={
					'screener'	:{
								'ticker_list'			: [], 
								'analysis_df'			: {}, 
								'chart_df'				: {},
								'refresh_analysis_df'	: {},
								'refresh_chart_df'		: {}, 
								'market'				: 'select entire market', 
								'industries'			: None, 
								'tickers'				: None,  
									},
					'single'	:{
								'ticker_list'			: ['select a ticker'],
								'analysis_df'			: {}, 
								'chart_df'				: {}, 
								'refresh_analysis_df'	: {},
								'refresh_chart_df'		: {},
								},
					'intraday'	:{
								'ticker_list'			: ['select a ticker'],
								'analysis_df'			: {}, 
								'chart_df'				: {}, 
								'refresh_analysis_df'	: {},
								'refresh_chart_df'		: {},
								},
					'volume'	:{
								'ticker_list'			: ['select a ticker'],
								'analysis_df'			: {}, 
								'chart_df'				: {}, 
								'refresh_analysis_df'	: {},
								'refresh_chart_df'		: {},
								},
					'research'	:{
								'ticker_list'			: ['select a ticker'],
								'analysis_df'			: {}, 
								'chart_df'				: {}, 
								'refresh_analysis_df'	: {},
								'refresh_chart_df'		: {},
								},
					}




