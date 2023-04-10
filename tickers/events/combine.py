




def combine_event(scope, ticker):

	# This event is triggered when new ticker data has been successfully downloaded
	# and combined with the existing loaded date
	# page dataframes will require replacement
	# Column adders will need to be recalculatd as well

	for page in scope.pages['page_list']:

		scope.tickers[ticker][page]['replace_df'] = True

		if page == 'chart':
			scope.tickers[ticker][page]['column_adders'] = scope.chart_settings['column_adders'].copy()

		if page == 'screener':
			scope.tickers[ticker][page]['column_adders'] = scope.trial_settings['column_adders'].copy()




