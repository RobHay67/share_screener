# This function show the results of any tests that have been run
# The actual tests runs are triggered by activating the tests or
# by making changes to the tests.
# Essentially this page show the results of those tests and provides
# the settings page to make test config changes.

# Note : Screener Tests are run during the add_columns calls
# 			- this is controlled by the header function

import logging
import streamlit as st

from page.header.controller import controller_page_header



# Page Configuration
scope = st.session_state
page = 'screener'
scope.display['page'] = page
logging.info(f"{page=}")


controller_page_header(scope)
# if scope.users['logged_in']:
	

