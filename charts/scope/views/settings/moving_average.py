import logging
import streamlit as st


from page.widgets.active import edit_active
from page.widgets.number import edit_number
from page.widgets.ohlc import edit_ohlc
from page.widgets.charts.colour import edit_colour


def moving_average_settings(scope, schema_key):  # SMA or EMA
	logging.debug("moving_average_settings")
	schema_group = 'charts'

	col1,col2,col3,col4,col5,col6 = st.columns([2,1,1,1,1,1])

	with col1:edit_active(scope, schema_group, schema_key)
	with col2:edit_number(scope, schema_group, schema_key, 'periods' )
	with col3:edit_ohlc(scope, schema_group, schema_key )
	with col4:edit_colour(scope, schema_group, schema_key )



