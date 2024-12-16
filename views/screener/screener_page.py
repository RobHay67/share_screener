import streamlit as st

from views.header.controller import render_app_header		
from views.screener.verdicts import render_trial_verdicts


# Page Configuration
scope = st.session_state
page = 'screener'
page_title = 'Ticker Screener'
page_icon = '🧪'
# -----------------------------

scope.pages['display'] = page


render_app_header(scope, page_title, page_icon)

if scope.users['logged_in']:
	render_trial_verdicts(scope)