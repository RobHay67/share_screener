import streamlit as st

from pages.view.three_cols import three_cols


# from charts.view.partials import render_volume_oscillator
from analysis.view.partials import render_ohlcv_trend


def view_analysis(scope):
	st.header('Analysis Measures')
	three_cols( 'Limit for the Number of (recent) rows in any Analysis', scope.analysis_row_limit, 'analysis_row_limit' )
	st.markdown("""---""")

	col1,col2,col3,col4,col5,col6,col7,col8 = st.columns([1,1,1,1,1,1,1,1])
	
	with col1: render_ohlcv_trend(scope, 'trend_open', 'open')
	with col2: render_ohlcv_trend(scope, 'trend_high', 'high')
	with col3: render_ohlcv_trend(scope, 'trend_low', 'low')
	with col4: render_ohlcv_trend(scope, 'trend_close', 'close')
	with col5: render_ohlcv_trend(scope, 'trend_volume', 'volume')


	# 	st.markdown('##### Charts without additional Variables')
	# 	render_activate_chart(scope, 'volume')
	# 	render_activate_chart(scope, 'vac')
	# 	render_activate_chart(scope, 'vol_per_minute')
	# # with col2: 
	# with col3: render_macd(scope)