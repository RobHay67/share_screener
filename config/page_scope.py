import logging
import streamlit as st
from page.header.router_page_title import page_title

from page.header.controller import controller_page_header
from config.scope.view_config_summary import show_config_summary
from config.scope.view_router import route_to_config_page


scope = st.session_state
page = 'scope'
scope.display['page'] = page
logging.info(f"{page=}")

page_title(scope)

# controller_page_header(scope)

if scope.users['logged_in']:
	# show_config_group_selection_buttons(scope)
	show_config_summary(scope)

	route_to_config_page(scope)

