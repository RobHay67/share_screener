
import streamlit as st


from widgets.active import edit_active
from widgets.number import edit_number


def render_macd_vol(scope):
	
	column_adder = 'macd_vol'
	type_config = 'charts'

	st.markdown('##### Moving Average, Convergence, Divergence (MACD) - Volume Only')

	col1,col2,col3,col4,col5,col6 = st.columns([1,1,1,1,1,1])

	with col1:edit_active(scope, type_config, column_adder)
	with col2:
		st.write('Column for MACD')
		st.write('Volume')
	with col3:edit_number(scope, type_config, column_adder, 'long' )
	with col4:edit_number(scope, type_config, column_adder, 'short' )
	with col5:edit_number(scope, type_config, column_adder, 'signal' )
	
	st.markdown("""---""")