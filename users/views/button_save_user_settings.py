
import logging
import streamlit as st
from users.scope.model.save.controller import save_users_table



def button_save_user_settings(scope):
	logging.debug("button_save_user_settings")
	button = st.button(
						label='💾 Save User Settings', 
						use_container_width=True, 
						on_click=save_users_table, args=(scope, ),
						)

	return button