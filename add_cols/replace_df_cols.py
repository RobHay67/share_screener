


def replace_page_df_columns(scope, page, ticker):

	schema_group = scope.tickers[ticker][page]['schema_group']
	
	scope.page[page]['render']['verdicts'] = False
				
	if schema_group != None:			
	# Some pages do not have any dataframes
		for schema_key, status in scope.tickers[ticker][page]['replace_column'].items():
			if status == True:	
			# Only replace the columns if requested to do so for this column adder
				ticker_df = scope.tickers[ticker][page]['df']
				# Call the column adding function for this schema_key
				scope[schema_group]['user_config'][schema_key]['add_columns']['function'](scope, schema_key, ticker, ticker_df)
				# Set the status to false to prevent refreshing unnecesarily
				scope.tickers[ticker][page]['replace_column'][schema_key] = False

				if schema_group == 'trials':
					# set stutus to recalc overall verdict for this ticker
					scope.tickers[ticker][page]['replace_verdict'] = True
					# Store the most date recent test result - it should be the first row
					scope.tickers[ticker][page]['trials'][schema_key] = ticker_df[schema_key].iloc[0]


