def create_analysis_df(scope, ticker_list):

	page 				= scope.page_to_display
	analysis_row_limit 	= int(scope.analysis_row_limit)
	refresh_analysis_df = scope.pages[page]['refresh_analysis_df']

	# so we only refresh if we have been asked to
	if refresh_analysis_df == True:
		for ticker in ticker_list:
			print ( '\033[93m' + ticker + ' > create_analysis_df\033[0m')

			if ticker in scope.ticker_data_files:
				analysis_df = scope.ticker_data_files[ticker].copy()

				# limit analysis to user specified row limit
				if analysis_row_limit != None : analysis_df = analysis_df.head(analysis_row_limit) 
				
				# store the new analysis_df
				scope.pages[page]['analysis_df'][ticker] = analysis_df

				# reset STATUS to prevent unnecesary updates
				scope.pages[page]['refresh_analysis_df'] 	= False
				scope.pages[page]['refresh_chart_df'] 		= True
	# else:
	# 	print ( '\033[92m' + 'create_analysis_df is NOT being re-run\033[0m')




