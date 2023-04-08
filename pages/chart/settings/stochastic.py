import streamlit as st


from pages.widgets.active import edit_active
from pages.widgets.number import edit_number


def render_stochastic(scope):
	
	column_adder = 'stochastic'
	type_config = 'charts'

	col1,col2,col3,col4,col5,col6 = st.columns([2,1,1,1,1,1])

	with col1:edit_active(scope, type_config, column_adder)
	with col2:edit_number(scope, type_config, column_adder, 'lookback_days' )
	with col3:edit_number(scope, type_config, column_adder, 'slow' )
	with col4:edit_number(scope, type_config, column_adder, 'signal' )


