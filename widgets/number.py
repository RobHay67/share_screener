from curses import keyname
import streamlit as st


from pages.model.data_status import set_page_data_status

	
def edit_number(scope, config_name, metric, measure ):
	
	widget_key 		= config_name + '_' + metric + '_' + measure
	display_name 	= measure.capitalize() + ' for ' + scope.config[config_name][metric]['name']
	
	previous_number = int(scope.config[config_name][metric]['metrics'][measure])	

	scope.config[config_name][metric]['metrics'][measure] = st.number_input(
																			label=display_name,
																			min_value=1, 
																			value=previous_number,
																			step=1,
																			key=widget_key,
																			)  

	if scope.config[config_name][metric]['metrics'][measure] != previous_number : 					# set to refresh pages if something has been changed
		if config_name == 'charts':
			# redo_page_data_singles_pages_all_tickers(scope, metric)
			set_page_data_status(scope, charts=metric)
		elif config_name == 'tests':
			set_page_data_status(scope, tests=metric)
		else:
			print ( '\033[91m' + ' < edit_number > function provided with unknown config_name > ' + config_name + '\033[0m')



	
