import streamlit as st


from apps.config_charts.active import render_activate_metric
from apps.config_charts.announcements import render_announcements
from apps.config_charts.bollinger_bands import render_bollinger_bands
from apps.config_charts.dividends import render_dividends
from apps.config_charts.moving_average import render_moving_average

from widgets.chart_height import set_chart_height_primary

def render_primary_charts_config(scope):

	# ----------------------------------------------------------------------
	# Primary Charts
	# ----------------------------------------------------------------------

	col1,col2,col3,col4,col5,col6,col7 = st.columns([1,1,1,1,1,1,1])
	
	with col1: st.header('Primary Charts')
	with col2: st.write('.')
	with col2: st.write('.')
	with col2: set_chart_height_primary(scope)

	with col3: render_primary_chart(scope, 'candlestick')
	with col4: render_primary_chart(scope, 'scatter')
	with col5: render_primary_chart(scope, 'bar')
	with col6: render_primary_chart(scope, 'line')
	with col7: render_primary_chart(scope, 'heiken_ashi')
	
	st.markdown("""---""")


	# ----------------------------------------------------------------------
	# Overlays
	# ----------------------------------------------------------------------
	col1,col2 = st.columns([1,9])
	with col1: st.subheader('Overlays')
	st.markdown("""---""")
	
	col1,col2,col3,col4,col5,col6 = st.columns([1,1,1,1,1,1])
	
	with col1: render_moving_average(scope, 'sma_1')
	with col2: render_moving_average(scope, 'sma_2')
	with col3: render_moving_average(scope, 'sma_3')
	
	with col1: render_moving_average(scope, 'ema_1')
	with col2: render_moving_average(scope, 'ema_2')
	with col3: render_moving_average(scope, 'ema_3')

	with col4: render_bollinger_bands(scope)
	with col5: render_dividends(scope)
	with col5: render_announcements(scope)
	

def render_primary_chart(scope, column_adder):
	st.write('.')
	render_activate_metric(scope, column_adder)



