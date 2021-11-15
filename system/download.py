import streamlit as st


from system.reports import render_3_columns



def scope_download(scope):
	# Download Ticker Variables
	scope.download_days 			= 5
	scope.download_industries 		= []
	scope.download_yf_files			= {}
	scope.downloaded_loaded_list 	= []
	scope.downloaded_missing_list 	= []
	scope.downloaded_yf_anomolies 	= {}


def render_download(scope):

	st.markdown('##### Download Variables')
	render_3_columns( 'Number of Days to Download', scope.download_days, 'download_days' )

	st.markdown('##### Most Recent Download Variables and Data')
	render_3_columns( 'Industry Groups for y_finance to iterate over', scope.download_industries, 'download_industries' )
	render_3_columns( 'Loaded Ticker List', scope.downloaded_loaded_list, 'downloaded_loaded_list' )
	render_3_columns( 'Missing Ticker List', scope.downloaded_missing_list, 'downloaded_missing_list' )
	render_3_columns( 'Latest Download Batch from y_finance', scope.download_yf_files, 'download_yf_files' )
	render_3_columns( 'Latest Error Messages from y_finance', scope.downloaded_yf_anomolies  , 'downloaded_yf_anomolies' )



def render_download_days(scope):

	previous_selection = int(scope.download_days)

	input_download_days = st.number_input( 
											'Number of most recent business days to download from Y_Finance', 
											min_value=1, 
											# max_value=6000, 
											value=previous_selection, 						# Default Value to display (would revert on every second try)
											key='97'
											)   

	# Store the selection for smoother transition between pages
	scope.download_days = input_download_days