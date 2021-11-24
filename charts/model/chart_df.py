import streamlit as st

# @st.cache 																								# handle refresh with code - value in scope.pages[page]['refresh_chart_df]
def establish_chart_df(scope, page, ticker):

	if scope.pages[page]['refresh_chart_df'] == True:

		print ( '\033[93m' + ticker + ' > establish_chart_df is being rebuilt \033[0m')

		chart_df = scope.pages[scope.display_page]['analysis_df'][ticker].copy()
		chart_df.sort_values(by=['date'], inplace=True, ascending=True)		

		for chart in scope.charts.keys():																	# Check if need additional columns for any selected charts
			if scope.charts[chart]['active'] == True:														# User has selected to display this chart
				if scope.charts[chart]['data_cols'] != None:												# This chart has additional columns (config contain the column details)
					scope.charts[chart]['data_cols']['function'](scope, chart_df, chart)					# Execute the column adding function
	
		
		scope.pages[scope.display_page]['chart_df'][ticker] = chart_df									# store the chart_df along with any additional columns that have been added
		scope.pages[page]['refresh_chart_df'] = False													# Refresh performed, prevent running a second time until required
	else:
		print ( '\033[92m' + ticker + ' > establish_chart_df is NOT being rebuilt \033[0m')


