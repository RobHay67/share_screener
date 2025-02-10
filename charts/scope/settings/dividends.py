import logging
import streamlit as st


from page.widgets.active import edit_active



def dividend_settings(scope):
	logging.warning("dividend_settings")
	schema_key = 'dividends'
	schema_group = 'charts'

	col1,col2,col3,col4,col5,col6 = st.columns([2,1,1,1,1,1])

	with col1:edit_active(scope, schema_group, schema_key)


