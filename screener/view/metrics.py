
import streamlit as st





def view_metrics(scope):

	st.markdown("""---""")
	st.write('**Screener Criteria**')

	with st.expander(label='OHLCV', expanded=True):
		st.write('This will be the criteria')
		# st.header('This will be the metrics selection page')
		col1,col2,col3,col4,col5,col6,col7,col8 = st.columns([1,1,1,1,1,1,1,1])
	
		with col1: render_ohlcv_trend(scope, 'trend_open',   'open')
		with col2: render_ohlcv_trend(scope, 'trend_high',   'high')
		with col3: render_ohlcv_trend(scope, 'trend_low',    'low')
		with col4: render_ohlcv_trend(scope, 'trend_close',  'close')
		with col5: render_ohlcv_trend(scope, 'trend_volume', 'volume')

	
	with st.expander(label='Annual General Meeting', expanded=False):
		st.write('This will be the criteria')
	

	with st.expander(label='Divdends', expanded=False):
		st.write('This will be the criteria')


	with st.expander(label='Simple Moving Averages (SMA)', expanded=False):
		st.write('This will be the criteria')
	

	with st.expander(label='Relative Strength Index (RSI)', expanded=False):
		st.write('This will be the criteria')

	with st.expander(label='Stochastic Oscillato', expanded=False):
		st.write('This will be the criteria')

	with st.expander(label='Moving Average - Convergence / Divergence (MACD)', expanded=False):
		st.write('This will be the criteria')

	with st.expander(label='MACD - Volume', expanded=False):
		st.write('This will be the criteria')





from pages.view.three_cols import three_cols
from metrics.view.ohlcv_trend import render_ohlcv_trend




# def view_metrics(scope):
# 	st.header('Screener Metrics')
# 	three_cols( 'Limit for the Number of (recent) rows in each Analysis Page', scope.page_row_limit, 'page_row_limit' )
# 	st.markdown("""---""")

# 	col1,col2,col3,col4,col5,col6,col7,col8 = st.columns([1,1,1,1,1,1,1,1])
	
# 	with col1: render_ohlcv_trend(scope, 'trend_open',   'open')
# 	with col2: render_ohlcv_trend(scope, 'trend_high',   'high')
# 	with col3: render_ohlcv_trend(scope, 'trend_low',    'low')
# 	with col4: render_ohlcv_trend(scope, 'trend_close',  'close')
# 	with col5: render_ohlcv_trend(scope, 'trend_volume', 'volume')


# 	# 	st.markdown('##### Charts without additional Variables')
# 	# 	render_activate_metric(scope, 'volume')
# 	# 	render_activate_metric(scope, 'vac')
# 	# 	render_activate_metric(scope, 'vol_per_minute')
# 	# # with col2: 
# 	# with col3: render_macd(scope)