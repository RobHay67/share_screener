
import streamlit as st

from widgets.active import edit_active
from widgets.trend import edit_trend_direction
from widgets.number import edit_number


def render_ohlcv_trend(scope, column_adder, column_name):
	
	type_config = 'trials'

	edit_active(scope, type_config, column_adder)
	st.write('column_name = ', column_name)
	edit_trend_direction (scope, type_config, column_adder)
	edit_number(scope, type_config, column_adder, 'duration' )
	edit_number(scope, type_config, column_adder, 'timespan' )
	st.markdown("""---""")

	