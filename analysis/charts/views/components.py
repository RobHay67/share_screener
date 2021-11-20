import streamlit as st


from analysis.charts.views.helpers import edit_active, edit_number, edit_ohlcv, edit_price, edit_colour

# -------------------------------------------------------------------------------------------------------------------------------------
# Primary and Secondary Charts
# -------------------------------------------------------------------------------------------------------------------------------------

def render_activate_chart(scope, chart):
	edit_active(scope, chart)
# -------------------------------------------------------------------------------------------------------------------------------------
# Primary Chart Components
# -------------------------------------------------------------------------------------------------------------------------------------
def render_primary_chart(scope, chart):
	st.write('.')
	render_activate_chart(scope, chart)
	
def render_primary_chart_height(scope):

	# st.subheader('Chart Height (pixels)')

	previous_selection = int(scope.primary_chart_height)

	input_chart_height = st.number_input( 	
										'Primary Chart Height', 
										min_value=0, 
										value=previous_selection,
										key='95'
										)  
	scope.primary_chart_height = input_chart_height

# -------------------------------------------------------------------------------------------------------------------------------------
# Overlays
# -------------------------------------------------------------------------------------------------------------------------------------
def render_moving_average(scope, chart):  # SMA or EMA
	edit_active(scope, chart)
	edit_number(scope, chart, 'periods' )
	edit_price(scope, chart )
	edit_colour(scope, chart )
	st.markdown("""---""")

def render_bollinger_bands(scope):
	# st.markdown('##### Bollinger Bands')
	chart = 'bollinger_bands'
	edit_active(scope, chart)
	edit_price(scope, chart )
	edit_number(scope, chart, 'length' )
	edit_number(scope, chart, 'shift_up' )
	edit_number(scope, chart, 'shift_down' )
	st.subheader('Moving Average Type - Rob to configure')		# TODO - Simple, Weighted, Exponential, Wilders
	st.markdown("""---""")

def render_dividends(scope):
	# st.markdown('##### Dividends')
	edit_active(scope, 'dividends')
	st.markdown("""---""")

def render_announcements(scope):
	# st.markdown('##### Announcements')
	edit_active(scope, 'announcements')
	st.markdown("""---""")
# -------------------------------------------------------------------------------------------------------------------------------------
# Secondary Charts
# -------------------------------------------------------------------------------------------------------------------------------------

def render_macd(scope):
	st.markdown('##### Moving Average, Convergence, Divergence (MACD)')
	chart = 'macd'
	edit_active(scope, chart)
	edit_price(scope, chart )
	edit_number(scope, chart, 'long' )
	edit_number(scope, chart, 'short' )
	edit_number(scope, chart, 'signal' )
	st.markdown("""---""")

def render_rsi(scope):
	st.markdown('##### Relative Strength Index (RSI)')
	chart = 'rsi'
	edit_active(scope, chart)
	edit_ohlcv(scope, chart )
	edit_number(scope, chart, 'periods' )
	st.markdown("""---""")

def render_stochastic(scope):
	st.markdown('##### Stochastic Oscillator')
	chart = 'stochastic'
	edit_active(scope, chart)
	# edit_price(scope, chart )
	edit_number(scope, chart, 'lookback_days' )
	edit_number(scope, chart, 'slow' )
	edit_number(scope, chart, 'signal' )
	st.markdown("""---""")

def render_volume_oscillator(scope):
	st.markdown('##### Volume Oscillator')
	chart = 'vol_osssy'
	edit_active(scope, chart)
	edit_number(scope, chart, 'fast' )
	edit_number(scope, chart, 'slow' )
	st.markdown("""---""")







