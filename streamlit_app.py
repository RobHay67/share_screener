# ------------------------------------------------- Execute Application
# pipenv shell
# streamlit run streamlit_app.py
# ------------------------------------------------- 


import streamlit as st
from config.helpers.re_render import app_is_re_rendering
from config.scope.model.set_scope import set_scope
from users.views.page_login import show_login_page
from page.sidebar.market_info import show_sidebar_app_info
from page.navigation.page_navigation import sidebar_navigation_buttons
from config.helpers.scope_keys import print_scope_keys


app_is_re_rendering()

if 'display_page' not in st.session_state:
	scope = set_scope(st.session_state)

page_navigation = sidebar_navigation_buttons(scope)

# Render Pages
if scope.users['logged_in'] == True:
	page_navigation.run()			# adds Application Navigation Buttons
	show_sidebar_app_info(scope)	# adds additional market info and global variables
else:
	show_login_page(scope)


#======================================================== TODO s
for i in range(5):print('')
print('='*66)
print('TODOs - document while coding then move to Trello')
print('TODO - we need to download and SAVE the dividend data as well')

print('='*66)
for i in range(3):print('')

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