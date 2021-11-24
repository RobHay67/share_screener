

def scope_pages(scope):
	# Page Specific Variables
	scope.pages={
					'multi'		:{
								'ticker_list'			: [], 
								'analysis_df'			: {}, 
								'chart_df'				: {},
								'refresh_analysis_df'	: True,
								'refresh_chart_df'		: True, 
								'market'				: 'select entire market', 
								'industries'			: None, 
								'tickers'				: None,  
									},
					'single'	:{
								'ticker_list'			: ['select a ticker'],
								'analysis_df'			: {}, 
								'chart_df'				: {}, 
								'refresh_analysis_df'	: True,
								'refresh_chart_df'		: True,
								},
					'intraday'	:{
								'ticker_list'			: ['select a ticker'],
								'analysis_df'			: {}, 
								'chart_df'				: {}, 
								'refresh_analysis_df'	: True,
								'refresh_chart_df'		: True,
								},
					'volume'	:{
								'ticker_list'			: ['select a ticker'],
								'analysis_df'			: {}, 
								'chart_df'				: {}, 
								'refresh_analysis_df'	: True,
								'refresh_chart_df'		: True,
								},
					'research'	:{
								'ticker_list'			: ['select a ticker'],
								'analysis_df'			: {}, 
								'chart_df'				: {}, 
								'refresh_analysis_df'	: True,
								'refresh_chart_df'		: True,
								},
					}




# A refresh of the chart_df is required if :
#	1) The Analysis_df is refreshed / changed - i.e. new data downloaded
#	2) A Change has been made to the charting parameters - i.e we changed the SMA from 21 days to 7 days




