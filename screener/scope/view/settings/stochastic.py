import streamlit as st
from screener.scope.view.settings.expander_status import set_expander_status
from app.views.widgets.active import edit_active
from app.views.widgets.number import edit_number
from app.views.widgets.trends.stochastic import edit_trend_stochastic


def stochastic_trend(scope):
	settings_group = ['stochastic_1','stochastic_2','stochastic_3']
	open_status = set_expander_status(scope, settings_group)
	with st.expander(label='Stochastic Oscillator - Momentum Indicator x 3 concurrrent options', expanded=open_status):
		for trial in settings_group:
			stochastic_settings(scope, trial=trial)
		# stochastic_settings(scope, trial='stochastic_2')
		# stochastic_settings(scope, trial='stochastic_3')


def stochastic_settings(scope, trial):
	
	schema_group = 'trials'

	col1,col2,col3,col4,col5,col6 = st.columns([2,1,1,1,1,1])

	with col1:edit_active(scope, schema_group, trial)
	with col2:edit_trend_stochastic(scope, schema_group, trial)
	with col3:edit_number(scope, schema_group, trial, 'lookback_days' )
	with col4:edit_number(scope, schema_group, trial, 'slow' )
	with col5:edit_number(scope, schema_group, trial, 'signal' )

