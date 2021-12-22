import streamlit as st


from config.model.set_page_metrics_status import set_refresh_chart_data
from config.model.set_page_metrics_status import set_refresh_metric_data

	
def edit_number(scope, config_name, metric, column ):
	
	display_name = scope[config_name][metric]['name']
	column_name = column.capitalize()
	
	if config_name == 'charts':
		previous_number = int(scope[config_name][metric]['metrics'][column])
	else:
		previous_number = int(scope[config_name][metric][column])


	new_number = st.number_input(
										# column_name,
										label=(column_name + ' for ' + display_name), 
										min_value=0, 
										value=previous_number,
										key=display_name
										)  

	

	if new_number != previous_number : 					# set to refresh pages if something has been changed
		if config_name == 'charts':
			scope[config_name][metric]['metrics'][column] = new_number
			set_refresh_chart_data(scope, metric)
		elif config_name == 'screener_tests':
			scope[config_name][metric][column] = new_number
			set_refresh_metric_data(scope, metric)
		else:
			print ( '\033[91m' + ' < edit_number > function provided with unknown config_name > ' + config_name + '\033[0m')


	





