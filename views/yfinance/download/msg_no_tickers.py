import streamlit as st


def no_tickers_selected(scope):
	st.toast("No Tickers have been selected. The Page worklist is empty", icon='⚠️')
