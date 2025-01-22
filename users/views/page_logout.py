import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from app.views.header.a_page_title.page_titles import page_title_layer
from users.scope.model.logout import logout_user



# Page Configuration
scope = st.session_state
scope.config['display'] = 'logout'

page_title_layer(scope)
logout_button = st.button(label='Logout Now')

if logout_button:
    logout_user(scope)
    st.warning('Logged out the user')
    switch_page('streamlit_app')















