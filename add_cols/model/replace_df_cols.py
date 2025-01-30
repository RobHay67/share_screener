


def replace_page_df_columns(scope, page, ticker):

	schema_group = scope.tickers[ticker][page]['schema_group']
	ticker_for_page = scope.tickers[ticker][page]
	# 
				
	# Some pages do not have any dataframes
	# This can be checked if the schema group has been assigned or not
	if schema_group != None:			
		
		# Iterate through each column adder for the page
		for schema_key, replace_column_adder in ticker_for_page['re_run_functions'].items():
			
			# Only replace the columns if requested to do so for 
			# this particular column adder
			if replace_column_adder == True:	
			
				# print('Replacing the Page Ticker df columns     Page = ',page, 'ticker = ', ticker)
				
				ticker_df = ticker_for_page['df']
				
				# Call the column adding function for this schema_key
				# This function will also remove any previous columns


				scope[schema_group]['user_config'][schema_key]['function']['function'](scope, schema_key, ticker, ticker_df)
				
				# Set the re_run_functions status to false 
				# to prevent refreshing unnecesarily
				ticker_for_page['re_run_functions'][schema_key] = False


				if schema_group == 'trials':
					# set stutus to recalc overall verdict for this ticker
					ticker_for_page['verdicts']['re_run_trials'] = True


					# Store the most date recent test result - it should be the first row				
					ticker_for_page['verdicts']['trial_verdicts'][schema_key] = ticker_df[schema_key].iloc[0]


