import streamlit as st

from pages.header.controller import render_app_header
from pages.config.controller import render_config_page

# Page Configuration
page = 'config'
page_title = 'Intra Day Analysis'
page_icon = '⚙️'
# -----------------------------
scope = st.session_state
scope.display_page = page


render_app_header(scope, page_title, page_icon)

if scope.user_logged_in:
	render_config_page(scope)



