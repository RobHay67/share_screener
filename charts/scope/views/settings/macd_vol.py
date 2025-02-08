
import logging
import streamlit as st


from page.widgets.active import edit_active
from page.widgets.number import edit_number


def macd_volume_settings(scope):
	logging.warning("macd_volume_settings")
	schema_key = 'macd_vol'
	schema_group = 'charts'

	col1,col2,col3,col4,col5,col6 = st.columns([2,1,1,1,1,1])

	with col1:edit_active(scope, schema_group, schema_key)
	with col2:
		st.write('Column for MACD Vol')
		st.caption('Volume')
	with col3:edit_number(scope, schema_group, schema_key, 'long' )
	with col4:edit_number(scope, schema_group, schema_key, 'short' )
	with col5:edit_number(scope, schema_group, schema_key, 'signal' )
