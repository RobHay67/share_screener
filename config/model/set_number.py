import streamlit as st


from config.model.set_chart_refresh import set_refresh_charts_for_all_pages


	
def edit_number(scope, schema, key, column ):
	
	display_name = scope[schema][key]['name']
	column_name = column.capitalize()
	
	if schema == 'charts':
		previous_period = int(scope[schema][key]['data_cols'][column])
	else:
		previous_period = int(scope[schema][key][column])


	input_period_no = st.number_input(
										# column_name,
										label=(column_name + ' for ' + display_name), 
										min_value=0, 
										value=previous_period,
										key=display_name
										)  

	if schema == 'charts':
		scope[schema][key]['data_cols'][column] = input_period_no
		if input_period_no != previous_period :
			set_refresh_charts_for_all_pages(scope)
	else:
		scope[schema][key][column] = input_period_no


	

	





