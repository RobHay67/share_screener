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
		view_chart(scope, 'line')  		# TODO I tried embedding the params in the line grpah - see if this works
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
		view_ma(scope, 'sma_1')
		view_ma(scope, 'sma_2')
		view_ma(scope, 'sma_3')
	with col2:
		st.markdown('##### Exponential Moving Averages (EMA)')
		view_ma(scope, 'ema_1')
		view_ma(scope, 'ema_2')
		view_ma(scope, 'ema_3')
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
def view_chart(scope, dict_key):
	scope_dict = scope.charts
	active_control(scope, scope_dict, dict_key)

def view_volume_oscillator(scope):
	st.markdown('##### Volume Oscillator')
	scope_dict = scope.charts
	dict_key = 'vol_osssy'
	active_control(scope, scope_dict, dict_key)
	edit_number(scope, scope_dict, dict_key, 'fast' )
	edit_number(scope, scope_dict, dict_key, 'slow' )
	st.markdown("""---""")

def view_stochastic(scope):
	st.markdown('##### Stochastic Oscillator')
	scope_dict = scope.charts
	dict_key = 'stochastic'
	active_control(scope, scope_dict, dict_key)
	edit_column(scope, scope_dict, dict_key )
	edit_number(scope, scope_dict, dict_key, 'periods' )
	edit_number(scope, scope_dict, dict_key, 'slow' )
	edit_number(scope, scope_dict, dict_key, 'signal' )
	st.markdown("""---""")

def view_macd(scope):
	st.markdown('##### Moving Average, Convergence, Divergence (MACD)')
	scope_dict = scope.charts
	dict_key = 'macd'
	active_control(scope, scope_dict, dict_key)
	edit_column(scope, scope_dict, dict_key )
	edit_number(scope, scope_dict, dict_key, 'long' )
	edit_number(scope, scope_dict, dict_key, 'short' )
	edit_number(scope, scope_dict, dict_key, 'signal' )
	st.markdown("""---""")

def view_rsi(scope):
	st.markdown('##### Relative Strength Index (RSI)')
	scope_dict = scope.charts
	dict_key = 'rsi'
	active_control(scope, scope_dict, dict_key)
	edit_column(scope, scope_dict, dict_key )
	edit_number(scope, scope_dict, dict_key, 'periods' )
	st.markdown("""---""")

def view_ma(scope, dict_key):
	scope_dict = scope.measures
	active_control(scope, scope_dict, dict_key)
	edit_number(scope, scope_dict, dict_key, 'periods' )
	edit_column(scope, scope_dict, dict_key )
	st.markdown("""---""")

def view_bollinger_bands(scope):
	st.markdown('##### Relative Strength Index (RSI)')
	scope_dict = scope.measures
	dict_key = 'bollinger_bands'
	active_control(scope, scope_dict, dict_key)
	edit_column(scope, scope_dict, dict_key )
	edit_number(scope, scope_dict, dict_key, 'length' )
	edit_number(scope, scope_dict, dict_key, 'shift_up' )
	edit_number(scope, scope_dict, dict_key, 'shift_down' )
	st.subheader('Moving Average Type - Rob to configure')		# TODO - Simple, Weighted, Exponential, Wilders
	st.markdown("""---""")

def view_dividends(scope):
	st.markdown('##### Dividends')
	scope_dict = scope.measures
	dict_key = 'dividends'
	active_control(scope, scope_dict, dict_key)
	st.markdown("""---""")

def view_announcements(scope):
	st.markdown('##### Announcements')
	scope_dict = scope.measures
	dict_key = 'announcements'
	active_control(scope, scope_dict, dict_key)
	st.markdown("""---""")

# -------------------------------------------------------------------------------------------------------------------------------------
# Helpers
# -------------------------------------------------------------------------------------------------------------------------------------


def active_control(scope, scope_dict, dict_key ):		# NOTE : sets the scope.charts_changed value to TRUE which can be utilised by the analysis_df builder
	display_name = scope_dict[dict_key]['name']
	previous_active_status = scope_dict[dict_key]['active']
	new_active_status = st.checkbox( 
								display_name, 
								value=previous_active_status,
								)
	scope_dict[dict_key]['active'] = new_active_status
	if new_active_status == True and previous_active_status == False:
		# print('-'*100)
		# print(dict_key, ' forced an update to scope.charts_changed == TRUE') # TODO - remove later
		scope.rebuild_plot_df = True

def edit_number(scope, scope_dict, dict_key, column ):
	display_name = scope_dict[dict_key]['name']
	column_name = column.capitalize()
	previous_period = int(scope_dict[dict_key]['params'][column])
	input_period_no = st.number_input(
										# column_name,
										label=(column_name + ' for ' + display_name), 
										min_value=0, 
										value=previous_period,
										key=display_name
										)  
	scope_dict[dict_key]['params']['periods'] = input_period_no
	if input_period_no != previous_period:
		# print('-'*100)
		# print(dict_key, ' forced an update to scope.charts_changed == TRUE') # TODO - remove later
		scope.rebuild_plot_df = True

def edit_column(scope, scope_dict, dict_key ):
	display_name = scope_dict[dict_key]['name']
	previous_column = scope_dict[dict_key]['params']['column']
	selected_column = st.selectbox ( 
									label=('Column for ' + display_name), 
									options=scope.dropdown_ticker_columns,
									index=scope.dropdown_ticker_columns.index(previous_column), 
									key=dict_key,
									) 
	scope_dict[dict_key]['params']['column'] = selected_column
	if selected_column != previous_column:
		# print('-'*100)
		# print(dict_key, ' forced an update to scope.charts_changed == TRUE') # TODO - remove later
		scope.rebuild_plot_df = True








	
# with col1: st.subheader('Primary Charts')
# for chart in scope.charts.keys():
# 	if scope.charts[chart]['primary'] == True:
# 		with col1:
# 			scope.charts[chart]['active'] = st.checkbox(scope.charts[chart]['name'], value=scope.charts[chart]['active'])