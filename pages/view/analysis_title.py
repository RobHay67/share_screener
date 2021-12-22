
import streamlit as st

from picker.controller import ticker_picker


# def analysis_titles(scope, title, page ):
def analysis_titles(scope, title):
	st.header(title)
	ticker_picker(scope)
	st.markdown("""---""")