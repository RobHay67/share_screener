import streamlit as st

from views.scope_var import three_cols





def view_download(scope):

	# st.markdown('##### Download Variables')
	# three_cols( 'Number of Days to Download', scope.download_days, 'download_days' )

	st.markdown('##### Most Recent Download Variables and Data')
	three_cols( 'Days to Download (recent)', scope.download_days, 'download_days' )
	three_cols( 'Industry Groups for y_finance to iterate over', scope.download_industries, 'download_industries' )
	three_cols( 'Loaded Ticker List', scope.downloaded_loaded_list, 'downloaded_loaded_list' )
	three_cols( 'Missing Ticker List', scope.downloaded_missing_list, 'downloaded_missing_list' )
	three_cols( 'Latest Download Batch from y_finance', scope.download_yf_files, 'download_yf_files' )
	three_cols( 'Latest Error Messages from y_finance', scope.downloaded_yf_anomolies  , 'downloaded_yf_anomolies' )




def set_download_days(scope):
	previous_selection = int(scope.download_days)

	input_download_days = st.number_input( 
											'Days to Download (recent)', 
											min_value=1, 
											value=previous_selection, 						# Default Value to display (would revert on every second try)
											key='97'
											)

	input_download_days = int(input_download_days)

	if input_download_days != previous_selection:
		scope.download_days = input_download_days
