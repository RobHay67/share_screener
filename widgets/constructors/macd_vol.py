
import streamlit as st


from widgets.active import edit_active
from widgets.number import edit_number


def render_macd_vol(scope):
	st.markdown('##### Moving Average, Convergence, Divergence (MACD) - Volume Only')
	expander = 'macd_vol'
	config_name = 'charts'

	edit_active(scope, config_name, expander)
	st.write('Column for MACD')
	st.write('Volume')
	edit_number(scope, config_name, expander, 'long' )
	edit_number(scope, config_name, expander, 'short' )
	edit_number(scope, config_name, expander, 'signal' )
	st.markdown("""---""")