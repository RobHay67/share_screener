
import streamlit as st

from ticker.loader import ticker_loader


def analysis_titles(scope, title, page ):
	st.subheader(title)
	ticker_loader(scope, page)
	st.markdown("""---""")