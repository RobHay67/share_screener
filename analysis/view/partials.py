import streamlit as st

from config.model.set_analysis_active import edit_active
from config.model.set_ohlcv import edit_ohlcv


def render_ohlcv_trend(scope, measure):
	edit_active(scope, measure)
	edit_ohlcv(scope, measure)
	# edit_number(scope, chart, 'periods' )
	# edit_price(scope, chart )
	# edit_colour(scope, chart )
	# st.markdown("""---""")