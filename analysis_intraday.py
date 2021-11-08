
import streamlit as st
import yfinance as yf
import pandas as pd
import datetime as dt
import plotly.graph_objects as go

# import matplotlib.pyplot as plt
# from matplotlib.pylab import date2num
# from mplfinance.original_flavor import candlestick_ohlc
import mplfinance as mpf


from indicators import line_sma

# from ticker_data import load_ticker_data_files, load_and_download_ticker_data
from ticker_loader import render_selectors_for_single_ticker, render_ticker_data_file

# TODO - Rob - just work on the end of day data and when we get this working we can wire in the 5 minute data


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



# ==============================================================================================================================================================
# Daily Analysis Render Controller
# ==============================================================================================================================================================

def render_intraday_analysis_page(scope):
	st.header('Intra-Day Analysis')
	# render_selectors_for_single_ticker(scope, 'ticker_for_intraday' )
	render_selectors_for_single_ticker(scope, 'intraday')
	st.markdown("""---""")

	# ticker = scope.ticker_for_intraday
	ticker = scope.ticker['intraday']

	if ticker != 'select a ticker':	
		
		# plot_candlestick(scope)
		plot_basic_chart(scope)
	# 	render_indicator_selectors(scope)
		# render_ticker_data(scope)
		render_ticker_data_file(scope, ticker)
		

	
	



def add_sma(scope):
	ticker 		= scope.ticker_for_intraday
	share_data 	= scope.share_data_files[ticker]
	
	st.info('Adding an SMA to this dataframe')

	# line_sma( params, share_df, column, no_of_days=10 ):
	share_data['test'] = 'this is a test'






# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Render Sections
# -------------------------------------------------------------------------------------------------------------------------------------------------------------


# def company_profile_ticker_selector(scope):
# 	col1,col2,col3,col4 = st.columns([2,2,2,6])							# col2=4 is just a dummy to prevent the widget filling the whole screen
	
# 	dropdown_list = scope.dropdown_ticker
# 	index_of_ticker = dropdown_list.index(scope.ticker_for_intraday)

# 	with col1: 
# 		ticker = st.selectbox ( 'Select Ticker', 
# 								dropdown_list, 
# 								index=index_of_ticker, 
# 								help='Select a ticker. Start typing to jump within list'
# 								) 
# 	with col3: load_tickers = st.button('Load Share Data File')
# 	with col3: download_tickers = st.button( ( 'Download Previous ' + str(int(st.download_days)) + ' days') )

# 	scope.ticker_for_intraday = ticker									# Store the selection for next session
	
# 	if ticker != 'select a ticker':	
# 		st.header( scope.ticker_index_file.loc[ticker]['company_name'] )	

# 	if load_tickers : 
# 		load_ticker_data_files(scope, [ticker])

# 	if download_tickers:
# 		st.warning('Need to configure the share downloader')


def plot_basic_chart(scope):
	
	ticker = scope.ticker['intraday']

	st.write('Chart of all available ' + ticker + ' data') 

	if ticker in list(scope.share_data_files.keys()):
		share_data = scope.share_data_files[ticker]
		fig = go.Figure(
				data=go.Scatter(x=share_data['date'], y=share_data['close'])
			)

		print(fig)
		fig.update_layout(
			title={
				'text': "Stock Prices Over Past ??????? Years",
				'y':0.9,
				'x':0.5,
				'xanchor': 'center',
				'yanchor': 'top'})
		st.plotly_chart(fig, use_container_width=True)

		# start = dt.datetime.today()-dt.timedelta(2 * 365)
		# end = dt.datetime.today()
		# df = yf.download(ticker,start,end)
		# df = df.reset_index()
		# fig = go.Figure(
		# 		data=go.Scatter(x=df['Date'], y=df['Adj Close'])
		# 	)

		st.warning('ROB to change chart to candlestick and maybe add a widget for the date range')
	else:
		st.error('Load / Download some ticker data')



# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Render Candlestick Chart
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

def plot_candlestick(scope):
	ticker = scope.ticker['intraday']
	st.write('Chart of all available ' + ticker + ' data < candle stick format >') 
	if ticker in list(scope.share_data_files.keys()):
		plot_data = scope.share_data_files[ticker].copy()

		plot_data.set_index('date', inplace=True)

		# print(plot_data)
		# print(plot_data.dtypes)

		# fig = mpf.Figure(
		# 		data=go.Scatter(x=share_data['date'], y=share_data['close'])
		# 	)
		fig = mpf.figure(style='yahoo',figsize=(7,8))
		ax1 = fig.add_subplot(2,1,1)
		ax2 = fig.add_subplot(2,1,2)

		mpf.plot(plot_data,ax=ax1,volume=ax2, savefig='test-fig.png')


		mpf.plot(plot_data,volume=True,tight_layout=True,figscale=0.75)




		# ok - this works but only dumps to a PNG
		# Plot candlestick.
		# Add volume.
		# Add moving averages: 3,6,9.
		# Save graph to *.png.
		mpf.plot(plot_data, type='candle', style='charles',   # tight option??
					title='S&P 500, Nov 2019',
					ylabel='Price ($)',
					ylabel_lower='Shares \nTraded',
					volume=True, 
					mav=(3,6,9), 
					savefig='test-mplfiance.png',
					)

		# st.plotly_chart(fig, use_container_width=True)


		# st.info('Plot the Candlestick right here RObbie')

		# fig = plt.figure()

		# axes_candle = fig.add_axes((0, 0.72, 1, 0.32))              # The dimensions [left, bottom, width, height] of the new axes.
		# axes_candle.xaxis_date()                                    # Format x-axis ticks as dates

		# ohlc = []

		# for date, row in share_data.iterrows():
		# 	openp, highp, lowp, closep = row[:4]
		# 	ohlc.append([date2num(date), openp, highp, lowp, closep])

		# print (ohlc)
		# # axes_candle.set_title( ticker.upper() + ' - ' + params.share_index.at[ticker, 'company_name'] )
	
		# # for chart_line in scope.chart_lines: 
		# # 	axes_candle.plot( share_data.index, share_data[chart_line], label=chart_line )


		# candlestick_ohlc( axes_candle, ohlc, colorup='g', colordown='r', width=0.3 )


# this is the initial caller
# plot_chart( params, analysis_df, ticker )


def plot_chart( params, share_df, ticker ):
	# chart_df   = share_df.copy()
	# %matplotlib tk
	share_df = share_df.iloc[-params.analysis_no_of_days:]                        # Filter number of observations for plot
	
	# Create figure, set axes and plot the candlestick graph (always)
	fig = plt.figure()
	fig.set_size_inches((20, 10))   							# w / h
	# plt.style.use('dark_background')
	axes_candle = fig.add_axes((0, 0.72, 1, 0.32))              # The dimensions [left, bottom, width, height] of the new axes.
	axes_candle.xaxis_date()                                    # Format x-axis ticks as dates
	
	plot_candlestick( params, share_df, axes_candle, ticker )                       
   
	# Save the chart as PNG
#     fig.savefig("charts/" + ticker + ".png", bbox_inches="tight")
	
	plt.show()



def plot_candlestick_original( params, share_data, axes_candle, ticker ): 
	# Get nested list of date, open, high, low and close prices
	ohlc = []

	for date, row in share_data.iterrows():
		openp, highp, lowp, closep = row[:4]
		ohlc.append([date2num(date), openp, highp, lowp, closep])

	axes_candle.set_title( ticker.upper() + ' - ' + params.share_index.at[ticker, 'company_name'] )
	
	for chart_line in params.chart_lines: 
		axes_candle.plot( share_data.index, share_data[chart_line], label=chart_line )

    # ax_candle.scatter( share_df.index, share_df['trade_buy' ],   label = 'Buy',  marker = 'X', color = 'blue' )
    # ax_candle.scatter( share_df.index, share_df['trade_sell'],   label = 'Sell', marker = 'v', color = 'orange'   )
	
	candlestick_ohlc( axes_candle, ohlc, colorup='g', colordown='r', width=0.3 )
	axes_candle.legend()







def render_indicator_selectors(scope):

	ticker = scope.ticker_for_intraday

	st.write('Add Indicators to the Chart for ' + ticker + '') 

	# Ensure we have some share data before attempting to do any of the following
	if ticker in list(scope.share_data_files.keys()):
		share_data = scope.share_data_files[ticker]

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

