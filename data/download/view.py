
import streamlit as st

from pages.view.three_cols import three_cols

def view_download(scope):

	# st.markdown('##### Download Variables')
	# three_cols( 'Number of Days to Download', scope.data['download']['days'], 'download_days' )

	st.markdown('##### Most Recent Download Variables and Data')
	three_cols( 'Days to Download (recent)', scope.data['download']['days'], 'download_days' )
	three_cols( 'Industry Groups for y_finance to iterate over', scope.data['download']['industries'], 'download_industries' )
	three_cols( 'Missing Ticker List', scope.data['download']['missing_list'], 'downloaded_missing_list' )
	three_cols( 'Latest Download Batch from y_finance', scope.data['download']['yf_files'], 'download_yf_files' )
	three_cols( 'Latest Error Messages from y_finance', scope.data['download']['yf_anomolies']  , 'downloaded_yf_anomolies' )






