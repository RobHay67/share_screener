
import streamlit as st

from users.views.login.login_auto_button import auto_login_button
from users.views.login.login_button import login_button
from users.views.login.messages import login_message


def render_login_page(scope):

	st.subheader('Login')

	login_name = st.text_input('User Name')
	login_pword = st.text_input('Password', type='password')

	if scope.allow_auto_login:
		auto_login_button(scope)

	if login_name in scope.users['user_list']:
		if login_pword == scope.users['json'][login_name]['password']:
			login_button(scope)
		else:
			if login_pword != '':
				login_message(login_name, 'invalid_password')
	else:
		if login_name != '':
			login_message(login_name, 'invalid_user')





