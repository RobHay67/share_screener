import logging
import streamlit as st


def no_tickers_selected(scope):
	logging.debug("no_tickers_selected")
	st.toast("No Tickers have been selected. The Page worklist is empty", icon='⚠️')
