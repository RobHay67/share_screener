
import streamlit as st
from pages.config.three_cols import three_cols



def view_missing_tickers(scope):

	st.subheader('Missing Tickers Configuration')
	three_cols( 'Missing Tickers Configuration stored in', {}, 'scope.missing_tickers', widget_type='string' )

	st.subheader('Missing Lists')
	three_cols( 'Local', scope.missing_tickers['local'], "scope.missing_tickers['local']" )
	three_cols( 'Cloud', scope.missing_tickers['cloud'], "scope.missing_tickers['cloud']" )
	three_cols( 'Complete List', scope.missing_tickers['list'], "scope.missing_tickers['list']" )

	st.subheader('Ticker Missing Errors')
	three_cols( 'Missing Ticker Error Messages', scope.missing_tickers['errors'], "scope.missing_tickers['errors']" )

	




