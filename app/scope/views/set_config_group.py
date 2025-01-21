import streamlit as st


def show_config_group_selection_buttons(scope):
	col1,col2,col3,col4,col5 = st.columns(5)
	with col1: 
		# st.button('Summary', 			use_container_width=True, on_click=set_st_button, args=(scope, 'show_scope_config', ))
		st.button('Application (scope.config)', use_container_width=True, on_click=set_st_button, args=(scope, 'show_scope_config', ))
		st.button('Folders and Paths', 	use_container_width=True, on_click=set_st_button, args=(scope, 'show_scope_files', ))
	with col2: 
		st.button('Page(s)', 			use_container_width=True, on_click=set_st_button, args=(scope, 'show_scope_page', ))
		st.button('Users', 				use_container_width=True, on_click=set_st_button, args=(scope, 'show_scope_users', ))
	with col3: 
		st.button('Ticker Index',		use_container_width=True, on_click=set_st_button, args=(scope, 'show_scope_ticker_index', ))
		# This should be config
		st.button('Tickers',			use_container_width=True, on_click=set_st_button, args=(scope, 'show_scope_tickers', ))
		# this should be ticker data
		st.button('Ticker Data', 		use_container_width=True, on_click=set_st_button, args=(scope, 'show_ticker_general_config', ))
		st.button('Y Finance', 			use_container_width=True, on_click=set_st_button, args=(scope, 'show_scope_yf', ))
	
	
	with col4: 		
		st.button('Charts', 			use_container_width=True, on_click=set_st_button, args=(scope, 'show_scope_chart', ))
	with col5: 
		st.button('Trials', 			use_container_width=True, on_click=set_st_button, args=(scope, 'show_trial_config', ))
		st.button('Strategies (WIP)', 	use_container_width=True, on_click=set_st_button, args=(scope, 'show_scope_strategy', ))
	
	st.divider()

def set_st_button(scope:dict, show_config:str):
	previous_value = scope.config['display_scope']['config_page']
	if previous_value == show_config: 
		scope.config['display_scope']['config_page'] = None
	else:
		scope.config['display_scope']['config_page'] = show_config













