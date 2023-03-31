import streamlit as st

from widgets.chart_height import set_chart_height_primary
from apps.chart.config.active import render_activate_metric

from apps.chart.config.active import render_activate_metric
from apps.chart.config.macd import render_macd
from apps.chart.config.macd_vol import render_macd_vol
from apps.chart.config.rsi import render_rsi
from apps.chart.config.stochastic import render_stochastic
from apps.chart.config.volume_oscillator import render_volume_oscillator
from widgets.save_user_settings import save_user_settings_button



def render_available_charts(scope):

	# ----------------------------------------------------------------------
	# Primary Charts
	# ----------------------------------------------------------------------
	
	st.markdown("""---""")
	col1,col2,col3 = st.columns([6,3,2])
	with col1:
		st.subheader('Charts Config')
		st.caption('Tick to display chart')
	with col2:
		set_chart_height_primary(scope)
	with col3:
		save_user_settings_button(scope)

	col1,col2,col3 = st.columns(3)
	with col1:
		render_activate_metric(scope, 'candlestick')
		render_activate_metric(scope, 'scatter')
		render_activate_metric(scope, 'bar')
	with col2: 
		render_activate_metric(scope, 'line')
		render_activate_metric(scope, 'heiken_ashi')
		render_activate_metric(scope, 'VWAP')
	with col3:
		render_activate_metric(scope, 'volume')
		render_activate_metric(scope, 'vac')
		render_activate_metric(scope, 'vol_per_minute')

	st.markdown("""---""")

	st.caption('Charts with additional configuration')
	render_macd(scope)
	render_macd_vol(scope)
	render_rsi(scope)
	render_stochastic(scope)
	render_volume_oscillator(scope)

	st.markdown("""---""")








