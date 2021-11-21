import streamlit as st


# from analysis.model.chart_df import create_chart_df

def establish_analysis_df(scope, ticker, no_of_loaded_rows):

	df_row_limit = int(scope.analysis_row_limit)

	# Establish the Analysis_df for this ticker
	analysis_df = create_analysis_df(scope, ticker, df_row_limit, no_of_loaded_rows)  
	scope.selected[scope.display_page]['analysis_df'][ticker] = analysis_df



# Cached Function - only reload when one of the following values changes
# 	ticker 				> new ticker = new df required
#	df_row_limit 		> User want a different number of rows to analyse
# 	no_of_loaded_rows 	> User has loaded more rows, so the analysis df will need to be updated as we might have newer data


@st.cache
def create_analysis_df(scope, ticker, analysis_row_limit, no_of_loaded_rows ):
	print ( '\033[91m' + ticker + ' > create_analysis_df has been called \033[0m')
	# print ( 'Ticker        = ', ticker)
	# print ( 'Analysis Rows = ', analysis_row_limit)
	# print ( 'Loaded   Rows = ', no_of_loaded_rows)
	

	share_data = scope.ticker_data_files[ticker].copy()

	if analysis_row_limit != None:
		share_data = share_data.head(analysis_row_limit)
	
	return share_data



