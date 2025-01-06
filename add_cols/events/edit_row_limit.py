

def edit_row_limit_event(scope):

	# This event is triggered when the user sets a new row limit for
	# every page - there is only a single global row limit
	#
	# page dataframes will require refreshing
	# Column  adders will require refreshing as well


	for ticker in scope.tickers.keys():
		for page in scope.pages['page_list']:

			scope.tickers[ticker][page]['replace_df'] = True

			if page == 'chart':
				scope.tickers[ticker][page]['replace_column'] = scope.charts['template_col_adders'].copy()

			if page == 'screener':
				scope.tickers[ticker][page]['replace_column'] = scope.trials['template_col_adders'].copy()







