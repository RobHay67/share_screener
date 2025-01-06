# This function show the results of any tests that have been run
# The actual tests runs are triggered by activating the tests or
# by making changes to the tests.
# Essentially this page show the results of those tests and provides
# the settings page to make test config changes.

# Note : Screener Tests are run during the add_columns calls
# 			- this is controlled by the header function


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