
import streamlit as st
from users.scope.model.save.controller import save_users_table



def save_user_settings_button(scope):

	# page = scope.config['display']
	# current_value = scope.page[page]['render']['strategy']
	# type_of_button = 'primary' if current_value == True else 'secondary'

	button = st.button(
						label='💾 Save User Settings', 
						use_container_width=True, 
						on_click=save_users_table, args=(scope, ),
						# type=type_of_button,
						# help='Save these settings for next login'
						)

	return button