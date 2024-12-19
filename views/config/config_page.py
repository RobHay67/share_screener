import streamlit as st

from views.header.controller import render_page_header
from views.config.controller import render_config_page

# Page Configuration
page = 'config'
page_title = 'Application Configuration & Settings'
page_icon = '⚙️'
# -----------------------------
scope = st.session_state
scope.pages['display'] = page


render_page_header(scope, page_title, page_icon)

if scope.users['logged_in']:
	render_config_page(scope)



