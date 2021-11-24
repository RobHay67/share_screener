import streamlit as st

from analysis.model.analysis_df import establish_analysis_df
from charts.model.chart_df import establish_chart_df

from ticker.views.dataframes import view_ticker_data_files

from analysis.views.dataframes import view_analysis_dfs
from charts.views.dataframes import view_chart_dfs



def dataframe_status(scope, page, col5, col6):

	if page == 'multi':
		ticker_list = list(scope.ticker_data_files.keys())
	else:
		ticker_list = scope.pages[page]['ticker_list']

	# ---------------------------------------------------------------------------------
	# Determine the Loaded Ticker DataFrame Situation - all files loaded into scope.ticker_data_files 
	# ---------------------------------------------------------------------------------
	# list_of_loaded_files 	= list(scope.ticker_data_files.keys())
	no_of_loaded_files 		= len(list(scope.ticker_data_files.keys()))
	total_loaded_rows		= 0	

	# ---------------------------------------------------------------------------------
	# Determine the Analysis and Chart DataFrame Sizes
	# --------------------------------------------------------------------------------- 
	total_analysis_df_rows	= 0
	total_chart_df_rows		= 0

	for ticker in ticker_list:
		loaded_df_row_count 	= int(len(scope.ticker_data_files[ticker]))
		establish_analysis_df(scope, page, ticker, loaded_df_row_count)								# This function is cached to speed things up
		analysis_df_row_count 	= len(scope.pages[page]['analysis_df'][ticker])
		total_loaded_rows 		+= loaded_df_row_count
		total_analysis_df_rows 	+= analysis_df_row_count

		establish_chart_df(scope, page, ticker)														# Not Cached, but has some code to check when to run
		chart_df_row_count 	= len(scope.pages[page]['chart_df'][ticker])
		total_chart_df_rows += chart_df_row_count

	analysis_df_ticker_count 	= len(scope.pages[page]['analysis_df'])
	chart_df_ticker_count 		= len(scope.pages[page]['chart_df'])

	loaded_df_button_message 	= ('Loaded   dfs = ' + str(no_of_loaded_files)   		+ ' rows = ' + str(total_loaded_rows))
	analysis_df_button_message 	= ('Analysis dfs = ' + str(analysis_df_ticker_count)  	+ ' rows = ' + str(total_analysis_df_rows))
	chart_df_button_message 	= ('Charting dfs = ' + str(chart_df_ticker_count)  		+ ' rows = ' + str(total_chart_df_rows))

	with col5: show_ticker_files   	= st.button(loaded_df_button_message)
	with col5: show_analysis_dfs 	= st.button(analysis_df_button_message)
	with col5: show_chart_dfs 		= st.button(chart_df_button_message)

	
	# Render Loading and downloading messages right here

	if page != 'multi':
		# Render the Company Name
		st.header( scope.ticker_index.loc[ticker]['company_name'] )
	
	if show_ticker_files	: view_ticker_data_files(scope, page)
	if show_analysis_dfs	: view_analysis_dfs(scope, page)
	if show_chart_dfs		: view_chart_dfs(scope, page)



