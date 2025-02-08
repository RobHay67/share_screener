import logging
import streamlit as st
from page.header.router_page_title import page_title



def show_welcome_page(scope):
	page = 'welcome'
	scope.display['page'] = page
	logging.warning(f"show_welcome_page {page=}")

	page_title(scope)
	st.write('Welcome to the Share Picker Appliction.')
	st.write('Select from the options in the sidebar (left)')
	st.write('User : ', scope.users['login_name'])

