import logging
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from page.header.a_page_title.router import build_page_header_title_row
from users.scope.model.logout import logout_user



# Page Configuration
scope = st.session_state
page = 'logout'
scope.display['page'] = page
logging.info(f"{page=}")

build_page_header_title_row(scope)
logout_button = st.button(label='Logout Now')

if logout_button:
    logout_user(scope)
    st.warning('Logged out the user')
    switch_page('streamlit_app')















