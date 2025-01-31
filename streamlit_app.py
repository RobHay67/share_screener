# ------------------------------------------------- Execute Application
# pipenv shell
# streamlit run streamlit_app.py
# ------------------------------------------------- 

import logging
# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(
					
					# filename="app.log",
					# encoding="utf-8",
					# filemode="a",			# a = append (to log file)
					format="{asctime} - {levelname} - {message}",
					style="{",
					datefmt="%Y-%m-%d %H:%M:%S",
					level=logging.DEBUG,
					)
# logging.getLogger(__name__)
# logging.warning("remain Calm!")

import streamlit as st
from config.helpers.re_render import app_is_re_rendering
from config.scope.model.set_scope import set_scope
from users.page_login import show_login_page
from page.sidebar.market_info import show_sidebar_app_info
from page.navigation.page_navigation import sidebar_navigation_buttons
from config.helpers.scope_keys import print_scope_keys


app_is_re_rendering()

if __name__ == "__main__":
	scope = set_scope(st.session_state)
	page_navigation = sidebar_navigation_buttons(scope)

	match scope.users['logged_in']:
		case True:
			page_navigation.run()			# adds Application Navigation Buttons
			show_sidebar_app_info(scope)	# adds additional market info and global variables
		case _ : 
			show_login_page(scope)

	logging.info("Download and Save the dividend data to this app")
	print_scope_keys('streamlit_app')















# [packages]
# pandas = "==1.5.3"
# streamlit = "*"
# datetime = "*"
# yfinance = "==0.2.14"
# mplfinance = "===0.12.7a5"
# matplotlib = "*"
# plotly = "*"
# pytz = "==2023.3"
# watchdog = "*"
# streamlit-extras = "*"
# jinja2 = "*"

# [dev-packages]

# [requires]
# python_version = "3.8"