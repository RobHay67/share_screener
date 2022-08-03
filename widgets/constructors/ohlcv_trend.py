
import streamlit as st

# from config.model.set_analysis_active import edit_active
from widgets.active import edit_active
# from config.model.set_ohlcv import edit_ohlcv
from widgets.trend import edit_trend_direction
from widgets.number import edit_number


# def render_ohlcv_trend(scope, measure, column_name):
def render_ohlcv_trend(scope, col_adder, column_name):
	# col_adder = 'macd'
	config_name = 'trials'

	# edit_active(scope, 'trials', measure)
	edit_active(scope, config_name, col_adder)
	st.write('column_name = ', column_name)
	edit_trend_direction (scope, config_name, col_adder)
	edit_number(scope, config_name, col_adder, 'duration' )
	edit_number(scope, config_name, col_adder, 'timespan' )
	st.markdown("""---""")


	# edit_active(scope, config_name, col_adder ):
	# with col1: render_ohlcv_trend(scope, 'trend_open', 'open')	
	# with col2: render_ohlcv_trend(scope, 'trend_high', 'high')
	# with col3: render_ohlcv_trend(scope, 'trend_low', 'low')
	# with col4: render_ohlcv_trend(scope, 'trend_close', 'close')
	# with col5: render_ohlcv_trend(scope, 'trend_volume', 'volume')



	