
import streamlit as st

from pages.widgets.active import edit_active
from pages.widgets.number import edit_number
from pages.widgets.ohlcv import edit_ohlcv
from pages.trials.trend_rsi import edit_trend_rsi


def render_rsi_trend(scope, trial):
	
	config_group = 'trials'

	col1,col2,col3,col4,col5,col6 = st.columns([2,1,1,1,1,1])

	with col1:edit_active(scope, config_group, trial)

	with col2:edit_ohlcv(scope, config_group, trial)
	
	with col3:edit_trend_rsi(scope, config_group, trial)
	
	with col4:edit_number(scope, config_group, trial, 'lookback_days' )
