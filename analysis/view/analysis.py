import streamlit as st

from pages.view.three_cols import three_cols


from charts.view.partials import render_volume_oscillator
from analysis.view.partials import render_ohlcv_trend


def view_analysis(scope):
	st.header('Analysis Measures')
	three_cols( 'Limit for the Number of (recent) rows in any Analysis', scope.analysis_row_limit, 'analysis_row_limit' )
	st.markdown("""---""")

	col1,col2,col3,col4,col5,col6,col7,col8 = st.columns([1.5,0.5,1,1,1,1,1,1])
	
	with col1: render_ohlcv_trend(scope, 'trend_close')
	# 	st.markdown('##### Charts without additional Variables')
	# 	render_activate_chart(scope, 'volume')
	# 	render_activate_chart(scope, 'vac')
	# 	render_activate_chart(scope, 'vol_per_minute')
	# # with col2: 
	# with col3: render_macd(scope)