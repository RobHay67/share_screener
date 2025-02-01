import logging
import streamlit as st

from page.header.controller import add_page_header

# Page Configuration
scope = st.session_state
page = 'testing'
scope.display['page'] = page
logging.info(f"{page=}")

add_page_header(scope)










