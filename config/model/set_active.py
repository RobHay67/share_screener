
import streamlit as st

from config.model.set_page_df_status import set_refresh_chart_dfs_for_non_screener_pages
from config.model.set_page_df_status import set_refresh_screener_dfs_for_screener_page

def edit_active(scope, schema, key ):

	display_name =  '' + scope[schema][key]['name']
	
	previous_active_status = scope[schema][key]['active']

	new_active_status = st.checkbox( 
								display_name, 
								value=previous_active_status,
								key=key
								)

	scope[schema][key]['active'] = new_active_status

	if new_active_status != previous_active_status : 				# set to refresh pages if something has been changed
		if schema == 'charts':
			set_refresh_chart_dfs_for_non_screener_pages(scope)
		elif schema == 'screener_tests':
			set_refresh_screener_dfs_for_screener_page(scope)
		else:
			print ( '\033[91m' + ' < edit_active > function provided with unknown schema > ' + schema + '\033[0m')

