
import streamlit as st
from pages.config.three_cols import three_cols



def view_missing_tickers(scope):

	st.subheader('Missing Tickers Configuration')
	three_cols( 'Missing Tickers Configuration stored in', {}, "scope.tickers['missing']", widget_type='string' )

	st.subheader('Missing Lists')
	three_cols( 'Local', scope.tickers['missing']['local'], "scope.tickers['missing']['local']" )
	three_cols( 'Cloud', scope.tickers['missing']['cloud'], "scope.tickers['missing']['cloud']" )
	three_cols( 'Complete List', scope.tickers['missing']['list'], "scope.tickers['missing']['list']" )

	st.subheader('Ticker Missing Errors')
	three_cols( 'Missing Ticker Error Messages', scope.tickers['missing']['errors'], "scope.tickers['missing']['errors']" )

	




