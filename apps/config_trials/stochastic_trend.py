
import streamlit as st

from widgets.active import edit_active
from widgets.number import edit_number
from widgets.trend_stochastic import edit_trend_stochastic


def render_stochastic_trend(scope, trial):
	
	type_config = 'trials'

	edit_active(scope, type_config, trial)
	edit_trend_stochastic(scope, type_config, trial)
	edit_number(scope, type_config, trial, 'lookback_days' )
	edit_number(scope, type_config, trial, 'slow' )
	edit_number(scope, type_config, trial, 'signal' )

