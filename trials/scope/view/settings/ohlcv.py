import logging
import streamlit as st
from trials.scope.view.settings.expander_status import set_expander_status
from page.widgets.active import edit_active
from page.widgets.trends.ohlcv import edit_trend_ohlcv
from page.widgets.number import edit_number
from page.widgets.ohlcv import edit_ohlcv


def ohlcv_price_direction(scope):
	logging.debug("ohlcv_price_direction")
	settings_group = ['price_1','price_2','price_3']
	open_status = set_expander_status(scope, settings_group)
	with st.expander(label='Price Direction (Trend) of either Open, High, Low, Close or Volume', expanded=open_status):
		for trial in settings_group:
			ohlcv_settings(scope, trial=trial)


def ohlcv_settings(scope, trial):
	logging.debug("ohlcv_settings")
	schema_group = 'trials'
	column_name = scope[schema_group]['user_config'][trial]['function']['column']

	col1,col2,col3,col4,col5,col6 = st.columns([2,1,1,1,1.5,1])

	with col1:edit_active(scope, schema_group, trial)
	with col2:edit_ohlcv(scope, schema_group, trial)
	with col3:edit_trend_ohlcv (scope, schema_group, trial)
	with col4:edit_number(scope, schema_group, trial, 'duration' )
	with col5:edit_number(scope, schema_group, trial, 'timespan' )
