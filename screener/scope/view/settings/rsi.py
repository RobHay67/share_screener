import streamlit as st
from screener.scope.view.settings.expander_status import set_expander_status
from app.views.widgets.active import edit_active
from app.views.widgets.number import edit_number
from app.views.widgets.ohlcv import edit_ohlcv
from app.views.widgets.trends.rsi import edit_trend_rsi


def rsi_trends(scope):
	settings_group = ['rsi_1','rsi_2']
	open_status = set_expander_status(scope, settings_group)
	
	with st.expander(label='Relative Strength Index (RSI) - Momentum Indicator x 3 concurrrent options', expanded=open_status):
		# col1,col2,col3,col4,col5,col6,col7,col8 = st.columns([1,1,1,1,1,1,1,1])
		rsi_settings(scope, trial='rsi_1')
		rsi_settings(scope, trial='rsi_2')


def rsi_settings(scope, trial):
	
	config_group = 'trials'

	col1,col2,col3,col4,col5,col6 = st.columns([2,1,1,1,1,1])

	with col1:edit_active(scope, config_group, trial)
	with col2:edit_ohlcv(scope, config_group, trial)
	with col3:edit_trend_rsi(scope, config_group, trial)
	with col4:edit_number(scope, config_group, trial, 'lookback_days' )
