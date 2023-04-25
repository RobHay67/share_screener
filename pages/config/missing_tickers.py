
import streamlit as st
from pages.config.three_cols import three_cols



def view_missing_tickers(scope):

	st.subheader('Missing Tickers Configuration')
	three_cols( 'Missing Tickers Configuration stored in', {}, "scope.tickers_missing", widget_type='string' )

	st.subheader('Missing Lists')
	three_cols( 'Local', scope.tickers_missing['local'], "scope.tickers_missing['local']" )
	three_cols( 'Cloud', scope.tickers_missing['cloud'], "scope.tickers_missing['cloud']" )
	three_cols( 'Complete List', scope.tickers_missing['list'], "scope.tickers_missing['list']" )

	st.subheader('Ticker Missing Errors')
	three_cols( 'Missing Ticker Error Messages', scope.tickers_missing['errors'], "scope.tickers_missing['errors']" )

	




