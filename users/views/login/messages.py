import logging
import streamlit as st


def login_message(login_name, status):
	logging.debug("login_message")
	scope = st.session_state
	if status == 'logged_in':
		st.success(login_name + ' Logged In')

		st.write('Welcome to the Share Picker Appliction.')
		st.write('Select from the options in the sidebar (left)')
		st.write('User : ', scope.users['login_name'])

	if status == 'invalid_password':
		st.error('Password is invalid for ' + login_name)

	if status == 'invalid_user':
		st.error('User Name ' + login_name + ' does not exist')
