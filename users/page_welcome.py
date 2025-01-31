import logging
import streamlit as st

from page.header.a_page_title.router import page_title_layer



def show_welcome_page(scope):
	logging.debug("show_welcome_page")
	scope.display['page'] = 'welcome'

	page_title_layer(scope)
	st.write('Welcome to the Share Picker Appliction.')
	st.write('Select from the options in the sidebar (left)')
	st.write('User : ', scope.users['login_name'])

