import logging
import streamlit as st
from trials.scope.view.settings.expander_status import set_expander_status
from page.widgets.active import edit_active
from page.widgets.trends.sma import edit_trend_sma
from page.widgets.number import edit_number
from page.widgets.ohlcv import edit_ohlcv


def sma_trends(scope):
	logging.warning("sma_trends")
	settings_group = ['sma_1','sma_2','sma_3']
	open_status = set_expander_status(scope, settings_group)

	with st.expander(label='Simple Moving Averages (SMA) on either Open, High, Low, Close or Volume', expanded=open_status):
		for trial in settings_group:
			sma_settings(scope, trial=trial)


def sma_settings(scope, trial):
	logging.warning("sma_settings")
	schema_group = 'trials'
	column_name = scope[schema_group]['user_config'][trial]['function']['column']

	col1,col2,col3,col4,col5,col6 = st.columns([2,1,1,1,1,1])

	with col1:edit_active(scope, schema_group, trial)
	with col2:edit_ohlcv(scope, schema_group, trial)
	with col3:edit_trend_sma(scope, schema_group, trial)
	with col4:edit_number(scope, schema_group, trial, 'periods' )

	