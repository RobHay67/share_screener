import streamlit as st

# from config.model.set_analysis_active import edit_active
from config.model.set_active import edit_active
from config.model.set_ohlcv import edit_ohlcv
from config.model.set_trend import edit_trend
from config.model.set_number import edit_number



def render_ohlcv_trend(scope, measure, column):
	edit_active(scope, 'analysis', measure)
	st.write('Column = ', column)
	edit_trend(scope, 'analysis', measure)
	edit_number(scope, 'analysis', measure, 'duration' )
	edit_number(scope, 'analysis', measure, 'timespan' )
	st.markdown("""---""")