import streamlit as st


from config.model.set_page_df_status import set_refresh_chart_dfs_for_non_screener_pages
from config.model.set_page_df_status import set_refresh_screener_dfs_for_screener_page

	
def edit_number(scope, schema, key, column ):
	
	display_name = scope[schema][key]['name']
	column_name = column.capitalize()
	
	if schema == 'charts':
		previous_number = int(scope[schema][key]['metrics'][column])
	else:
		previous_number = int(scope[schema][key][column])


	new_number = st.number_input(
										# column_name,
										label=(column_name + ' for ' + display_name), 
										min_value=0, 
										value=previous_number,
										key=display_name
										)  

	if new_number != previous_number : 					# set to refresh pages if something has been changed
		if schema == 'charts':
			scope[schema][key]['metrics'][column] = new_number
			set_refresh_chart_dfs_for_non_screener_pages(scope)
		elif schema == 'screener_tests':
			scope[schema][key][column] = new_number
			set_refresh_screener_dfs_for_screener_page(scope)
		else:
			print ( '\033[91m' + ' < edit_number > function provided with unknown schema > ' + schema + '\033[0m')


	





