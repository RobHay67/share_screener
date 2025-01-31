
import logging
import streamlit as st


def render_ticker_index_df(scope):
	logging.debug("render_ticker_index_df")
    # Entire Ticker index
	if scope.ticker_index['show']['ticker_index']:
		st.subheader('Ticker Index Dataframe')
		st.dataframe(scope.ticker_index['df'])




