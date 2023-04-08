
import streamlit as st

from pages.config.three_cols import three_cols



def view_download(scope):


	st.subheader('Download Configuration')
	three_cols( 'Download Variables stored in', {}, 'scope.download', widget_type='string' )

	# st.subheader('Most Recent Download Variables and Data')
	st.subheader('Download Days')
	three_cols( 'Days to Download (recent)', scope.download['days'], 'scope.download.days' )
	three_cols( 'Days to Download (yfinance format)', scope.download['yf_period'], 'scope.download.yf_period' )
	
	st.subheader('yFinance Batch Download Variables')
	three_cols( 'Industry Groups for iteration', scope.download['yf_download_these_industries'], 'scope.download.yf_download_these_industries',  widget_type='selectbox')
	three_cols( 'Type', scope.download['yf_batch_type'], 'scope.download.yf_batch_type' )
	three_cols( 'Batch Number', scope.download['yf_batch_no'], 'scope.download.yf_batch_no' )
	three_cols( 'Industry', scope.download['yf_batch_industry'], 'scope.download.yf_batch_industry' )
	three_cols( 'Ticker String', scope.download['yf_batch_ticker_string'], 'scope.download.yf_batch_ticker_string' )
	three_cols( 'Data', scope.download['yf_batch_data'], 'scope.download.yf_batch_data' )
	three_cols( 'Errors', scope.download['yf_batch_errors'], 'scope.download.yf_batch_errors' )
	
	
	st.subheader('Batch Download Variables')
	three_cols( 'Ticker List', scope.download['yf_ticker_list'], 'scope.download.yf_data' )
	three_cols( 'All Errors', scope.download['yf_errors']  , 'scope.download.yf_errors' )
	three_cols( 'All Data', scope.download['yf_data'], 'scope.download.yf_data' )
	






