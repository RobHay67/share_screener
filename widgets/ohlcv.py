import streamlit as st


from pages.model.data_status import redo_page_data_singles_pages_all_tickers
from pages.model.data_status import redo_page_data_screener_page_all_tickers


def edit_ohlcv(scope, config_name, metric ):
	
	display_name = scope.config[config_name][metric]['name']
	
	if config_name == 'charts':
		previous_ohlcv_col = scope.config[config_name][metric]['metrics']['column']
	else:
		previous_ohlcv_col = scope.config[config_name][metric]['column']
	
	
	new_ohlcv_col = st.selectbox ( 
									label=('Column for ' + display_name), 
									options=scope.config['dropdowns']['ohlcv_columns'],
									index=scope.config['dropdowns']['ohlcv_columns'].index(previous_ohlcv_col), 
									key=metric,
									) 

	if new_ohlcv_col != previous_ohlcv_col : 					# set to refresh pages if something has been changed
		if config_name == 'charts':
			scope.config[config_name][metric]['metrics']['column'] = new_ohlcv_col
			redo_page_data_singles_pages_all_tickers(scope, metric)
		elif config_name == 'tests':
			scope.config[config_name][metric]['column'] = new_ohlcv_col
			redo_page_data_screener_page_all_tickers(scope, metric)
		else:
			print ( '\033[91m' + ' < edit_ohlcv > function provided with unknown config_name > ' + config_name + '\033[0m')



def edit_ohlc(scope, config_name, metric ):
	
	display_name = scope.config[config_name][metric]['name']
	
	if config_name == 'charts':
		previous_ohlcv_col = scope.config[config_name][metric]['metrics']['column']
	else:
		previous_ohlcv_col = scope.config[config_name][metric]['column']

	new_ohlc_col = st.selectbox ( 
									label=('Column for ' + display_name), 
									options=scope.config['dropdowns']['price_columns '],
									index=scope.config['dropdowns']['price_columns '].index(previous_ohlcv_col), 
									key=metric,
									) 

	if new_ohlc_col != previous_ohlcv_col : 					# set to refresh pages if something has been changed
		if config_name == 'charts':
			scope.config[config_name][metric]['metrics']['column'] = new_ohlc_col
			redo_page_data_singles_pages_all_tickers(scope, metric)
		elif config_name == 'tests':
			scope.config[config_name][metric]['column'] = new_ohlc_col
			redo_page_data_screener_page_all_tickers(scope, metric)
		else:
			print ( '\033[91m' + ' < edit_ohlc > function provided with unknown config_name > ' + config_name + '\033[0m')
