
import logging
import streamlit as st

from users.views.save_user_settings_button import save_user_settings_button
from trials.scope.view.settings.ohlcv import ohlcv_price_direction
from trials.scope.view.settings.sma import sma_trends
from trials.scope.view.settings.stochastic import stochastic_trend
from trials.scope.view.settings.rsi import rsi_trends
from trials.scope.view.settings.example import example_settings


def show_settings_trials(scope):
	logging.debug("show_settings_trials")
	st.divider()
	col1,col2=st.columns([8,4])
	with col1:st.subheader('Trial/Test Settings for User ')
	with col2:save_user_settings_button(scope)
	
	ohlcv_price_direction(scope)
	sma_trends(scope)
	rsi_trends(scope)
	stochastic_trend(scope)

	with st.expander(label='Moving Average - Convergence / Divergence (MACD)', expanded=False):
		st.write('This will be the criteria')

	with st.expander(label='MACD - Volume', expanded=False):
		st.write('This will be the criteria')
	

	st.write('**Fundamental Analysis**')
	with st.expander(label='Annual General Meeting', expanded=False):
		st.write('This will be the criteria')
	with st.expander(label='Divdends - Dividend Yield', expanded=False):
		st.write('This will be the criteria')
	with st.expander(label='Price to Earnings Ratio - P/E', expanded=False):
		st.write('Dividend per share / Earning per share')



	st.divider()

	with st.expander(label='Current Asset Ratio', expanded=False):
		st.write('This will be the criteria')

	with st.expander(label='Debt to Equity Ratio', expanded=False):
		st.write('This will be the criteria')

	with st.expander(label='Cash Flow - Operating', expanded=False):
		st.write('This will be the criteria')

	with st.expander(label='Cash Flow - Capital', expanded=False):
		st.write('This will be the criteria')
	
	with st.expander(label='Cash Flow - Financial', expanded=False):
		st.write('This will be the criteria')



	example_settings(scope)









