import streamlit as st



# from config.model.set_chart_active import edit_active
from config.model.set_active import edit_active
from config.model.set_number import edit_number
from config.model.set_ohlcv import edit_ohlcv
from config.model.set_ohlcv import edit_price
from config.model.set_colour import edit_colour

# -------------------------------------------------------------------------------------------------------------------------------------
# Primary and Secondary Charts
# -------------------------------------------------------------------------------------------------------------------------------------

def render_activate_chart(scope, chart):
	edit_active(scope, 'charts', chart)


# -------------------------------------------------------------------------------------------------------------------------------------
# Primary Chart Components
# -------------------------------------------------------------------------------------------------------------------------------------
def render_primary_chart(scope, chart):
	st.write('.')
	render_activate_chart(scope, chart)
	


# -------------------------------------------------------------------------------------------------------------------------------------
# Secondary Charts
# -------------------------------------------------------------------------------------------------------------------------------------

def render_macd(scope):
	st.markdown('##### Moving Average, Convergence, Divergence (MACD)')
	chart = 'macd'
	edit_active(scope, 'charts', chart)
	edit_price(scope, 'charts', chart )
	edit_number(scope, 'charts', chart, 'long' )
	edit_number(scope, 'charts', chart, 'short' )
	edit_number(scope, 'charts', chart, 'signal' )
	st.markdown("""---""")

def render_macd_vol(scope):
	st.markdown('##### Moving Average, Convergence, Divergence (MACD) - Volume Only')
	chart = 'macd_vol'
	edit_active(scope, 'charts', chart)
	st.write('Column for MACD')
	st.write('Volume')
	edit_number(scope, 'charts', chart, 'long' )
	edit_number(scope, 'charts', chart, 'short' )
	edit_number(scope, 'charts', chart, 'signal' )
	st.markdown("""---""")

def render_rsi(scope):
	st.markdown('##### Relative Strength Index (RSI)')
	chart = 'rsi'
	edit_active(scope, 'charts', chart)
	edit_ohlcv(scope, 'charts', chart )
	edit_number(scope, 'charts', chart, 'lookback_days' )
	st.markdown("""---""")

def render_stochastic(scope):
	st.markdown('##### Stochastic Oscillator')
	chart = 'stochastic'
	edit_active(scope, 'charts', chart)
	# edit_price(scope, chart )
	edit_number(scope, 'charts', chart, 'lookback_days' )
	edit_number(scope, 'charts', chart, 'slow' )
	edit_number(scope, 'charts', chart, 'signal' )
	st.markdown("""---""")

def render_volume_oscillator(scope):
	st.markdown('##### Volume Oscillator')
	chart = 'vol_osssy'
	edit_active(scope, 'charts', chart)
	edit_number(scope, 'charts', chart, 'fast' )
	edit_number(scope, 'charts', chart, 'slow' )
	st.markdown("""---""")

# -------------------------------------------------------------------------------------------------------------------------------------
# Overlays
# -------------------------------------------------------------------------------------------------------------------------------------
def render_moving_average(scope, chart):  # SMA or EMA
	edit_active(scope, 'charts', chart)
	edit_number(scope, 'charts', chart, 'periods' )
	edit_price(scope, 'charts', chart )
	edit_colour(scope, 'charts', chart )
	st.markdown("""---""")

def render_bollinger_bands(scope):
	# st.markdown('##### Bollinger Bands')
	chart = 'bollinger_bands'
	edit_active(scope, 'charts', chart)
	edit_price(scope, 'charts', chart )
	edit_number(scope, 'charts', chart, 'length' )
	edit_number(scope, 'charts', chart, 'shift_up' )
	edit_number(scope, 'charts', chart, 'shift_down' )
	st.subheader('Moving Average Type - Rob to configure')		# TODO - Simple, Weighted, Exponential, Wilders
	st.markdown("""---""")

def render_dividends(scope):
	# st.markdown('##### Dividends')
	edit_active(scope, 'charts', 'dividends')
	st.markdown("""---""")

def render_announcements(scope):
	# st.markdown('##### Announcements')
	edit_active(scope, 'charts', 'announcements')
	st.markdown("""---""")





