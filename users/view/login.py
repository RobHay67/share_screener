
import streamlit as st

from users.model.config import set_user_access

def render_login_form(scope):

	col1,col2 = st.columns([2,8])
	
	with col1:

		st.subheader('Login to Share Screener Application')

		login_name = st.text_input('User Name')
		login_pword = st.text_input('Password', type='password')
		
		if login_name in scope.users['user_list']:
			user_pword = scope.users['json'][login_name]['password']

			if login_pword == user_pword:
				st.button(	
							'login', 
							on_click=set_user_access, 
							args=(scope, login_name, ), 
							key='widget_login_button',
							)
			else:
				if login_pword != '':
					login_message(login_name, 'invalid_password')
		else:
			if login_name != '':
				login_message(login_name, 'invalid_user')




def login_message(login_name, status):

	if status == 'logged_in':
		st.success(login_name + ' Logged In')

	if status == 'invalid_password':
		st.error('Password is invalid for ' + login_name)

	if status == 'invalid_user':
		st.error('User Name ' + login_name + ' does not exist')