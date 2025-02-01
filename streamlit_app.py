# ------------------------------------------------- Execute Application
# pipenv shell
# streamlit run streamlit_app.py
# --------------------------------------------------------------------- 
import logging
import streamlit as st
from config.logger.log import set_logging_config
from config.helpers.re_render import app_is_re_rendering
from config.scope.model.set_scope import set_scope
from users.page_login import show_login_page
from page.sidebar.market_info import show_sidebar_app_info
from page.navigation.page_navigation import sidebar_navigation


set_logging_config()
app_is_re_rendering()

if __name__ == "__main__":
	scope = set_scope(st.session_state)
	page_navigation = sidebar_navigation(scope)

	match scope.users['logged_in']:
		case True:
			page_navigation.run()			# adds Application Navigation Buttons
			show_sidebar_app_info(scope)	# adds additional market info and global variables
		case _ : 
			show_login_page(scope)

	logging.critical("Download and Save the dividend data to this app")
	





