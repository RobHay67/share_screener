import streamlit as st

# @st.cache 
def create_chart_df(scope, ticker):
	print ( '\033[93m' + ticker + ' > create_chart_df is being rebuilt \033[0m')

	chart_df = scope.selected[scope.display_page]['analysis_df'][ticker].copy()
	chart_df.sort_values(by=['date'], inplace=True, ascending=True)		

	for chart in scope.charts.keys():																	# Check if need additional columns for any selected charts
		if scope.charts[chart]['active'] == True:														# User has selected to display this chart
			if scope.charts[chart]['data_cols'] != None:												# This chart has additional columns (config contain the column details)
				scope.charts[chart]['data_cols']['function'](scope, chart_df, chart)					# Execute the column adding functin
 
	# store the chart_df along with any additional columns that have been added
	scope.selected[scope.display_page]['chart_df'][ticker] = chart_df

