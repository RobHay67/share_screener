
import streamlit as st

from pages.config.three_cols import three_cols



def view_download(scope):


	st.subheader('Download Configuration')
	three_cols( 'Download Variables stored in', {}, 'scope.yf', widget_type='string' )

	# st.subheader('Most Recent Download Variables and Data')
	st.subheader('Download Days')
	three_cols( 'Days to Download (recent)', scope.config['download_days'], "scope.config['download_days']" )
	three_cols( 'Days to Download (yfinance format)', scope.yf['period'], 'scope.yf.yf_period' )
	
	st.subheader('yFinance Batch Download Variables')
	three_cols( 'Industry Groups for iteration', scope.yf['download_these_industries'], 'scope.yf.yf_download_these_industries',  widget_type='selectbox')
	three_cols( 'Type', scope.yf['batch_type'], 'scope.yf.yf_batch_type' )
	three_cols( 'Batch Number', scope.yf['batch_no'], 'scope.yf.yf_batch_no' )
	three_cols( 'Industry', scope.yf['batch_industry'], 'scope.yf.yf_batch_industry' )
	three_cols( 'Ticker String', scope.yf['batch_ticker_string'], 'scope.yf.yf_batch_ticker_string' )
	three_cols( 'Data', scope.yf['batch_data'], 'scope.yf.yf_batch_data' )
	three_cols( 'Errors', scope.yf['batch_errors'], 'scope.yf.yf_batch_errors' )
	
	
	st.subheader('Batch Download Variables')
	three_cols( 'Ticker List', scope.yf['ticker_list'], 'scope.yf.yf_data' )
	three_cols( 'All Errors', scope.yf['errors']  , 'scope.yf.yf_errors' )
	three_cols( 'All Data', scope.yf['data'], 'scope.yf.yf_data' )
	






