import streamlit as st




def establish_analysis_df(scope, ticker, no_of_loaded_rows):

	df_row_limit = int(scope.analysis_row_limit)

	analysis_df = create_analysis_df(scope, ticker, df_row_limit, no_of_loaded_rows)  

	# store the analysis_df
	scope.selected[scope.display_page]['analysis_df'][ticker] = analysis_df



# Cached Function - only reload when one of the following values changes
# 	ticker 				> new ticker = new df required
#	df_row_limit 		> User want a different number of rows to analyse
# 	no_of_loaded_rows 	> User has loaded more rows, so the analysis df will need to be updated as we might have newer data


@st.cache
def create_analysis_df(scope, ticker, analysis_row_limit, no_of_loaded_rows ):
	print ( '\033[96mcreate_analysis_df has been called - is this ok? \033[0m')

	share_data = scope.ticker_data_files[ticker].copy()

	if analysis_row_limit != None:
		# share_data.sort_values(by=['date'], inplace=True, ascending=True)
		share_data = share_data.head(analysis_row_limit)
	
	# System flag to indication that the plot_df will require a rebuild 
	# because we have changed the analysis_df on which it is based.
	scope.rebuild_plot_df = True

	return share_data



