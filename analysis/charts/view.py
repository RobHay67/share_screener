import streamlit as st

# https://www.investopedia.com/investing/market-reversals-and-how-spot-them/

def view_charts(scope):
	
	st.subheader('User Charts Selections and Settings  (Applies to all Analysis pages)')
	
	col1,col2,col3,col4,col5 = st.columns([1,1,1,1,1])
	
	with col1: 
		st.subheader('_')
		view_chart(scope, 'candlestick')
		view_chart(scope, 'scatter')
	with col2: 
		st.subheader('Primary Charts')	
		view_chart(scope, 'bar')
		view_chart(scope, 'line')  		# TODO I tried embedding the data_cols in the line grpah - see if this works
	with col3:
		st.subheader('_')	
		view_chart(scope, 'heiken_ashi')
	with col4:
		st.subheader('Secondary Charts')
		view_chart(scope, 'volume')
		view_chart(scope, 'vac')
	with col5:
		st.subheader('Secondary Charts')
		view_chart(scope, 'vol_per_minute')

	st.markdown("""---""")
	
	col1,col2,col3,col4,col5 = st.columns([1,1,1,1,1])

	with col1: 
		st.markdown('##### Simple Moving Averages (SMA)')
		view_moving_average(scope, 'sma_1')
		view_moving_average(scope, 'sma_2')
		view_moving_average(scope, 'sma_3')
	with col2:
		st.markdown('##### Exponential Moving Averages (EMA)')
		view_moving_average(scope, 'ema_1')
		view_moving_average(scope, 'ema_2')
		view_moving_average(scope, 'ema_3')
	with col3:
		view_dividends(scope)
		view_announcements(scope)
		view_bollinger_bands(scope)

	with col4: view_macd(scope)
	with col4: view_rsi(scope)
	with col5: view_stochastic(scope)
	with col5: view_volume_oscillator(scope)

	print( 'scope.rebuild_plot_df = ', scope.rebuild_plot_df)
# -------------------------------------------------------------------------------------------------------------------------------------
# view Contollers
# -------------------------------------------------------------------------------------------------------------------------------------
def view_chart(scope, chart):
	active_control(scope, chart)

def view_volume_oscillator(scope):
	st.markdown('##### Volume Oscillator')
	chart = 'vol_osssy'
	active_control(scope, chart)
	edit_number(scope, chart, 'fast' )
	edit_number(scope, chart, 'slow' )
	st.markdown("""---""")

def view_stochastic(scope):
	st.markdown('##### Stochastic Oscillator')
	chart = 'stochastic'
	active_control(scope, chart)
	# edit_price(scope, chart )
	edit_number(scope, chart, 'lookback_days' )
	edit_number(scope, chart, 'slow' )
	edit_number(scope, chart, 'signal' )
	st.markdown("""---""")

def view_macd(scope):
	st.markdown('##### Moving Average, Convergence, Divergence (MACD)')
	chart = 'macd'
	active_control(scope, chart)
	edit_price(scope, chart )
	edit_number(scope, chart, 'long' )
	edit_number(scope, chart, 'short' )
	edit_number(scope, chart, 'signal' )
	st.markdown("""---""")

def view_rsi(scope):
	st.markdown('##### Relative Strength Index (RSI)')
	chart = 'rsi'
	active_control(scope, chart)
	edit_ohlcv(scope, chart )
	edit_number(scope, chart, 'periods' )
	st.markdown("""---""")

def view_moving_average(scope, chart):
	active_control(scope, chart)
	edit_number(scope, chart, 'periods' )
	edit_price(scope, chart )
	st.markdown("""---""")

def view_bollinger_bands(scope):
	st.markdown('##### Relative Strength Index (RSI)')
	chart = 'bollinger_bands'
	active_control(scope, chart)
	edit_price(scope, chart )
	edit_number(scope, chart, 'length' )
	edit_number(scope, chart, 'shift_up' )
	edit_number(scope, chart, 'shift_down' )
	st.subheader('Moving Average Type - Rob to configure')		# TODO - Simple, Weighted, Exponential, Wilders
	st.markdown("""---""")

def view_dividends(scope):
	st.markdown('##### Dividends')
	active_control(scope, 'dividends')
	st.markdown("""---""")

def view_announcements(scope):
	st.markdown('##### Announcements')
	active_control(scope, 'announcements')
	st.markdown("""---""")

# -------------------------------------------------------------------------------------------------------------------------------------
# Helpers
# -------------------------------------------------------------------------------------------------------------------------------------


def active_control(scope, chart ):		# NOTE : sets the scope.charts_changed value to TRUE which can be utilised by the analysis_df builder
	display_name = scope.charts[chart]['name']

	previous_active_status = scope.charts[chart]['active']
	new_active_status = st.checkbox( 
								display_name, 
								value=previous_active_status,
								)
	scope.charts[chart]['active'] = new_active_status
	if new_active_status == True and previous_active_status == False:
		# print('-'*100)
		# print(chart, ' forced an update to scope.charts_changed == TRUE') # TODO - remove later
		scope.rebuild_plot_df = True

def edit_number(scope, chart, column ):
	display_name = scope.charts[chart]['name']
	column_name = column.capitalize()
	# previous_period = int(scope.charts[chart]['data_cols'][column])
	previous_period = int(scope.charts[chart]['data_cols'][column])
	input_period_no = st.number_input(
										# column_name,
										label=(column_name + ' for ' + display_name), 
										min_value=0, 
										value=previous_period,
										key=display_name
										)  
	scope.charts[chart]['data_cols'][column] = input_period_no
	if input_period_no != previous_period:
		# print('-'*100)
		# print(chart, ' forced an update to scope.charts_changed == TRUE') # TODO - remove later
		scope.rebuild_plot_df = True

def edit_ohlcv(scope, chart ):
	display_name = scope.charts[chart]['name']
	previous_column = scope.charts[chart]['data_cols']['column']
	selected_column = st.selectbox ( 
									label=('Column for ' + display_name), 
									options=scope.dropdown_ohlcv_columns,
									index=scope.dropdown_ohlcv_columns.index(previous_column), 
									key=chart,
									) 
	scope.charts[chart]['data_cols']['column'] = selected_column
	if selected_column != previous_column:
		scope.rebuild_plot_df = True

def edit_price(scope, chart ):
	display_name = scope.charts[chart]['name']
	previous_column = scope.charts[chart]['data_cols']['column']
	selected_column = st.selectbox ( 
									label=('Column for ' + display_name), 
									options=scope.dropdown_price_columns,
									index=scope.dropdown_price_columns.index(previous_column), 
									key=chart,
									) 
	scope.charts[chart]['data_cols']['column'] = selected_column
	if selected_column != previous_column:
		scope.rebuild_plot_df = True






	
# with col1: st.subheader('Primary Charts')
# for chart in scope.charts.keys():
# 	if scope.charts[chart]['primary'] == True:
# 		with col1:
# 			scope.charts[chart]['active'] = st.checkbox(scope.charts[chart]['name'], value=scope.charts[chart]['active'])