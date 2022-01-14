import streamlit as st


from pages.model.set_page_metrics_status import set_refresh_chart_data
from pages.model.set_page_metrics_status import set_refresh_metric_data


def edit_ohlcv(scope, config_name, metric ):
	
	display_name = scope[config_name][metric]['name']
	
	if config_name == 'charts':
		previous_ohlcv_col = scope[config_name][metric]['metrics']['column']
	else:
		previous_ohlcv_col = scope[config_name][metric]['column']
	
	
	new_ohlcv_col = st.selectbox ( 
									label=('Column for ' + display_name), 
									options=scope.dropdown_ohlcv_columns,
									index=scope.dropdown_ohlcv_columns.index(previous_ohlcv_col), 
									key=metric,
									) 

	if new_ohlcv_col != previous_ohlcv_col : 					# set to refresh pages if something has been changed
		if config_name == 'charts':
			scope[config_name][metric]['metrics']['column'] = new_ohlcv_col
			set_refresh_chart_data(scope, metric)
		elif config_name == 'screener_tests':
			scope[config_name][metric]['column'] = new_ohlcv_col
			set_refresh_metric_data(scope, metric)
		else:
			print ( '\033[91m' + ' < edit_ohlcv > function provided with unknown config_name > ' + config_name + '\033[0m')



def edit_ohlc(scope, config_name, metric ):
	
	display_name = scope[config_name][metric]['name']
	
	if config_name == 'charts':
		previous_ohlcv_col = scope[config_name][metric]['metrics']['column']
	else:
		previous_ohlcv_col = scope[config_name][metric]['column']

	new_ohlc_col = st.selectbox ( 
									label=('Column for ' + display_name), 
									options=scope.dropdown_price_columns,
									index=scope.dropdown_price_columns.index(previous_ohlcv_col), 
									key=metric,
									) 

	if new_ohlc_col != previous_ohlcv_col : 					# set to refresh pages if something has been changed
		if config_name == 'charts':
			scope[config_name][metric]['metrics']['column'] = new_ohlc_col
			set_refresh_chart_data(scope, metric)
		elif config_name == 'screener_tests':
			scope[config_name][metric]['column'] = new_ohlc_col
			set_refresh_metric_data(scope, metric)
		else:
			print ( '\033[91m' + ' < edit_ohlc > function provided with unknown config_name > ' + config_name + '\033[0m')
