import streamlit as st

from pages.data.status import set_page_data_status


def edit_trend(scope, config_name, metric ):

	display_name = scope.config[config_name][metric]['name']
	
	previous_trend = scope.config[config_name][metric]['add_columns']['trend']

	new_trend = st.selectbox ( 
									label=('Direction for ' + display_name), 
									options=scope.config['tests']['trends'],
									index=scope.config['tests']['trends'].index(previous_trend), 
									key=metric,
									) 

	scope.config[config_name][metric]['trend'] = new_trend

	if new_trend != previous_trend : 					# set to refresh pages if something has been changed
		if config_name == 'tests':
			set_page_data_status(scope, tests=metric, caller='edit_trend')
		else:
			print ( '\033[91m' + ' < edit_trend > function provided with unknown config_name > ' + config_name + '\033[0m')

