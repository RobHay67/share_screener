import streamlit as st


from widgets.active import edit_active
from widgets.number import edit_number
from widgets.ohlc import edit_ohlc
from widgets.colour import edit_colour


def render_moving_average(scope, col_adder):  # SMA or EMA

	config_name = 'charts'

	edit_active(scope, config_name, col_adder)
	edit_number(scope, config_name, col_adder, 'periods' )
	edit_ohlc(scope, config_name, col_adder )
	edit_colour(scope, config_name, col_adder )
	st.markdown("""---""")



