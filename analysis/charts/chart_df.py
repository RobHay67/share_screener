

#@st.cache - I dont think we need to do this as its handled by code?? - Not sure if we change screen though!
def create_chart_df(scope, ticker ):
	print ( '\033[93mcreate_chart_df is being rebuilt - are you certain now is the time to do this ? \033[0m')

	chart_df = scope.selected[scope.display_page]['analysis_df'][ticker].copy()
	chart_df.sort_values(by=['date'], inplace=True, ascending=True)	

	for chart in scope.charts.keys():
		if scope.charts[chart]['active'] == True and scope.charts[chart]['data_cols'] != None:		# chart / overlay is requested AND there appears to be a data column spec to render
			print ('<create_chart_df> Add Data Columns for requested chart or overlay = ', chart)
			if scope.charts[chart]['data_cols']['function'] != None:								# TODO - remove this after add everything
				scope.charts[chart]['data_cols']['function'](scope, chart_df, chart)
			else:
				print( '\033[91mFunction has not yet been defined for this Chart\033[0m')
 
	# store the analysis_df
	scope.selected[scope.display_page]['chart_df'][ticker] = chart_df

	# Prevent the Function from Running Multiple Times
	# so this function does not get called when we already have done the work
	scope.rebuild_chart_df = False
