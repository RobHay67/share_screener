import logging
import streamlit as st
from users.views.button_save_user_settings import button_save_user_settings

from charts.scope.settings.chart_height import set_chart_height_primary
from page.widgets.active import edit_active

from charts.scope.settings.macd import macd_settings
from charts.scope.settings.macd_vol import macd_volume_settings
from charts.scope.settings.rsi import rsi_settings
from charts.scope.settings.stochastic import stochastic_settings
from charts.scope.settings.volume_oscillator import volume_oscillator_settings
from charts.scope.settings.line import line_settings


def show_settings_charts(scope):
	logging.warning("show_settings_charts")
	# ----------------------------------------------------------------------
	# Primary Charts
	# ----------------------------------------------------------------------
	col1,col2,col3,col4 = st.columns([4,2,4,2]) #12
	with col1:
		st.subheader('Chart Settings')
	with col2:
		st.write('')
		st.caption('Tick to display chart')
	with col3:
		set_chart_height_primary(scope)
	with col4:
		button_save_user_settings(scope)

	col1,col2,col3 = st.columns(3)
	with col1:
		st.caption('Price Display Charts')
		activate_chart(scope, 'candlestick')
		# activate_chart(scope, 'line')
		# line_settings(scope)
		st.caption('Line Chart - see below')
		activate_chart(scope, 'bar')
	with col2: 
		st.caption('?? Charts')
		activate_chart(scope, 'scatter')
		activate_chart(scope, 'heiken_ashi')
		activate_chart(scope, 'VWAP')
	with col3:
		st.caption('?? Charts')
		activate_chart(scope, 'volume')
		activate_chart(scope, 'vac')
		activate_chart(scope, 'vol_per_minute')

	st.divider()

	st.caption('Charts with additional configuration')
	line_settings(scope)
	macd_settings(scope)
	macd_volume_settings(scope)
	rsi_settings(scope)
	stochastic_settings(scope)
	volume_oscillator_settings(scope)

	st.divider()


def activate_chart(scope, schema_key):
	logging.warning("activate_chart")
	edit_active(scope, 'charts', schema_key)








