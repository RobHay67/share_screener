

def scope_pages(scope):
	# Page Specific Variables
	scope.selected={
					'multi'		:{'ticker_list':[]				   , 'analysis_df':{},				'market':'select entire market', 'industries':None, 'tickers':None,   	},
					'single'	:{'ticker_list':['select a ticker'], 'analysis_df':{}, 'chart_df':{}, 																		},
					'intraday'	:{'ticker_list':['select a ticker'], 'analysis_df':{}, 'chart_df':{}, 																		},
					'volume'	:{'ticker_list':['select a ticker'], 'analysis_df':{}, 'chart_df':{}, 																		},
					'research'	:{'ticker_list':['select a ticker'], 'analysis_df':{}, 'chart_df':{}, 																		},
					}
