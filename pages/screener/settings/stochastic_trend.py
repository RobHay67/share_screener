
import streamlit as st

from pages.widgets.active import edit_active
from pages.widgets.number import edit_number
from pages.trials.trend_stochastic import edit_trend_stochastic


def render_stochastic_trend(scope, trial):
	
	config_group = 'trials'

	col1,col2,col3,col4,col5,col6 = st.columns([2,1,1,1,1,1])

	with col1:edit_active(scope, config_group, trial)
	with col2:edit_trend_stochastic(scope, config_group, trial)
	with col3:edit_number(scope, config_group, trial, 'lookback_days' )
	with col4:edit_number(scope, config_group, trial, 'slow' )
	with col5:edit_number(scope, config_group, trial, 'signal' )

