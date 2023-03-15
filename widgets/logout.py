
import streamlit as st

from users.logout import logout_user


def logout_button(scope):

	widget_key = 'widget_logout_button' 

	st.sidebar.button( 
					'Logout ( Save Settings )', 
					on_click=logout_user, 
					args=(scope, ), 
					key=widget_key,
					use_container_width=True
					)