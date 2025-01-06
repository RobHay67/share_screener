import streamlit as st
from screener.views.settings.expander_status import set_expander_status
from app.views.widgets.active import edit_active
from app.views.widgets.trends.sma import edit_trend_sma
from app.views.widgets.number import edit_number
from app.views.widgets.ohlcv import edit_ohlcv


def sma_trends(scope):
	settings_group = ['sma_1','sma_2','sma_3']
	open_status = set_expander_status(scope, settings_group)

	with st.expander(label='Simple Moving Averages (SMA) on either Open, High, Low, Close or Volume', expanded=open_status):
		for trial in settings_group:
			sma_settings(scope, trial=trial)


def sma_settings(scope, trial):
	
	config_group = 'trials'
	column_name = scope[config_group]['user_config'][trial]['add_columns']['column']

	col1,col2,col3,col4,col5,col6 = st.columns([2,1,1,1,1,1])

	with col1:edit_active(scope, config_group, trial)
	with col2:edit_ohlcv(scope, config_group, trial)
	with col3:edit_trend_sma(scope, config_group, trial)
	with col4:edit_number(scope, config_group, trial, 'periods' )

	