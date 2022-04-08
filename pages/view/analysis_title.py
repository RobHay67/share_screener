
import streamlit as st

from pages.picker.controller import render_ticker_picker


# def analysis_titles(scope, title, page ):
def analysis_titles(scope, title):
	st.header(title)
	render_ticker_picker(scope)
	st.markdown("""---""")