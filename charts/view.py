import streamlit as st

from view.scope_var import three_cols


def view_chart(scope):
	
	st.header('User Chart Selections (for all pages')
	
	col1,col2,col3,col4,col5,col6,col7 = st.columns(7)

	with col1: st.subheader('Candlestick Charts')
	with col1: scope.chart['candlestick'] = st.checkbox('CandleStick', value=scope.chart['candlestick'])
	with col1: scope.chart['heiken_ashi'] = st.checkbox('Heikin Ashi', value=scope.chart['heiken_ashi'])

	with col2: st.subheader('Momentum Charts')
	with col2: scope.chart['macd'] 			= st.checkbox('MACD', value=scope.chart['macd'])
	with col2: scope.chart['stochastic'] 	= st.checkbox('Stochastic', value=scope.chart['stochastic'])
	with col2: scope.chart['rsi'] 			= st.checkbox('RSI', value=scope.chart['rsi'])
	with col2: scope.chart['ichi_moku'] 	= st.checkbox('Ichi Moku', value=scope.chart['ichi_moku'])

	with col3: st.subheader('Trend Following')
	with col3: scope.chart['bollinger_bands'] = st.checkbox('add Bollinger Bands', value=scope.chart['bollinger_bands'])

	with col4: st.subheader('Volume Charts')
	with col4: scope.chart['volume'] = st.checkbox('Volume', value=scope.chart['volume'])
	with col4: scope.chart['vac'] = st.checkbox('VAC', value=scope.chart['vac'])
	with col4: scope.chart['vol_osclillator'] = st.checkbox('Volume Oscillator', value=scope.chart['vol_osclillator'])

	with col5: st.subheader('Basic Charts')
	with col5: scope.chart['line'] = st.checkbox('Line Chart', value=scope.chart['line'])

	with col6: st.subheader('Special Charts')
	with col6: scope.chart['dividends'] = st.checkbox('add Dividends', value=scope.chart['dividends'])
	with col6: scope.chart['announcements'] = st.checkbox('add Announcements', value=scope.chart['announcements'])

	st.markdown("""---""")

	st.subheader('Charting Parameters')
	three_cols( 'Chart Line', scope.chart_lines, 'chart_lines' )
	three_cols( 'Chart MACD on Price', scope.chart_macd_on_price, 'chart_macd_on_price' )
	three_cols( 'Chart MACD on Volume', scope.chart_macd_on_volume, 'chart_macd_on_volume' )



