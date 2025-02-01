import logging
import streamlit as st

from page.header.a_page_title.router import build_page_header_title_row



def show_welcome_page(scope):
	page = 'welcome'
	scope.display['page'] = page
	logging.info(f"show_welcome_page {page=}")

	build_page_header_title_row(scope)
	st.write('Welcome to the Share Picker Appliction.')
	st.write('Select from the options in the sidebar (left)')
	st.write('User : ', scope.users['login_name'])

