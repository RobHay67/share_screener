
import streamlit as st

from pages.picker.controller import render_ticker_picker


def render_page_title(scope, title):
	st.header(title)
	render_ticker_picker(scope)
	st.markdown("""---""")