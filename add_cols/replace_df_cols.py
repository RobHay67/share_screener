


def replace_page_df_columns(scope, page, ticker):

	config_group = scope.tickers[ticker][page]['config_group']
	
	scope.pages[page]['render']['verdicts'] = False
				
	if config_group != None:			
	# Some pages do not have any dataframes
		for config_key, status in scope.tickers[ticker][page]['replace_column'].items():
			if status == True:	
			# Only replace the columns if requested to do so for this column adder
				ticker_df = scope.tickers[ticker][page]['df']
				# Call the column adding function for this config_key
				scope[config_group]['config'][config_key]['add_columns']['function'](scope, config_key, ticker, ticker_df)
				# Set the status to false to prevent refreshing unnecesarily
				scope.tickers[ticker][page]['replace_column'][config_key] = False

				if config_group == 'trials':
					# set stutus to recalc overall verdict for this ticker
					scope.tickers[ticker][page]['replace_verdict'] = True
					# Store the most date recent test result - it should be the first row
					scope.tickers[ticker][page]['trials'][config_key] = ticker_df[config_key].iloc[0]


