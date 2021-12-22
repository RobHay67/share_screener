import streamlit as st

from config.model.set_page_metrics_status import set_refresh_metric_data


def edit_trend(scope, config_name, metric ):

	display_name = scope[config_name][metric]['name']
	
	previous_trend = scope[config_name][metric]['trend']

	new_trend = st.selectbox ( 
									label=('Direction for ' + display_name), 
									options=scope.screener_trends,
									index=scope.screener_trends.index(previous_trend), 
									key=metric,
									) 

	scope[config_name][metric]['trend'] = new_trend

	if new_trend != previous_trend : 					# set to refresh pages if something has been changed
		if config_name == 'screener_tests':
			set_refresh_metric_data(scope, metric)
		else:
			print ( '\033[91m' + ' < edit_trend > function provided with unknown config_name > ' + config_name + '\033[0m')

