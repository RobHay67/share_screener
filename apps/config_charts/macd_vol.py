
import streamlit as st


from widgets.active import edit_active
from widgets.number import edit_number


def render_macd_vol(scope):
	
	st.markdown('##### Moving Average, Convergence, Divergence (MACD) - Volume Only')
	column_adder = 'macd_vol'
	type_config = 'charts'

	edit_active(scope, type_config, column_adder)
	st.write('Column for MACD')
	st.write('Volume')
	edit_number(scope, type_config, column_adder, 'long' )
	edit_number(scope, type_config, column_adder, 'short' )
	edit_number(scope, type_config, column_adder, 'signal' )
	st.markdown("""---""")