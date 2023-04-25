import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from pages.header.page_title import page_title_layer
from users.logout import logout_user

# Page Configuration
page = 'logout'
page_title = 'Logout ( Save User Settings )'
page_icon = '🔒'
# -----------------------------
scope = st.session_state
scope.pages['display'] = page


page_title_layer(scope, page_title, page_icon)

logout_button = st.button(label='Logout Now')

if logout_button:
    logout_user(scope)
    st.warning('Logged out the user')
    switch_page('Home')













