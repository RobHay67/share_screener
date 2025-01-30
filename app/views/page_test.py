import streamlit as st

from app.views.header.controller import show_page_header


# Page Configuration
scope = st.session_state
page = 'testing'
scope.display['page'] = page

show_page_header(scope)










