import streamlit as st

from widgets.chart_height import set_chart_height_primary
from apps.chart.config.active import render_activate_metric

from apps.chart.config.active import render_activate_metric
from apps.chart.config.macd import render_macd
from apps.chart.config.macd_vol import render_macd_vol
from apps.chart.config.rsi import render_rsi
from apps.chart.config.stochastic import render_stochastic
from apps.chart.config.volume_oscillator import render_volume_oscillator




def render_primary_charts_config(scope):

	# ----------------------------------------------------------------------
	# Primary Charts
	# ----------------------------------------------------------------------
	
	st.markdown("""---""")
	col1, col2, col3 = st.columns([5,2,5])
	with col1:
		st.subheader('Charts Config')
		st.caption('Tick to display the chart')
	with col2:set_chart_height_primary(scope)
	# st.markdown("""---""")

	col1, col2 = st.columns([10,5])
	with col1:render_primary_chart(scope, 'candlestick')
	with col1:render_primary_chart(scope, 'scatter')
	with col1:render_primary_chart(scope, 'bar')
	with col1:render_primary_chart(scope, 'line')
	with col1:render_primary_chart(scope, 'heiken_ashi')

	with col1: 
		render_activate_metric(scope, 'volume')
		render_activate_metric(scope, 'vac')
		render_activate_metric(scope, 'vol_per_minute')

	render_macd(scope)
	render_macd_vol(scope)
	render_rsi(scope)
	render_stochastic(scope)
	render_volume_oscillator(scope)

	st.markdown("""---""")






	

def render_primary_chart(scope, column_adder):
	render_activate_metric(scope, column_adder)





