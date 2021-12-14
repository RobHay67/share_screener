import streamlit as st

from config.model.set_page_df_refresh import set_refresh_chart_dfs_for_non_screener_pages
from config.model.set_page_df_refresh import set_refresh_screener_dfs_for_screener_page


def edit_trend(scope, schema, key ):

	display_name = scope[schema][key]['name']
	
	previous_trend = scope[schema][key]['trend']

	new_trend = st.selectbox ( 
									label=('Direction for ' + display_name), 
									options=scope.screener_trends,
									index=scope.screener_trends.index(previous_trend), 
									key=key,
									) 

	if new_trend != previous_trend : 					# set to refresh pages if something has been changed
		if schema == 'screener_tests':
			scope[schema][key]['trend'] = new_trend
			set_refresh_screener_dfs_for_screener_page(scope)
		else:
			print ( '\033[91m' + ' < edit_trend > function provided with unknown schema > ' + schema + '\033[0m')

