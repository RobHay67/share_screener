import streamlit as st

from pages.model.set_refresh_analysis import set_refresh_analysis_for_all_pages


def scope_analysis(scope):
	
	scope.analysis_row_limit 	= 100


	scope.volume_trend = 'up'
	scope.volume_lookback_days = 3

	scope.rsi_level = 0.50
	scope.rsi_column = 'close'

	scope.macd_direction = 'up'
	scope.macd_strength = 'strong'


	scope.sma_line = 'above'
	scope.ema_line = 'above'






def set_analysis_row_limit():

	analysis_row_limit = st.sidebar.number_input( 
							'No of Rows for Analysis', 
							min_value=100, 
							key='89',
							on_change=set_refresh_analysis_for_all_pages, 
							)
	return analysis_row_limit






