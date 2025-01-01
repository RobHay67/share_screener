import streamlit as st

from charts.views.settings.announcements import render_announcements
from charts.views.settings.bollinger_bands import render_bollinger_bands
from charts.views.settings.dividends import render_dividends
from charts.views.settings.moving_average import render_moving_average



def show_overlay_config(scope):
	# ----------------------------------------------------------------------
	# Overlays
	# ----------------------------------------------------------------------
	
	
	st.divider()
	st.subheader('Overlays')
	st.caption('added to every relevant chart')
	
	col1,col2,col3,col4,col5,col6 = st.columns([1,1,1,1,1,1])
	
	
	render_dividends(scope)
	render_announcements(scope)

	render_moving_average(scope, 'sma_a')
	render_moving_average(scope, 'sma_b')
	render_moving_average(scope, 'sma_c')
	
	render_moving_average(scope, 'ema_a')
	render_moving_average(scope, 'ema_b')
	render_moving_average(scope, 'ema_c')

	render_bollinger_bands(scope)

	st.divider()



