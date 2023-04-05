
import streamlit as st

from apps.screener.config.ohlcv_trend import render_ohlcv_trend
from apps.screener.config.sma_trend import render_sma_trend
from apps.screener.config.stochastic_trend import render_stochastic_trend
from apps.screener.config.rsi_trend import render_rsi_trend
from apps.screener.config.example import example_settings
from widgets.save_user_settings import save_user_settings_button


def render_available_trials(scope):

	st.markdown("""---""")
	col1,col2=st.columns([8,4])
	with col1:st.subheader('Trial / Test Configuration Settings')
	with col2:save_user_settings_button(scope)
	
	ohlcv_price_direction(scope)
	sma_trends(scope)
	rsi_trends(scope)
	stochastic_trend(scope)
	

	st.write('**Fundamental Analysis**')
	with st.expander(label='Annual General Meeting', expanded=False):
		st.write('This will be the criteria')
	with st.expander(label='Divdends - Dividend Yield', expanded=False):
		st.write('This will be the criteria')
	with st.expander(label='Price to Earnings Ratio - P/E', expanded=False):
		st.write('Dividend per share / Earning per share')
	st.write('**Technical Trading Indicators**')

	with st.expander(label='Moving Average - Convergence / Divergence (MACD)', expanded=False):
		st.write('This will be the criteria')

	with st.expander(label='MACD - Volume', expanded=False):
		st.write('This will be the criteria')

	st.markdown("""---""")

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


def ohlcv_price_direction(scope):
	trial_group = ['price_1','price_2','price_3']
	open_status = set_open_status(scope, trial_group)
	with st.expander(label='Price Direction (Trend) of either Open, High, Low, Close or Volume', expanded=open_status):
		for trial in trial_group:
			render_ohlcv_trend(scope, trial=trial)


def stochastic_trend(scope):
	trial_group = ['stochastic_1','stochastic_2','stochastic_3']
	open_status = set_open_status(scope, trial_group)
	with st.expander(label='Stochastic Oscillator - Momentum Indicator x 3 concurrrent options', expanded=open_status):
		for trial in trial_group:
			render_stochastic_trend(scope, trial=trial)
		# render_stochastic_trend(scope, trial='stochastic_2')
		# render_stochastic_trend(scope, trial='stochastic_3')


def rsi_trends(scope):
	trial_group = ['rsi_1','rsi_2']
	open_status = set_open_status(scope, trial_group)
	
	with st.expander(label='Relative Strength Index (RSI) - Momentum Indicator x 3 concurrrent options', expanded=open_status):
		# col1,col2,col3,col4,col5,col6,col7,col8 = st.columns([1,1,1,1,1,1,1,1])
		render_rsi_trend(scope, trial='rsi_1')
		render_rsi_trend(scope, trial='rsi_2')


def sma_trends(scope):
	trial_group = ['sma_1','sma_2','sma_3']
	open_status = set_open_status(scope, trial_group)

	with st.expander(label='Simple Moving Averages (SMA) on either Open, High, Low, Close or Volume', expanded=open_status):
		for trial in trial_group:
			render_sma_trend(scope, trial=trial)


def set_open_status(scope, trial_group):
	open_expanded = False
	for trial in trial_group:
		if scope.trials[trial]['active']:
			open_expanded=True
			break
	return open_expanded


