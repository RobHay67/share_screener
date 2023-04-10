import streamlit as st


from pages.widgets.active import edit_active
from pages.widgets.number import edit_number
from pages.widgets.ohlc import edit_ohlc
from pages.widgets.colour import edit_colour


def render_moving_average(scope, config_key_name):  # SMA or EMA

	config_group = 'charts'

	col1,col2,col3,col4,col5,col6 = st.columns([2,1,1,1,1,1])

	with col1:edit_active(scope, config_group, config_key_name)
	with col2:edit_number(scope, config_group, config_key_name, 'periods' )
	with col3:edit_ohlc(scope, config_group, config_key_name )
	with col4:edit_colour(scope, config_group, config_key_name )



