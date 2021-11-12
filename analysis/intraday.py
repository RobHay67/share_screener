
import streamlit as st
import yfinance as yf
import pandas as pd
import datetime as dt

from indicators.indicators import line_sma

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Render Sections
# -------------------------------------------------------------------------------------------------------------------------------------------------------------


def add_sma(scope):
	ticker 		= scope.ticker_for_intraday
	share_data 	= scope.share_data_files[ticker]
	
	st.info('Adding an SMA to this dataframe')

	# line_sma( params, share_df, column, no_of_days=10 ):
	share_data['test'] = 'this is a test'


def alternative_indicators(scope):
	st.number_input('Pick a number', 0, 10)
	st.slider('Pick a number', 0, 100)
	st.select_slider('Pick a size', ['S', 'M', 'L'])
	st.text_input('First name')
	st.text_area('Text to translate')


	col1,col2,col3,col4,col5,col6,col7 = st.columns([1.5,1,1,1,1,1,1])

	with col1: st.write('Add Measure to Ticker Data')
	with col2: st.write('Days')
	with col3: st.write('OHLC-V')
	with col4: st.write('ADD MEASURE')



	with col1: st.subheader('Simple Moving Average (SMA)')
	with col2: sma_days = st.number_input('', 1, 1000, 10,key='9223209')					# we might be able to limit this to the lenght of the share data??
	with col3: sma_cols = st.multiselect('s', scope.dropdown_ticker_columns, default='close', help='choose a column', key='sma_cols11')
	with col4: sma_button = st.button('Add SMA', key='3409823042')


def indicator_selectors(scope):

	# ticker = scope.ticker_for_intraday

	st.write('Add Indicators to the Chart for ' + '') 

	# Ensure we have some share data before attempting to do any of the following
	# if ticker in list(scope.share_data_files.keys()):
		# share_data = scope.share_data_files[ticker]

	# Add Buttons
	col1,col2,col3,col4,col5,col6,col7 = st.columns([1,1,1,1,1,1,1])

	with col1: st.subheader('Simple Moving Average (SMA)')
	with col1: sma_days = st.number_input('no of days', min_value=1, max_value=1000, value=10, key='10')
	with col1: sma_cols = st.multiselect('column(s)', scope.dropdown_ticker_columns, default='close', help='choose a column', key='11')
	with col1: sma_button = st.button('Add SMA')

	with col2: st.subheader('Exponetial Moving Average (EMA)')
	with col2: st.ema_days = st.number_input('no of days', min_value=1, max_value=1000, value=10, key='20') 
	with col2: ema_cols = st.multiselect('column(s)', scope.dropdown_ticker_columns, default='close', help='choose a column', key='21')
	with col2: ema_button = st.button('Add EMA')

	with col3: st.subheader('Moving Average Convergence Divergence (MACD)')
	with col3: macd_short_days = st.number_input('short period', min_value=1, max_value=1000, value=12, key='30')
	with col3: macd_long_days = st.number_input('long period', min_value=1, max_value=1000, value=26, key='31')
	with col3: macd_signal_days = st.number_input('signal line', min_value=1, max_value=1000, value=9, key='32')
	with col3: macd_cols = st.multiselect('column(s)', scope.dropdown_ticker_columns, default='close', help='choose a column', key='33')
	with col3: macd_button = st.button('Add MACD')			
	
	with col4: st.subheader('Relative Strength Index (RSI)')
	with col4: rsi_days = st.number_input('no of days', min_value=1, max_value=1000, value=14, key='41')
	with col4: rsi_cols = st.multiselect('column(s)', scope.dropdown_ticker_columns, default='close', help='choose a column', key='42')
	with col4: rsi_button = st.button('Add RSI')

	with col5: st.subheader('Recent Price Movements (RPM)')
	with col5: rpm_days = st.number_input('lookback days', min_value=1, max_value=1000, value=5, key='51')
	with col5: rpm_button = st.button('Add VPM')

	with col6: st.subheader('Stochastic Oscillator (SO)')
	with col6: so_days = st.number_input('lookback days', min_value=1, max_value=1000, value=14, key='60')
	with col6: so_slow_days = st.number_input('slow K', min_value=1, max_value=1000, value=3, key='61')
	with col6: so_signal_days = st.number_input('signal', min_value=1, max_value=1000, value=3, key='62')
	with col6: so_button = st.button('Add SO')			



	with col7: vpm_button = st.button('Add Volume Per Minute')		
		# def volume_per_minute(params, share_df, ticker ):


	if sma_button: add_sma(scope)



# X  trend lines
# 1  def line_sma( params, share_df, column, no_of_days=10 ):   
# 2  def line_ema( params, share_df, column, no_of_days, temp_ema=False ):
# 99 def volume_per_minute(params, share_df, ticker ):
# # Complex Measures
# def trend_sma_50_low( params, share_df ):
# 5  def recent_price_moves( params, share_df, lookback_days=5 ):
# 3  def macd( params, share_df, short=12, long=26, signal=9):
# def highs_and_lows( params, share_df ):
# X  Momentum Oscillation
# 4  def rsi( params, share_df, no_of_days=14 ):
# 6  def stochastic_oscillator(params, share_df, lookback_days=14, slow_k=3, signal=3):
# # Technical Analysis measures (traditional)
# x def add_rsi( params, share_df, column, no_of_days=14):
# X  Trend Line Columns - Naming Convention Helpers - what was the original column name
# def determine_original_column_name( column ):



