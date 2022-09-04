
import streamlit as st

from widgets.active import edit_active
from widgets.trend import edit_trend_direction
from widgets.number import edit_number


def render_ohlcv_trend(scope, trial):
	
	type_config = 'trials'
	column_name = scope[type_config][trial]['add_columns']['column']

	edit_active(scope, type_config, trial)
	# st.write('column_name = ', column_name)
	edit_trend_direction (scope, type_config, trial)
	edit_number(scope, type_config, trial, 'duration' )
	edit_number(scope, type_config, trial, 'timespan' )

	