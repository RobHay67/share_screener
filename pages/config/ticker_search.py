

import streamlit as st
from pages.config.three_cols import three_cols



def view_ticker_search(scope):
	st.subheader('Ticker Search')
	three_cols( 'Ticker Search (Default List)', scope.pages['ticker_search'], "scope.pages['ticker_search']" )


