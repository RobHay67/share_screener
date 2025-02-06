import logging
import streamlit as st

from page.header.controller import controller_page_header

# Page Configuration
scope = st.session_state
page = 'testing'
scope.display['page'] = page
logging.debug(f"{page=}")

controller_page_header(scope)










