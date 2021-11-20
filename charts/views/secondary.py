import streamlit as st


from charts.views.components import render_activate_chart, render_macd, render_rsi, render_stochastic, render_volume_oscillator



def view_secondary(scope):
	st.header('Secondary Charts')
	st.write('appears on all single ticker analysis pages')
	
	st.markdown("""---""")

	col1,col2,col3,col4,col5,col6,col7 = st.columns([1.5,0.5,1,1,1,1,1])
	
	with col1: 
		st.markdown('##### Charts without additional Variables')
		render_activate_chart(scope, 'volume')
		render_activate_chart(scope, 'vac')
		render_activate_chart(scope, 'vol_per_minute')
	# with col2: 
	with col3: render_macd(scope)
	with col4: render_rsi(scope)
	with col5: render_stochastic(scope)
	with col6: render_volume_oscillator(scope)


