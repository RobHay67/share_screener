import streamlit as st
from screener.views.settings.expander_status import set_expander_status
from app.views.widgets.active import edit_active
from app.views.widgets.trends.ohlcv import edit_trend_ohlcv
from app.views.widgets.number import edit_number
from app.views.widgets.ohlcv import edit_ohlcv


def ohlcv_price_direction(scope):
	settings_group = ['price_1','price_2','price_3']
	open_status = set_expander_status(scope, settings_group)
	with st.expander(label='Price Direction (Trend) of either Open, High, Low, Close or Volume', expanded=open_status):
		for trial in settings_group:
			ohlcv_settings(scope, trial=trial)


def ohlcv_settings(scope, trial):
	
	config_group = 'trials'
	column_name = scope[config_group]['user_config'][trial]['add_columns']['column']

	col1,col2,col3,col4,col5,col6 = st.columns([2,1,1,1,1.5,1])

	with col1:edit_active(scope, config_group, trial)
	with col2:edit_ohlcv(scope, config_group, trial)
	with col3:edit_trend_ohlcv (scope, config_group, trial)
	with col4:edit_number(scope, config_group, trial, 'duration' )
	with col5:edit_number(scope, config_group, trial, 'timespan' )
