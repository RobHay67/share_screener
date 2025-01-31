import logging
import streamlit as st


def add_page_title(scope):
	logging.debug("add_page_title")
	page = scope.display['page']
	page_icon = scope.config['page_schema'][page]['icon']
	page_title = scope.config['page_schema'][page]['title']

	st.subheader(
				body=page_icon + ' '	+ page_title, 
				divider='gray'
				)	
	