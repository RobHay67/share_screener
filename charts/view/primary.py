import streamlit as st


from charts.view.partials import render_announcements
from charts.view.partials import render_bollinger_bands
from charts.view.partials import render_dividends
from charts.view.partials import render_moving_average
from charts.view.partials import render_primary_chart

from config.model.set_chart_height import set_primary_chart_height


def view_primary(scope):


	schema = scope.charts

	# ----------------------------------------------------------------------
	# Primary Charts
	# ----------------------------------------------------------------------

	col1,col2,col3,col4,col5,col6,col7 = st.columns([1,1,1,1,1,1,1])
	with col1: st.header('Primary Charts')
	with col2: st.write('.')
	with col2: st.write('.')
	with col2: set_primary_chart_height(scope)

	with col3: render_primary_chart(scope, 'candlestick')
	with col4: render_primary_chart(scope, 'scatter')
	with col5: render_primary_chart(scope, 'bar')
	with col6: render_primary_chart(scope, 'line')					# TODO I tried embedding the data_cols in the line grpah - see if this works
	with col7: render_primary_chart(scope, 'heiken_ashi')
	
	st.markdown("""---""")
	col1,col2 = st.columns([1,9])
	with col1: st.subheader('Overlays')
	st.markdown("""---""")

	# ----------------------------------------------------------------------
	# Overlays
	# ----------------------------------------------------------------------
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
	



