
import streamlit as st

from pages.config.three_cols import three_cols



def view_download(scope):


	st.subheader('Download Configuration')
	three_cols( 'Download Variables stored in', {}, 'scope.yf', widget_type='string' )
	three_cols( 'Days to Download stored in', scope.pages['download_days'], "scope.pages['download_days']" )

	st.write('---')
	st.caption('Download settings')
	three_cols( 'Days to Download (yfinance format)', scope.yf['period'], "scope.yf['period']" )
	three_cols( 'Industry Groups for Batch iteration', scope.yf['download_these_industries'], "scope.yf['download_these_industries']",  widget_type='selectbox')

	st.write('---')
	st.caption('yFinance Batch Download Variables')
	three_cols( 'Type', scope.yf['batch_type'], "scope.yf['batch_type']" )
	three_cols( 'Batch Number', scope.yf['batch_no'], "scope.yf['batch_no']" )
	three_cols( 'Industry', scope.yf['batch_industry'], "scope.yf['batcbatch_industryh_type']" )
	three_cols( 'Ticker String', scope.yf['batch_ticker_string'], "scope.yf['batch_ticker_string']" )
	three_cols( 'Data', scope.yf['batch_data'], "scope.yf['batch_data']" )
	three_cols( 'Errors', scope.yf['batch_errors'], "scope.yf['batch_errors']" )
	
	st.write('---')
	st.caption('Download Variables')
	three_cols( 'Ticker List', scope.yf['ticker_list'], "scope.yf['ticker_list']" )
	three_cols( 'All Errors', scope.yf['errors']  , "scope.yf['errors']" )
	three_cols( 'All Data', scope.yf['data'], "scope.yf['data']" )
	






