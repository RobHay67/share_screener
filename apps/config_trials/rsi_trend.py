
import streamlit as st

from widgets.active import edit_active
from widgets.number import edit_number
from widgets.ohlcv import edit_ohlcv
from widgets.trend_rsi import edit_trend_rsi


def render_rsi_trend(scope, trial):
	
	type_config = 'trials'

	edit_active(scope, type_config, trial)
	edit_trend_rsi(scope, type_config, trial)
	edit_ohlcv(scope, type_config, trial)
	edit_number(scope, type_config, trial, 'lookback_days' )
