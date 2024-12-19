import streamlit as st

from users.login import login_user

def auto_login_button(scope):
	button = st.button(
						'Press to Auto Login to Rob ', 
						on_click=login_user, 
						args=(scope, 'Rob', ),
						key='widget_auto_login_button',)
	return button

