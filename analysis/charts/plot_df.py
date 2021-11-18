







def create_plot_df(scope, ticker ):
	print ( '\033[93mcreate_plot_df is being rebuilt - are you certain now is the time to do this ? \033[0m')

	plot_df = scope.selected[scope.display_page]['analysis_df'][ticker].copy()
	plot_df.sort_values(by=['date'], inplace=True, ascending=True)	

	print('-'*100)
	for chart in scope.charts.keys():
		if scope.charts[chart]['active'] == True:
			print ('Add Chart columns for > ', chart)
			if scope.charts[chart]['function'] != None:					# TODO - remove this after add everything
				scope.charts[chart]['function'](scope, plot_df, chart)
			else:
					print( '\033[91mFunction has not yet been defined for this Chart\033[0m')
	print('-'*100)
	for measure in scope.measures.keys():
		if scope.measures[measure]['active'] == True:
			if scope.measures[measure]['params'] != None:
				print ('Add Measure columns for > ', measure)
				if scope.measures[measure]['function'] != None:					# TODO - remove this after add everything
					scope.measures[measure]['function'](scope, plot_df, measure)
				else:
					print( '\033[91mFunction has not yet been defined for this measure\033[0m')
# 
	# store the analysis_df
	scope.selected[scope.display_page]['plot_df'][ticker] = plot_df


	# after adding all the relevant measures we can reset this 
	# so this function does not get called unnecasily
	scope.rebuild_plot_df = False
