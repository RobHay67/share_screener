


def replace_page_df_columns(scope, page, ticker):

	schema_group = scope.tickers[ticker][page]['schema_group']
	page_ticker = scope.tickers[ticker][page]
	# 
				
	# Some pages do not have any dataframes
	# This can be checked if the schema group has been assigned or not
	if schema_group != None:			
		
		# Iterate through each column adder for the page
		for schema_key, replace_column_adder in page_ticker['replace_column_adder'].items():
			
			# Only replace the columns if requested to do so for 
			# this particular column adder
			if replace_column_adder == True:	
			
				
				ticker_df = page_ticker['df']
				
				# Call the column adding function for this schema_key
				# This function will also remove any previous columns


				scope[schema_group]['user_config'][schema_key]['function']['function'](scope, schema_key, ticker, ticker_df)
				
				# Set the replace_column_adder status to false 
				# to prevent refreshing unnecesarily
				page_ticker['replace_column_adder'][schema_key] = False


				if schema_group == 'trials':
					# set stutus to recalc overall verdict for this ticker
					page_ticker['verdicts']['replace_verdict'] = True


					# Store the most date recent test result - it should be the first row				
					page_ticker['verdicts']['trials'][schema_key] = ticker_df[schema_key].iloc[0]


