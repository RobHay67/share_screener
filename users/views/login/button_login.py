import logging
import streamlit as st

from users.scope.login import login_user


def show_login_button(scope, login_name):
	logging.warning("show_login_button")
	button = st.button(	
					'login', 
					on_click=login_user, 
					args=(scope, login_name, ), 
					key='widget_login_button',
					)
	return button

