import streamlit as st

from view.scope_var import three_cols



# https://www.investopedia.com/investing/market-reversals-and-how-spot-them/

def view_chart(scope):
	
	st.subheader('User Chart Selections (for all pages')
	
	col1,col2,col3 = st.columns(3)
	
	
	with col1: st.subheader('Primary Charts')
	with col1: scope.chart['candlestick'] 	= st.checkbox('CandleStick', value=scope.chart['candlestick'])
	with col1: st.write('Scatter')
	with col1: st.write('Bar')
	with col1: scope.chart['line'] 			= st.checkbox('Line Chart', value=scope.chart['line'])
	with col1: scope.chart['heiken_ashi'] 	= st.checkbox('Heikin Ashi', value=scope.chart['heiken_ashi'])

	with col2: st.subheader('Secondary Charts')
	with col2: st.write('rendered in additional to Primary - no other indicators')
	with col2: scope.chart['volume'] 			= st.checkbox('Volume', value=scope.chart['volume'])
	with col2: scope.chart['macd'] 				= st.checkbox('MACD', value=scope.chart['macd'])
	with col2: scope.chart['stochastic'] 		= st.checkbox('Stochastic', value=scope.chart['stochastic'])
	with col2: scope.chart['rsi'] 				= st.checkbox('RSI', value=scope.chart['rsi'])
	with col2: scope.chart['vac'] 				= st.checkbox('VAC', value=scope.chart['vac'])
	with col2: scope.chart['vol_osclillator'] 	= st.checkbox('Volume Oscillator', value=scope.chart['vol_osclillator'])
	with col2: st.write('Volume Per Minute - might be an indicator')
	
	# Overlayed on Primary Chart (maybe these are our technical indicators)
	with col3: st.subheader('Technical Indicators')
	with col3: st.write('applied to Primary Charts')
	with col3: scope.chart['bollinger_bands'] = st.checkbox('add Bollinger Bands', value=scope.chart['bollinger_bands'])
	with col3: scope.chart['ichi_moku'] 	= st.checkbox('Ichi Moku', value=scope.chart['ichi_moku'])
	with col3: scope.chart['dividends'] = st.checkbox('add Dividends', value=scope.chart['dividends'])
	with col3: scope.chart['announcements'] = st.checkbox('add Announcements', value=scope.chart['announcements'])
	with col3: st.write('EMA')
	with col3: st.write('SMA')
	with col3: st.write('WMA - check if useful')
	with col3: st.write('Volume by Price - check if useful')
	with col3: st.write('Daily Ichi Moku')

	st.markdown("""---""")

	st.subheader('Charting Parameters')
	three_cols( 'Chart Line', scope.chart_lines, 'chart_lines' )
	three_cols( 'Chart MACD on Price', scope.chart_macd_on_price, 'chart_macd_on_price' )
	three_cols( 'Chart MACD on Volume', scope.chart_macd_on_volume, 'chart_macd_on_volume' )



