import streamlit as st
from app.views.header.controller import show_page_header
# from app.scope.views.config_summary import show_config_group_selection_buttons
from app.scope.views.config_summary import show_config_summary
from app.scope.views.router import route_to_config_page


scope = st.session_state
scope.config['display'] = 'scope'

show_page_header(scope)

if scope.users['logged_in']:
	# show_config_group_selection_buttons(scope)
	show_config_summary(scope)

	route_to_config_page(scope)

