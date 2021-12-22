import streamlit as st


from config.model.set_active import edit_active
from config.model.set_number import edit_number
from config.model.set_ohlcv import edit_ohlcv
from config.model.set_ohlcv import edit_ohlc
from config.model.set_colour import edit_colour

# -------------------------------------------------------------------------------------------------------------------------------------
# Primary and Secondary Charts
# -------------------------------------------------------------------------------------------------------------------------------------

def render_activate_chart(scope, metric):
	edit_active(scope, 'charts', metric)


# -------------------------------------------------------------------------------------------------------------------------------------
# Primary metric Components
# -------------------------------------------------------------------------------------------------------------------------------------
def render_primary_chart(scope, metric):
	st.write('.')
	render_activate_chart(scope, metric)
	


# -------------------------------------------------------------------------------------------------------------------------------------
# Secondary Charts
# -------------------------------------------------------------------------------------------------------------------------------------

def render_macd(scope):
	st.markdown('##### Moving Average, Convergence, Divergence (MACD)')
	metric = 'macd'
	config_name = 'charts'

	edit_active(scope, config_name, metric)
	edit_ohlc  (scope, config_name, metric)
	edit_number(scope, config_name, metric, 'long' )
	edit_number(scope, config_name, metric, 'short' )
	edit_number(scope, config_name, metric, 'signal' )
	st.markdown("""---""")

def render_macd_vol(scope):
	st.markdown('##### Moving Average, Convergence, Divergence (MACD) - Volume Only')
	metric = 'macd_vol'
	config_name = 'charts'

	edit_active(scope, config_name, metric)
	st.write('Column for MACD')
	st.write('Volume')
	edit_number(scope, config_name, metric, 'long' )
	edit_number(scope, config_name, metric, 'short' )
	edit_number(scope, config_name, metric, 'signal' )
	st.markdown("""---""")

def render_rsi(scope):
	st.markdown('##### Relative Strength Index (RSI)')
	metric = 'rsi'
	config_name = 'charts'

	edit_active(scope, config_name, metric)
	edit_ohlcv(scope, config_name, metric )
	edit_number(scope, config_name, metric, 'lookback_days' )
	st.markdown("""---""")

def render_stochastic(scope):
	st.markdown('##### Stochastic Oscillator')
	metric = 'stochastic'
	config_name = 'charts'

	edit_active(scope, config_name, metric)
	edit_number(scope, config_name, metric, 'lookback_days' )
	edit_number(scope, config_name, metric, 'slow' )
	edit_number(scope, config_name, metric, 'signal' )
	st.markdown("""---""")

def render_volume_oscillator(scope):
	st.markdown('##### Volume Oscillator')
	metric = 'vol_osssy'
	config_name = 'charts'

	edit_active(scope, config_name, metric)
	edit_number(scope, config_name, metric, 'fast' )
	edit_number(scope, config_name, metric, 'slow' )
	st.markdown("""---""")

# -------------------------------------------------------------------------------------------------------------------------------------
# Overlays
# -------------------------------------------------------------------------------------------------------------------------------------
def render_moving_average(scope, metric):  # SMA or EMA

	config_name = 'charts'

	edit_active(scope, config_name, metric)
	edit_number(scope, config_name, metric, 'periods' )
	edit_ohlc(scope, config_name, metric )
	edit_colour(scope, config_name, metric )
	st.markdown("""---""")

def render_bollinger_bands(scope):
	# st.markdown('##### Bollinger Bands')
	metric = 'bollinger_bands'
	config_name = 'charts'

	edit_active(scope, config_name, metric)
	edit_ohlc(scope, config_name, metric )
	edit_number(scope, config_name, metric, 'length' )
	edit_number(scope, config_name, metric, 'shift_up' )
	edit_number(scope, config_name, metric, 'shift_down' )
	st.subheader('Moving Average Type - Rob to configure')		# TODO - Simple, Weighted, Exponential, Wilders
	st.markdown("""---""")

def render_dividends(scope):
	# st.markdown('##### Dividends')
	metric = 'dividends'
	config_name = 'charts'

	edit_active(scope, config_name, metric)
	st.markdown("""---""")

def render_announcements(scope):
	# st.markdown('##### Announcements')
	metric = 'announcements'
	config_name = 'charts'

	edit_active(scope, config_name, metric)
	st.markdown("""---""")





