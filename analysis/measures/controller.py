

# share_data = scope.ticker_data_files[ticker].copy()



def create_plot_df(scope, ticker ):
	print ( '\033[93mcreate_plot_df is being rebuilt - are you certain now is the time to do this ? \033[0m')

	plot_df = scope.selected[scope.display_page]['analysis_df'][ticker].copy()

	print ( 'ADD SMA and plot this on the Candlestick Chart')


	# how are we going to do this 
	# print ( scope.charts)
	# print ( scope.measures)


	print('-'*100)
	for chart in scope.charts.keys():
		if scope.charts[chart]['active'] == True:
			print ('Add Chart columns for > ', chart)

	print('-'*100)
	for measure in scope.measures.keys():
		if scope.measures[measure]['active'] == True:
			if scope.measures[measure]['params'] != None:
				print ('Add Measure columns for > ', measure)
				# page_view_map[page](st.session_state)
				scope.measures[measure]['function'](scope, plot_df, measure)

	print('='*100)
	# store the analysis_df
	scope.selected[scope.display_page]['plot_df'][ticker] = plot_df


	# after adding all the relevant measures we can reset this 
	# so this function does not get called unnecasily
	scope.rebuild_plot_df = False
