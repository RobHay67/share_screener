# ------------------------------------------------- Execute Application
# pipenv shell
# streamlit run streamlit_app.py
# --------------------------------------------------------------------- 
import logging
import streamlit as st
from config.logger.log import set_logging_config
from config.helpers.re_render import app_is_re_rendering
from config.scope.scope_set_scope import set_scope
from users.page_login import build_login_page
from page.sidebar.market_info import show_sidebar_app_info
from page.navigation.page_navigation import sidebar_navigation


scope=st.session_state
if 'config' not in scope:
	set_logging_config()	# This needs to be the first code to run


if __name__ == "__main__":
	app_is_re_rendering()
	if 'config' not in scope:set_scope(scope)
	page_navigation = sidebar_navigation(scope)

	match scope.users['logged_in']:
		case True:
			page_navigation.run()			# adds Application Navigation Buttons
			show_sidebar_app_info(scope)	# adds additional market info and global variables
		case _ : 
			build_login_page(scope)

	
	





