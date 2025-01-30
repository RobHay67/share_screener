# This function show the results of any tests that have been run
# The actual tests runs are triggered by activating the tests or
# by making changes to the tests.
# Essentially this page show the results of those tests and provides
# the settings page to make test config changes.

# Note : Screener Tests are run during the add_columns calls
# 			- this is controlled by the header function


import streamlit as st

from app.views.header.controller import show_page_header
from screener.views.active_trials.active_tests import show_active_trials
from screener.views.verdicts.router import show_verdicts


# Page Configuration
scope = st.session_state
page = 'screener'
scope.display['page'] = page
show_page_header(scope)
if scope.users['logged_in']:
	show_active_trials(scope)
	show_verdicts(scope)
	st.divider()
	st.subheader('Fliss Simple Strategy')
	st.write('Closing Price is up n times over the last x days')
	st.write('Volume is up n times over the last x days')

