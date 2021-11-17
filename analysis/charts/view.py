import streamlit as st

from view.scope_var import three_cols



# https://www.investopedia.com/investing/market-reversals-and-how-spot-them/

def view_chart(scope):
	
	st.subheader('User Charts Selections and Settings  (Applies to all Analysis pages)')
	
	col1,col2,col3 = st.columns(3)
	
	
	with col1: st.subheader('Primary Charts')
	with col1: scope.charts['candlestick']['display'] 	= st.checkbox('CandleStick (tech indicators)', value=scope.charts['candlestick']['display'])
	with col1: scope.charts['scatter']['display'] 		= st.checkbox('Scatter (tech indicators)', value=scope.charts['scatter']['display'])
	with col1: scope.charts['bar']['display'] 			= st.checkbox('Bar (tech indicators)', value=scope.charts['bar']['display'])
	with col1: scope.charts['line']['display'] 			= st.checkbox('Line charts (tech indicators)', value=scope.charts['line']['display']) 		# TODO I tried embedding the params in the line grpah - see if this works
	with col1: scope.charts['heiken_ashi']['display'] 	= st.checkbox('Heikin Ashi (tech indicators)', value=scope.charts['heiken_ashi']['display'])

	with col2: st.subheader('Secondary Charts')
	with col2: scope.charts['volume']['display'] 		= st.checkbox('Volume  (None)', value=scope.charts['volume']['display'])
	with col2: scope.charts['macd']['display'] 			= st.checkbox('MACD (charts sepecific params)', value=scope.charts['macd']['display'])
	with col2: scope.charts['stochastic']['display'] 	= st.checkbox('Stochastic (charts sepecific params)', value=scope.charts['stochastic']['display'])
	with col2: scope.charts['rsi']['display'] 			= st.checkbox('RSI (charts sepecific params)', value=scope.charts['rsi']['display'])
	with col2: scope.charts['vac']['display'] 			= st.checkbox('VAC  (None)', value=scope.charts['vac']['display'])
	with col2: scope.charts['vol_osssy']['display'] 	= st.checkbox('Volume Oscillator   (charts sepecific params)', value=scope.charts['vol_osssy']['display'])
	
	
	# # Overlayed on Primary charts (maybe these are our technical indicators)
	# with col3: st.subheader('Technical Indicators')
	# with col3: st.write('applied to Primary Charts')
	# # with col3: 
	# with col3: scope.charts['ichi_moku'] 	= st.checkbox('Ichi Moku', value=scope.charts['ichi_moku'])
	# with col3: scope.charts['dividends'] = st.checkbox('add Dividends', value=scope.charts['dividends'])
	# with col3: scope.charts['announcements'] = st.checkbox('add Announcements', value=scope.charts['announcements'])
	# with col3: st.write('EMA')
	# with col3: st.write('SMA')
	# with col3: st.write('WMA - check if useful')
	# with col3: st.write('Volume by Price - check if useful')
	# with col3: st.write('Daily Ichi Moku')
	# with col3: st.write('Volume Per Minute - might be an indicator')

	st.markdown("""---""")


def view_technical_indicators(scope):
	col1,col2,col3 = st.columns(3)


	with col1: scope.charts['ti_bollinger_bands'] = st.checkbox('Bollinger Bands', value=scope.charts['bollinger_bands'])



