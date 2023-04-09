import streamlit as st

from pages.header.controller import render_app_header		
from pages.screener.verdicts import render_trial_verdicts


# Page Configuration
scope = st.session_state
page = 'screener'
page_title = 'Ticker Screener'
page_icon = '🧪'
# -----------------------------

scope.display_page = page


render_app_header(scope, page_title, page_icon)

if scope.user_logged_in:
	render_trial_verdicts(scope)