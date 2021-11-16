import streamlit as st


from system.view import view_3_columns



def scope_download(scope):
	# Download Ticker Variables
	# scope.download_days 			= 5  # now in user settings
	scope.download_industries 		= []
	scope.download_yf_files			= {}
	scope.downloaded_loaded_list 	= []
	scope.downloaded_missing_list 	= []
	scope.downloaded_yf_anomolies 	= {}


def view_download(scope):

	# st.markdown('##### Download Variables')
	# view_3_columns( 'Number of Days to Download', scope.download_days, 'download_days' )

	st.markdown('##### Most Recent Download Variables and Data')
	view_3_columns( 'Industry Groups for y_finance to iterate over', scope.download_industries, 'download_industries' )
	view_3_columns( 'Loaded Ticker List', scope.downloaded_loaded_list, 'downloaded_loaded_list' )
	view_3_columns( 'Missing Ticker List', scope.downloaded_missing_list, 'downloaded_missing_list' )
	view_3_columns( 'Latest Download Batch from y_finance', scope.download_yf_files, 'download_yf_files' )
	view_3_columns( 'Latest Error Messages from y_finance', scope.downloaded_yf_anomolies  , 'downloaded_yf_anomolies' )



