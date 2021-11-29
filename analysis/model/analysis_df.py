def create_analysis_df(scope, ticker_list):

	page 				= scope.page_to_display
	analysis_row_limit 	= int(scope.analysis_row_limit)

	# so we only refresh if we have been asked to
	for ticker in ticker_list:
		if scope.pages[page]['refresh_analysis_df'][ticker] == True:
			if ticker in scope.ticker_data_files:
				print ( '\033[93m' + ticker + ' < create_analysis_df > adding ticker to analysis_df for page \033[0m')
				analysis_df = scope.ticker_data_files[ticker].copy()

				# limit analysis to user specified row limit
				if analysis_row_limit != None : analysis_df = analysis_df.head(analysis_row_limit) 
				
				# store the new analysis_df
				scope.pages[page]['analysis_df'][ticker] = analysis_df

				# reset STATUS to prevent unnecesary updates
				scope.pages[page]['refresh_analysis_df'][ticker] 	= False
				scope.pages[page]['refresh_chart_df'][ticker] 		= True
			else:
				print ( '\033[91m' + ticker + ' < create_analysis_df > ticker file missing from scope.ticker_data_files\033[0m')
		else:
				print ( '\033[92m' + ticker + ' < create_analysis_df > refresh not requested\033[0m')




