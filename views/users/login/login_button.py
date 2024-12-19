import streamlit as st

from users.login import login_user


def login_button(scope, login_name):
		button = st.button(	
						'login', 
						on_click=login_user, 
						args=(scope, login_name, ), 
						key='widget_login_button',
						)
		print('Manual Login called for >', login_name)

		return button

