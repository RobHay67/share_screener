import streamlit as st


from apps.chart.config.active import render_activate_metric

from widgets.chart_height import set_chart_height_primary

def render_primary_charts_config(scope):

	# ----------------------------------------------------------------------
	# Primary Charts
	# ----------------------------------------------------------------------
	
	st.markdown("""---""")
	col1, col2 = st.columns([10,5])
	with col1:st.subheader('Primary Charts')
	with col2:set_chart_height_primary(scope)
	st.markdown("""---""")

	col1, col2 = st.columns([10,5])
	# col1, col2 = st.columns([2,10])
	with col1:render_primary_chart(scope, 'candlestick')
	with col1:render_primary_chart(scope, 'scatter')
	with col1:render_primary_chart(scope, 'bar')
	with col1:render_primary_chart(scope, 'line')
	with col1:render_primary_chart(scope, 'heiken_ashi')

	st.markdown("""---""")




	

def render_primary_chart(scope, column_adder):
	# st.write('.')
	render_activate_metric(scope, column_adder)






	# col1,col2,col3,col4,col5,col6,col7 = st.columns([1,1,1,1,1,1,1])
	
	# with col1: st.header('Primary Charts')
	# with col2: st.write('.')
	# with col2: st.write('.')
	# with col2: set_chart_height_primary(scope)

	# with col3: render_primary_chart(scope, 'candlestick')
	# with col4: render_primary_chart(scope, 'scatter')
	# with col5: render_primary_chart(scope, 'bar')
	# with col6: render_primary_chart(scope, 'line')
	# with col7: render_primary_chart(scope, 'heiken_ashi')
	
	# st.markdown("""---""")
