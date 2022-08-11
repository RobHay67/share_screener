
import streamlit as st

from widgets.active import edit_active
from widgets.trend import edit_trend_direction
from widgets.number import edit_number


# def render_ohlcv_trend(scope, measure, column_name):
def render_ohlcv_trend(scope, column_adder, column_name):
	# column_adder = 'macd'
	type_config = 'trials'

	# edit_active(scope, 'trials', measure)
	edit_active(scope, type_config, column_adder)
	st.write('column_name = ', column_name)
	edit_trend_direction (scope, type_config, column_adder)
	edit_number(scope, type_config, column_adder, 'duration' )
	edit_number(scope, type_config, column_adder, 'timespan' )
	st.markdown("""---""")


	# edit_active(scope, type_config, column_adder ):
	# with col1: render_ohlcv_trend(scope, 'trend_open', 'open')	
	# with col2: render_ohlcv_trend(scope, 'trend_high', 'high')
	# with col3: render_ohlcv_trend(scope, 'trend_low', 'low')
	# with col4: render_ohlcv_trend(scope, 'trend_close', 'close')
	# with col5: render_ohlcv_trend(scope, 'trend_volume', 'volume')


	print('test')
	