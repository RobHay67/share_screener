
import streamlit as st

# from pages.model.data_status import redo_page_data_singles_pages_all_tickers
from pages.model.data_status import set_page_data_status
from pages.config import scope_page_templates





def edit_active(scope, config_name, metric ):
	print('config_name = ', config_name)
	print('metric      = ', metric)

	print('This is the scope object')
	print(scope.config[config_name][metric])

	
	display_name =  '' + scope.config[config_name][metric]['name']
	
	previous_active_status = scope.config[config_name][metric]['active']

	new_active_status = st.checkbox( 
								display_name, 
								value=previous_active_status,
								key=metric
								)

	scope.config[config_name][metric]['active'] = new_active_status

	if new_active_status != previous_active_status : 				# set to refresh metrics if something has been changed
		scope_page_templates(scope)									# rebase the active and inactive page metrics
		if config_name == 'charts':
			redo_page_data_singles_pages_all_tickers(scope, metric)
		elif config_name == 'tests':
			set_page_data_status(scope, tests=metric)
		else:
			print ( '\033[91m' + ' < edit_active > function provided with unknown config_name > ' + config_name + '\033[0m')

