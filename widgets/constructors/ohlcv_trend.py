
import streamlit as st

# from config.model.set_analysis_active import edit_active
from widgets.active import edit_active
# from config.model.set_ohlcv import edit_ohlcv
from widgets.trend import edit_trend
from widgets.number import edit_number


# def render_ohlcv_trend(scope, measure, column_name):
def render_ohlcv_trend(scope, metric, column_name):
	# metric = 'macd'
	config_name = 'tests'

	# edit_active(scope, 'tests', measure)
	edit_active(scope, config_name, metric)
	st.write('column_name = ', column_name)
	edit_trend (scope, config_name, metric)
	edit_number(scope, config_name, metric, 'duration' )
	edit_number(scope, config_name, metric, 'timespan' )
	st.markdown("""---""")


	# edit_active(scope, config_name, metric ):
	# with col1: render_ohlcv_trend(scope, 'trend_open', 'open')	
	# with col2: render_ohlcv_trend(scope, 'trend_high', 'high')
	# with col3: render_ohlcv_trend(scope, 'trend_low', 'low')
	# with col4: render_ohlcv_trend(scope, 'trend_close', 'close')
	# with col5: render_ohlcv_trend(scope, 'trend_volume', 'volume')



	