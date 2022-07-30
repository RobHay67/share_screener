import streamlit as st


from widgets.constructors.active import render_activate_metric
from widgets.constructors.macd import render_macd
from widgets.constructors.macd_vol import render_macd_vol
from widgets.constructors.rsi import render_rsi
from widgets.constructors.stochastic import render_stochastic
from widgets.constructors.volume_oscillator import render_volume_oscillator



def render_secondary_charts_config(scope):

	st.header('Secondary Charts')
	st.write('appears on all single ticker analysis pages')
	st.markdown("""---""")

	col1,col2,col3,col4,col5,col6,col7,col8 = st.columns([1.5,0.5,1,1,1,1,1,1])
	
	with col1: 
		st.markdown('##### Charts without additional Variables')
		render_activate_metric(scope, 'volume')
		render_activate_metric(scope, 'vac')
		render_activate_metric(scope, 'vol_per_minute')
	# with col2: 
	with col3: render_macd(scope)
	with col4: render_macd_vol(scope)
	with col5: render_rsi(scope)
	with col6: render_stochastic(scope)
	with col7: render_volume_oscillator(scope)


