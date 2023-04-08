import streamlit as st


from widgets.active import edit_active
from widgets.number import edit_number
from widgets.ohlc import edit_ohlc
from widgets.colour import edit_colour


def render_moving_average(scope, column_adder):  # SMA or EMA

	type_config = 'charts'

	col1,col2,col3,col4,col5,col6 = st.columns([2,1,1,1,1,1])

	with col1:edit_active(scope, type_config, column_adder)
	with col2:edit_number(scope, type_config, column_adder, 'periods' )
	with col3:edit_ohlc(scope, type_config, column_adder )
	with col4:edit_colour(scope, type_config, column_adder )



