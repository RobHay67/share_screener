from screener.scope.model.remove_test_result import remove_test_result_column

# This event is triggered when a column adder is changed to either 
#
# Active 	(True) 
# or 
# Inactive 	(False)
#
# Column Adder require recalculation for every ticker using this test
# Column adders activated will require recalculation
# Column adders deactived need to be removed from the page_df
# Screener Page Overall Verdict will need to be re-run

def edit_active_event(scope, schema_group, schema_key, status):
	
	# Update this status in Each Page / Ticker that utilises this column adder (schema_key)
	for ticker in scope.tickers.keys():
		for page in scope.config['page_list']: 
			# if the activated column adder is used by this page then change the refresh status
			if schema_key in scope.tickers[ticker][page]['re_run_functions'].keys():
				scope.tickers[ticker][page]['re_run_functions'][schema_key] = status
				# for the screener page, remove the test result 
				# if the users has deactivated this test
				# and rerun the overall test
				if page == 'screener' and status == False:
					remove_test_result_column(scope, ticker, schema_key)
					scope.tickers[ticker][page]['verdicts']['re_run_trials'] = True

	# Update the Active lists for charts or trials
	# either add the chart or trial or remove it

	if status == True:
		# add chart or trial to active list
		scope[schema_group]['active_list'].append(schema_key)
	else:
		# remove the chart or trial from the active list
		if schema_key in scope[schema_group]['active_list']:
			scope[schema_group]['active_list'].remove(schema_key)


