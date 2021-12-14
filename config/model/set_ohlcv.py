import streamlit as st


from config.model.set_page_df_refresh import set_refresh_chart_dfs_for_non_screener_pages
from config.model.set_page_df_refresh import set_refresh_screener_dfs_for_screener_page


def edit_ohlcv(scope, schema, key ):
	
	display_name = scope[schema][key]['name']
	
	if schema == 'charts':
		previous_ohlcv_col = scope[schema][key]['data_cols']['column']
	else:
		previous_ohlcv_col = scope[schema][key]['column']
	
	
	new_ohlcv_col = st.selectbox ( 
									label=('Column for ' + display_name), 
									options=scope.dropdown_ohlcv_columns,
									index=scope.dropdown_ohlcv_columns.index(previous_ohlcv_col), 
									key=key,
									) 

	if new_ohlcv_col != previous_ohlcv_col : 					# set to refresh pages if something has been changed
		if schema == 'charts':
			scope[schema][key]['data_cols']['column'] = new_ohlcv_col
			set_refresh_chart_dfs_for_non_screener_pages(scope)
		elif schema == 'screener_tests':
			scope[schema][key]['column'] = new_ohlcv_col
			set_refresh_screener_dfs_for_screener_page(scope)
		else:
			print ( '\033[91m' + ' < edit_ohlcv > function provided with unknown schema > ' + schema + '\033[0m')



def edit_ohlc(scope, schema, key ):
	
	display_name = scope[schema][key]['name']
	
	if schema == 'charts':
		previous_ohlcv_col = scope[schema][key]['data_cols']['column']
	else:
		previous_ohlcv_col = scope[schema][key]['column']

	new_ohlc_col = st.selectbox ( 
									label=('Column for ' + display_name), 
									options=scope.dropdown_price_columns,
									index=scope.dropdown_price_columns.index(previous_ohlcv_col), 
									key=key,
									) 

	if new_ohlc_col != previous_ohlcv_col : 					# set to refresh pages if something has been changed
		if schema == 'charts':
			scope[schema][key]['data_cols']['column'] = new_ohlc_col
			set_refresh_chart_dfs_for_non_screener_pages(scope)
		elif schema == 'screener_tests':
			scope[schema][key]['column'] = new_ohlc_col
			set_refresh_screener_dfs_for_screener_page(scope)
		else:
			print ( '\033[91m' + ' < edit_ohlc > function provided with unknown schema > ' + schema + '\033[0m')
