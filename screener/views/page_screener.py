import streamlit as st

from app.views.header.controller import show_page_header		
from screener.views.verdicts.controller import show_verdicts


# Page Configuration
scope = st.session_state
page = 'screener'
page_title = 'Ticker Screener'
page_icon = '🧪'
# -----------------------------

scope.pages['display'] = page


show_page_header(scope, page_title, page_icon)

if scope.users['logged_in']:
	show_verdicts(scope)