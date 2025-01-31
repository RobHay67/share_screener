
import logging
import streamlit as st
from users.scope.model.save.controller import save_users_table



def save_user_settings_button(scope):
	logging.debug("save_user_settings_button")
	button = st.button(
						label='💾 Save User Settings', 
						use_container_width=True, 
						on_click=save_users_table, args=(scope, ),
						)

	return button