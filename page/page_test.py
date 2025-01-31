import logging
import streamlit as st

from page.header.controller import show_page_header

# Page Configuration
scope = st.session_state
page = 'testing'
scope.display['page'] = page
logging.debug("page = test")

show_page_header(scope)










