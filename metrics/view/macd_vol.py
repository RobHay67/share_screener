
import streamlit as st


from widgets.active import edit_active
from widgets.number import edit_number


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