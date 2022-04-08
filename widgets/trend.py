import streamlit as st

from pages.model.data_status import redo_page_data_screener_page_all_tickers


def edit_trend(scope, config_name, metric ):

	display_name = scope.config[config_name][metric]['name']
	
	previous_trend = scope.config[config_name][metric]['metrics']['trend']

	new_trend = st.selectbox ( 
									label=('Direction for ' + display_name), 
									options=scope.config['tests']['trends'],
									index=scope.config['tests']['trends'].index(previous_trend), 
									key=metric,
									) 

	scope.config[config_name][metric]['trend'] = new_trend

	if new_trend != previous_trend : 					# set to refresh pages if something has been changed
		if config_name == 'tests':
			redo_page_data_screener_page_all_tickers(scope, metric)
		else:
			print ( '\033[91m' + ' < edit_trend > function provided with unknown config_name > ' + config_name + '\033[0m')

