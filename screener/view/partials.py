import streamlit as st

# from config.model.set_analysis_active import edit_active
from config.model.set_active import edit_active
from config.model.set_ohlcv import edit_ohlcv
from config.model.set_trend import edit_trend
from config.model.set_number import edit_number



def render_ohlcv_trend(scope, measure, column):
	edit_active(scope, 'screener_schema', measure)
	st.write('Column = ', column)
	edit_trend(scope, 'screener_schema', measure)
	edit_number(scope, 'screener_schema', measure, 'duration' )
	edit_number(scope, 'screener_schema', measure, 'timespan' )
	st.markdown("""---""")