

def scope_pages(scope):
	# Page Specific Variables
	scope.selected={
					'multi'		:{'analysis_df':{}, 'ticker_list':[], 				'market':'select entire market', 'industries':None, 'tickers':None  },
					'single'	:{'analysis_df':{}, 'ticker_list':['select a ticker']},
					'intraday'	:{'analysis_df':{}, 'ticker_list':['select a ticker']},
					'volume'	:{'analysis_df':{}, 'ticker_list':['select a ticker']},
					'research'	:{'analysis_df':{}, 'ticker_list':['select a ticker']},
					}
