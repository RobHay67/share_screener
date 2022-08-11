import streamlit as st


from widgets.active import edit_active
from widgets.number import edit_number
from widgets.ohlc import edit_ohlc
from widgets.colour import edit_colour


def render_moving_average(scope, column_adder):  # SMA or EMA

	type_config = 'charts'

	edit_active(scope, type_config, column_adder)
	edit_number(scope, type_config, column_adder, 'periods' )
	edit_ohlc(scope, type_config, column_adder )
	edit_colour(scope, type_config, column_adder )
	st.markdown("""---""")



