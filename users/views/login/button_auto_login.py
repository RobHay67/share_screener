import logging
import streamlit as st

from users.scope.model.login import login_user

def add_auto_login_button(scope):
	logging.debug("add_auto_login_button")
	button = st.button(
						'Press to Auto Login to Rob ', 
						on_click=login_user, 
						args=(scope, 'Rob', ),
						key='widget_auto_login_button',)
	return button

