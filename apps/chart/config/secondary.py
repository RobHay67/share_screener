import streamlit as st


from apps.chart.config.active import render_activate_metric
from apps.chart.config.macd import render_macd
from apps.chart.config.macd_vol import render_macd_vol
from apps.chart.config.rsi import render_rsi
from apps.chart.config.stochastic import render_stochastic
from apps.chart.config.volume_oscillator import render_volume_oscillator



def render_secondary_charts_config(scope):

	st.subheader('Secondary Charts')
	st.write('appears on all single ticker analysis pages')
	
	st.markdown("""---""")

	col1,col2,col3,col4,col5,col6,col7,col8 = st.columns([1.5,0.5,1,1,1,1,1,1])
	
	with col1: 
		st.markdown('##### Charts without additional Variables')
		render_activate_metric(scope, 'volume')
		render_activate_metric(scope, 'vac')
		render_activate_metric(scope, 'vol_per_minute')
		st.markdown("""---""")
	# with col2: 
	render_macd(scope)
	render_macd_vol(scope)
	render_rsi(scope)
	render_stochastic(scope)
	render_volume_oscillator(scope)


