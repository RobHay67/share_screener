
import streamlit as st

from apps.config_trials.ohlcv_trend import render_ohlcv_trend
from apps.config_trials.sma_trend import render_sma_trend
from apps.config_trials.stochastic_trend import render_stochastic_trend
from apps.config_trials.rsi_trend import render_rsi_trend


def render_available_trials(scope):
	
	st.markdown("""---""")
	st.write('**Fundamental Analysis**')

	with st.expander(label='Annual General Meeting', expanded=False):
		st.write('This will be the criteria')

	with st.expander(label='Divdends - Dividend Yield', expanded=False):
		st.write('This will be the criteria')

	with st.expander(label='Price to Earnings Ratio - P/E', expanded=False):
		st.write('Dividend per share / Earning per share')



	st.write('**Technical Trading Indicators**')


	with st.expander(label='Trend Analysis on Open, High, Low, Close and Volume', expanded=False):
		col1,col2,col3,col4,col5 = st.columns([1,1,1,1,1])
		with col1: render_ohlcv_trend(scope, trial='trend_open')
		with col2: render_ohlcv_trend(scope, trial='trend_high')
		with col3: render_ohlcv_trend(scope, trial='trend_low')
		with col4: render_ohlcv_trend(scope, trial='trend_close')
		with col5: render_ohlcv_trend(scope, trial='trend_volume')

	with st.expander(label='Simple Moving Averages (SMA) on Open, High, Low, Close and Volume', expanded=False):
		col1,col2,col3,col4,col5,col6,col7,col8 = st.columns([1,1,1,1,1,1,1,1])
		with col1: render_sma_trend(scope, trial='sma_open')
		with col2: render_sma_trend(scope, trial='sma_high')
		with col3: render_sma_trend(scope, trial='sma_low')
		with col4: render_sma_trend(scope, trial='sma_close')
		with col5: render_sma_trend(scope, trial='sma_volume')

	with st.expander(label='Stochastic Oscillator - Momentum Indicator x 3 concurrrent options', expanded=True):
		col1,col2,col3,col4,col5,col6,col7,col8 = st.columns([1,1,1,1,1,1,1,1])
		with col1: render_stochastic_trend(scope, trial='stochastic_1')
		with col2: render_stochastic_trend(scope, trial='stochastic_2')
		with col3: render_stochastic_trend(scope, trial='stochastic_3')

	with st.expander(label='Relative Strength Index (RSI) - Momentum Indicator x 3 concurrrent options', expanded=True):
		st.write('This will be the criteria')
		col1,col2,col3,col4,col5,col6,col7,col8 = st.columns([1,1,1,1,1,1,1,1])
		with col1: render_rsi_trend(scope, trial='rsi_1')
		with col2: render_rsi_trend(scope, trial='rsi_2')





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




