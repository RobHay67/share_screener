import logging
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from page.header.router_page_title import row_page_title
from users.scope.model.logout import logout_user



# Page Configuration
scope = st.session_state
page = 'logout'
scope.display['page'] = page
logging.debug(f"{page=}")

row_page_title(scope)
logout_button = st.button(label='Logout Now')

if logout_button:
    logout_user(scope)
    st.warning('Logged out the user')
    switch_page('streamlit_app')















