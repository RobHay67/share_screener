import logging
import streamlit as st
from page.header.controller import controller_page_header
# from config.scope.views.config_summary import show_config_group_selection_buttons
from config.scope.views.config_summary import show_config_summary
from config.scope.views.router import route_to_config_page


scope = st.session_state
page = 'scope'
scope.display['page'] = page
logging.info(f"{page=}")

controller_page_header(scope)

if scope.users['logged_in']:
	# show_config_group_selection_buttons(scope)
	show_config_summary(scope)

	route_to_config_page(scope)

