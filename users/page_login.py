
import logging
import streamlit as st

from users.views.login.button_auto_login import auto_login_button
from users.views.login.button_login import show_login_button
from users.views.login.messages import show_login_message


def build_login_page(scope):
	logging.debug("build_login_page")
	st.subheader('Login')

	login_name = st.text_input('User Name')
	login_pword = st.text_input('Password', type='password')

	if scope.allow_auto_login:
		auto_login_button(scope)

	if login_name in scope.users['user_list']:
		if login_pword == scope.users['json'][login_name]['password']:
			show_login_button(scope)
		else:
			if login_pword != '':
				show_login_message(login_name, 'invalid_password')
	else:
		if login_name != '':
			show_login_message(login_name, 'invalid_user')






