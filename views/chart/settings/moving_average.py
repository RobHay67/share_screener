import streamlit as st


from views.widgets.active import edit_active
from views.widgets.number import edit_number
from views.widgets.ohlc import edit_ohlc
from views.chart.settings.colour import edit_colour


def render_moving_average(scope, config_key):  # SMA or EMA

	config_group = 'charts'

	col1,col2,col3,col4,col5,col6 = st.columns([2,1,1,1,1,1])

	with col1:edit_active(scope, config_group, config_key)
	with col2:edit_number(scope, config_group, config_key, 'periods' )
	with col3:edit_ohlc(scope, config_group, config_key )
	with col4:edit_colour(scope, config_group, config_key )



