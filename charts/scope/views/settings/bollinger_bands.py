import streamlit as st


from app.views.widgets.active import edit_active
from app.views.widgets.number import edit_number
from app.views.widgets.ohlc import edit_ohlc




def bollinger_band_settings(scope):
	schema_key = 'bollinger_bands'
	schema_group = 'charts'

	col1,col2,col3,col4,col5,col6 = st.columns([2,1,1,1,1,1])

	with col1:edit_active(scope, schema_group, schema_key)
	with col1:st.write('Moving Average Type - Rob to configure')		# TODO - Simple, Weighted, Exponential, Wilders
	with col2:edit_ohlc(scope, schema_group, schema_key )
	with col3:edit_number(scope, schema_group, schema_key, 'length' )
	with col4:edit_number(scope, schema_group, schema_key, 'shift_up' )
	with col5:edit_number(scope, schema_group, schema_key, 'shift_down' )
	
