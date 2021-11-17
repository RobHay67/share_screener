
apply = 'apply'					# True or False - is this technical Indicator is being applied to our Primary Chart?
chart = 'chart'					# True or False - param set if for a particular chart and cannot be applied to a Primary Chart 
params = 'params'				# None or dictionary of paramaters required for this techncial indicator
periods = 'periods'				# Most Indicators use a base number of days/hours (periods) for their calcs - store it here
column = 'column'				# OHLCV column required for calc
slow = 'slow'
fast = 'fast'
long = 'long'					# for the MACD
short = 'short'					# for the MACD
signal = 'signal'				# Signal line for some charts

tech_indicators = {
					'sma'		:{ apply:False, chart:False, params:{ periods:21  , column:'close' , fast:None, slow:None, long:None, short:None, signal:None } },
					'ema'		:{ apply:False, chart:False, params:{ periods:21  , column:'close' , fast:None, slow:None, long:None, short:None, signal:None } },
					'vol_min'	:{ apply:False, chart:False, params:{ periods:21  , column:'volume', fast:None, slow:None, long:None, short:None, signal:None } },
					'rsi'		:{ apply:False, chart:True , params:{ periods:10  , column:'close' , fast:None, slow:None, long:None, short:None, signal:None } },
					'stochastic':{ apply:False, chart:True , params:{ periods:14  , column:'close' , fast:None, slow:3   , long:None, short:None, signal:3    } },
					'macd'		:{ apply:False, chart:True , params:{ periods:None, column:'close' , fast:None, slow:None, long:26  , short:12  , signal:9    } },
					'vol_osssy'	:{ apply:False, chart:True , params:{ periods:None, column:'volume', fast:14  , slow:21  , long:None, short:None, signal:None } },				
}


def scope_tech_indicators(scope):
	# scope.chart_lines = []					# these are the technical indicator params so will move to that module
	# scope.chart_macd_on_price = {}			# these are the technical indicator params so will move to that module
	# scope.chart_macd_on_volume = {}			# these are the technical indicator params so will move to that module
	scope.tech_indicators = tech_indicators




	# with col1: st.subheader('Simple Moving Average (SMA)')
	# with col1: sma_days = st.number_input('no of days', min_value=1, max_value=1000, value=10, key='10')
	# with col1: sma_cols = st.multiselect('column(s)', scope.dropdown_ticker_columns, default='close', help='choose a column', key='11')
	# with col1: sma_button = st.button('Add SMA')

	# with col2: st.subheader('Exponetial Moving Average (EMA)')
	# with col2: st.ema_days = st.number_input('no of days', min_value=1, max_value=1000, value=10, key='20') 
	# with col2: ema_cols = st.multiselect('column(s)', scope.dropdown_ticker_columns, default='close', help='choose a column', key='21')
	# with col2: ema_button = st.button('Add EMA')

	# with col3: st.subheader('Moving Average Convergence Divergence (MACD)')
	# with col3: macd_short_days = st.number_input('short period', min_value=1, max_value=1000, value=12, key='30')
	# with col3: macd_long_days = st.number_input('long period', min_value=1, max_value=1000, value=26, key='31')
	# with col3: macd_signal_days = st.number_input('signal line', min_value=1, max_value=1000, value=9, key='32')
	# with col3: macd_cols = st.multiselect('column(s)', scope.dropdown_ticker_columns, default='close', help='choose a column', key='33')
	# with col3: macd_button = st.button('Add MACD')			
	
	# with col4: st.subheader('Relative Strength Index (RSI)')
	# with col4: rsi_days = st.number_input('no of days', min_value=1, max_value=1000, value=14, key='41')
	# with col4: rsi_cols = st.multiselect('column(s)', scope.dropdown_ticker_columns, default='close', help='choose a column', key='42')
	# with col4: rsi_button = st.button('Add RSI')

	# with col5: st.subheader('Recent Price Movements (RPM)')
	# with col5: rpm_days = st.number_input('lookback days', min_value=1, max_value=1000, value=5, key='51')
	# with col5: rpm_button = st.button('Add VPM')

	# with col6: st.subheader('Stochastic Oscillator (SO)')
	# with col6: so_days = st.number_input('lookback days', min_value=1, max_value=1000, value=14, key='60')
	# with col6: so_slow_days = st.number_input('slow K', min_value=1, max_value=1000, value=3, key='61')
	# with col6: so_signal_days = st.number_input('signal', min_value=1, max_value=1000, value=3, key='62')
	# with col6: so_button = st.button('Add SO')	