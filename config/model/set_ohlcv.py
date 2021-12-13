import streamlit as st


# from config.model.set_chart_refresh import set_refresh_chart_dfs_for_most_pages
from config.model.set_page_df_refresh import set_refresh_chart_dfs_for_most_pages





# TODO - column is in a different spot for charts and analysis - how to fix this Rob ????




def edit_ohlcv(scope, schema, key ):
	
	display_name = scope[schema][key]['name']
	
	if schema == 'charts':
		previous_column = scope[schema][key]['data_cols']['column']
	else:
		previous_column = scope[schema][key]['column']
	
	
	selected_column = st.selectbox ( 
									label=('Column for ' + display_name), 
									options=scope.dropdown_ohlcv_columns,
									index=scope.dropdown_ohlcv_columns.index(previous_column), 
									key=key,
									) 

	if schema == 'charts':
		scope[schema][key]['data_cols']['column'] = selected_column
		if selected_column != previous_column : 
			set_refresh_chart_dfs_for_most_pages(scope)
	else:
		scope[schema][key]['column'] = selected_column

			
	


def edit_price(scope, schema, key ):
	
	display_name = scope[schema][key]['name']
	
	if schema == 'charts':
		previous_column = scope[schema][key]['data_cols']['column']
	else:
		previous_column = scope[schema][key]['column']
	

	selected_column = st.selectbox ( 
									label=('Column for ' + display_name), 
									options=scope.dropdown_price_columns,
									index=scope.dropdown_price_columns.index(previous_column), 
									key=key,
									) 

	if schema == 'charts':
		scope[schema][key]['data_cols']['column'] = selected_column
		if selected_column != previous_column : 
			set_refresh_chart_dfs_for_most_pages(scope)
	else:
		scope[schema][key]['column'] = selected_column



