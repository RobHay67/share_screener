
import streamlit as st

from picker.controller import ticker_picker


def analysis_titles(scope, title, page ):
	st.header(title)
	ticker_picker(scope, page)
	st.markdown("""---""")