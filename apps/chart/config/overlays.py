import streamlit as st

from apps.chart.config.announcements import render_announcements
from apps.chart.config.bollinger_bands import render_bollinger_bands
from apps.chart.config.dividends import render_dividends
from apps.chart.config.moving_average import render_moving_average



def render_overlays_config(scope):
	# ----------------------------------------------------------------------
	# Overlays
	# ----------------------------------------------------------------------
	
	
	st.markdown("""---""")
	st.subheader('Overlays')
	st.caption('added to every relevant chart')
	
	col1,col2,col3,col4,col5,col6 = st.columns([1,1,1,1,1,1])
	
	
	render_dividends(scope)
	render_announcements(scope)

	render_moving_average(scope, 'sma_1')
	render_moving_average(scope, 'sma_2')
	render_moving_average(scope, 'sma_3')
	
	render_moving_average(scope, 'ema_1')
	render_moving_average(scope, 'ema_2')
	render_moving_average(scope, 'ema_3')

	render_bollinger_bands(scope)

	st.markdown("""---""")


