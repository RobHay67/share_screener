
import streamlit as st

from pages.widgets.active import edit_active
from pages.widgets.number import edit_number
from pages.widgets.trend_stochastic import edit_trend_stochastic


def render_stochastic_trend(scope, trial):
	
	type_config = 'trials'

	col1,col2,col3,col4,col5,col6 = st.columns([2,1,1,1,1,1])

	with col1:edit_active(scope, type_config, trial)
	with col2:edit_trend_stochastic(scope, type_config, trial)
	with col3:edit_number(scope, type_config, trial, 'lookback_days' )
	with col4:edit_number(scope, type_config, trial, 'slow' )
	with col5:edit_number(scope, type_config, trial, 'signal' )

