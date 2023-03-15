
import streamlit as st

from widgets.active import edit_active
from widgets.trend_ohlcv import edit_trend_ohlcv
from widgets.number import edit_number


def render_ohlcv_trend(scope, trial):
	
	type_config = 'trials'
	column_name = scope[type_config][trial]['add_columns']['column']

	col1,col2,col3,col4,col5,col6 = st.columns([2,1,1,1,1,1])


	with col1:edit_active(scope, type_config, trial)
	# st.write('column_name = ', column_name)
	with col2:edit_trend_ohlcv (scope, type_config, trial)
	with col3:edit_number(scope, type_config, trial, 'duration' )
	with col4:edit_number(scope, type_config, trial, 'timespan' )

	