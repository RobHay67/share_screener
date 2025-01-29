import streamlit as st

from app.views.header.a_page_title.router import page_title_layer



def show_welcome_page(scope):
	scope.config['display'] = 'welcome'

	page_title_layer(scope)
	st.write('Welcome to the Share Picker Appliction.')
	st.write('Select from the options in the sidebar (left)')
	st.write('User : ', scope.users['login_name'])

