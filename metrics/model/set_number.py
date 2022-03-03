from curses import keyname
import streamlit as st


from pages.model.set_page_metrics_status import set_refresh_chart_data
from pages.model.set_page_metrics_status import set_refresh_metric_data


	
def edit_number(scope, config_name, metric, measure ):
	
	widget_key 		= config_name + '_' + metric + '_' + measure
	display_name 	= measure.capitalize() + ' for ' + scope[config_name][metric]['name']
	
	previous_number = int(scope[config_name][metric]['metrics'][measure])	

	scope[config_name][metric]['metrics'][measure] = st.number_input(
										label=display_name,
										min_value=1, 
										value=previous_number,
										step=1,
										key=widget_key,
										)  

	if scope[config_name][metric]['metrics'][measure] != previous_number : 					# set to refresh pages if something has been changed
		if config_name == 'charts':
			set_refresh_chart_data(scope, metric)
		elif config_name == 'screener_tests':
			set_refresh_metric_data(scope, metric)
		else:
			print ( '\033[91m' + ' < edit_number > function provided with unknown config_name > ' + config_name + '\033[0m')



	





	# if metric == 'trend_high':
	# 	print('EDIt_NUmber Function')
	# 	print('widget_key  = ', widget_key)
	# 	print('config_name = ', config_name)
	# 	print('metric      = ', metric)
	# 	print('measure     = ', measure.upper())
	# 	print('before      = ', scope[config_name][metric]['metrics'][measure])
