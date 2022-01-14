import streamlit as st


from metrics.model.set_active import edit_active
from metrics.model.set_number import edit_number
from metrics.model.set_ohlcv import edit_ohlc
from metrics.model.set_colour import edit_colour





def render_moving_average(scope, metric):  # SMA or EMA

	config_name = 'charts'

	edit_active(scope, config_name, metric)
	edit_number(scope, config_name, metric, 'periods' )
	edit_ohlc(scope, config_name, metric )
	edit_colour(scope, config_name, metric )
	st.markdown("""---""")



