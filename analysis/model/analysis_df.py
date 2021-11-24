import streamlit as st


# from analysis.model.chart_df import create_chart_df

def establish_analysis_df(scope, page, ticker, loaded_df_row_count):

	df_row_limit = int(scope.analysis_row_limit)

	# Establish the Analysis_df for this ticker
	analysis_df = create_analysis_df(scope, page, ticker, df_row_limit, loaded_df_row_count)  
	scope.pages[scope.display_page]['analysis_df'][ticker] = analysis_df



# Cached Function - only reload when one of the following values changes
# 	ticker 				> new ticker = new df required
#	df_row_limit 		> User want a different number of rows to analyse
# 	loaded_df_row_count > User has loaded more rows, so the analysis df will need to be updated as we might have newer data


@st.cache
def create_analysis_df(scope, page, ticker, analysis_row_limit, loaded_df_row_count ):
	print ( '\033[91m' + ticker + ' > create_analysis_df has been called \033[0m')
	# the loaded_df_row_count variable is only used to trigger a new run of this code - ie prevent runs on data already loaded
	
	# print ( 'Ticker        = ', ticker)
	# print ( 'Analysis Rows = ', analysis_row_limit)
	# print ( 'Loaded   Rows = ', loaded_df_row_count)
	

	share_data = scope.ticker_data_files[ticker].copy()

	if analysis_row_limit != None:
		share_data = share_data.head(analysis_row_limit)
	
	scope.pages[page]['refresh_chart_df'] = True


	return share_data



