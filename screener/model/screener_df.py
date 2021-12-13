def create_screener_df(scope, ticker_list):

	page 				= scope.page_to_display
	analysis_row_limit 	= int(scope.analysis_row_limit)

	# so we only refresh if we have been asked to
	if page == 'screener':
		for ticker in ticker_list:
			if scope.pages[page]['refresh_ticker_df'][ticker] == True:
				if ticker in scope.ticker_data_files:
					print ( '\033[93m' + ticker + ' < create_screener_df > adding ticker to screener_df for page = ' + page + '\033[0m')
					screener_df = scope.ticker_data_files[ticker].copy()

					# limit analysis to user specified row limit
					if analysis_row_limit != None : screener_df = screener_df.head(analysis_row_limit) 
					
					# store the new screener_df
					scope.pages[page]['screener_df'][ticker] = screener_df

					# reset STATUS to prevent unnecesary updates
					scope.pages[page]['refresh_ticker_df'][ticker] 	= False
				else:
					print ( '\033[91m' + ticker + ' < create_screener_df > ticker file missing from scope.ticker_data_files\033[0m')
			else:
					print ( '\033[92m' + ticker + ' < create_screener_df > refresh not requested\033[0m')




