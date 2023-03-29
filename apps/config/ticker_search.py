

import streamlit as st
from apps.config.three_cols import three_cols




def scope_ticker_search(scope):
	# company names for the ticker search
	scope.config['ticker_search'] = {}
	scope.config['ticker_search'] = (scope.ticker_index['df']['company_name']).to_dict()


def view_ticker_search(scope):
	st.subheader('Ticker Search')
	three_cols( 'Ticker Search (Default List)', scope.config['ticker_search'], "scope.config['ticker_search']" )


