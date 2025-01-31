import logging
import streamlit as st

from page.widgets.active import edit_active
from page.widgets.number import edit_number
from page.widgets.ohlc import edit_ohlc, edit_ohlc_active_col


def line_settings(scope):
	logging.debug("line_settings")
	schema_group = 'charts'
	schema_key = 'line'
	
	col1,col2,col3,col4,col5,col6 = st.columns([2,1,1,1,1,1])

	with col1:edit_active(scope, schema_group, schema_key)
	with col2:edit_ohlc_active_col(scope, schema_group, schema_key, 'open')
	with col3:edit_ohlc_active_col(scope, schema_group, schema_key, 'high' )
	with col4:edit_ohlc_active_col(scope, schema_group, schema_key, 'low' )
	with col5:edit_ohlc_active_col(scope, schema_group, schema_key, 'close' )


