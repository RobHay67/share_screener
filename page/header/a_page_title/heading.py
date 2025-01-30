import streamlit as st


def page_heading(scope):

	page = scope.display['page']
	page_icon = scope.config['page_schema'][page]['icon']
	page_title = scope.config['page_schema'][page]['title']

	st.subheader(
				body=page_icon + ' '	+ page_title, 
				divider='gray'
				)	
	