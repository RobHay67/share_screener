
import streamlit as st

from widgets.active import edit_active
from widgets.number import edit_number
from widgets.ohlcv import edit_ohlcv
from widgets.trend_rsi import edit_trend_rsi


def render_rsi_trend(scope, trial):
	
	type_config = 'trials'

	col1,col2,col3,col4,col5,col6 = st.columns([2,1,1,1,1,1])

	with col1:edit_active(scope, type_config, trial)
	with col2:edit_trend_rsi(scope, type_config, trial)
	with col3:edit_ohlcv(scope, type_config, trial)
	with col4:edit_number(scope, type_config, trial, 'lookback_days' )
