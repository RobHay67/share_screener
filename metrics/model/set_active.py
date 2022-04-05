
import streamlit as st

from pages.model.set_page_metrics_status import set_refresh_chart_data
from pages.model.set_page_metrics_status import set_refresh_metric_data
from pages.config import scope_page_templates





def edit_active(scope, config_name, metric ):

	display_name =  '' + scope[config_name][metric]['name']
	
	previous_active_status = scope[config_name][metric]['active']

	new_active_status = st.checkbox( 
								display_name, 
								value=previous_active_status,
								key=metric
								)

	scope[config_name][metric]['active'] = new_active_status

	if new_active_status != previous_active_status : 				# set to refresh metrics if something has been changed
		scope_page_templates(scope)									# rebase the active and inactive page metrics
		if config_name == 'charts':
			set_refresh_chart_data(scope, metric)
		elif config_name == 'screener_tests':
			set_refresh_metric_data(scope, metric)
		else:
			print ( '\033[91m' + ' < edit_active > function provided with unknown config_name > ' + config_name + '\033[0m')

