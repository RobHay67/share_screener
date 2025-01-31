import logging
import streamlit as st

from charts.scope.views.settings.announcements import announcement_settings
from charts.scope.views.settings.bollinger_bands import bollinger_band_settings
from charts.scope.views.settings.dividends import dividend_settings
from charts.scope.views.settings.moving_average import moving_average_settings



def show_settings_overlay(scope):
	logging.debug("show_settings_overlay")
	# ----------------------------------------------------------------------
	# Overlays
	# ----------------------------------------------------------------------	
	st.subheader('Overlays')
	st.caption('added to every relevant chart')
	
	col1,col2,col3,col4,col5,col6 = st.columns([1,1,1,1,1,1])
		
	dividend_settings(scope)
	announcement_settings(scope)

	moving_average_settings(scope, 'sma_a')
	moving_average_settings(scope, 'sma_b')
	moving_average_settings(scope, 'sma_c')
	
	moving_average_settings(scope, 'ema_a')
	moving_average_settings(scope, 'ema_b')
	moving_average_settings(scope, 'ema_c')

	bollinger_band_settings(scope)

	st.divider()



