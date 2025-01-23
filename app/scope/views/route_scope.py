import streamlit as st


def show_config_group_selection_buttons(scope):
	col1,col2,col3,col4,col5,col6 = st.columns(6)
	with col1: 
		st.button('Summary', 			use_container_width=True, on_click=set_st_button, args=(scope, 'route_config_summary', ))
		st.button('Config (App)', 		use_container_width=True, on_click=set_st_button, args=(scope, 'route_config_config', ))
	with col2: 
		st.button('Users', 				use_container_width=True, on_click=set_st_button, args=(scope, 'route_config_users', ))
		st.button('Folders and Paths', 	use_container_width=True, on_click=set_st_button, args=(scope, 'route_config_files', ))
	with col3: 
		st.button('Ticker Index',		use_container_width=True, on_click=set_st_button, args=(scope, 'route_config_ticker_index', ))
		st.button('Y Finance', 			use_container_width=True, on_click=set_st_button, args=(scope, 'route_config_yf', ))
		st.button('Verdicts', 			use_container_width=True, on_click=set_st_button, args=(scope, 'route_config_verdicts', ))
	with col4: 	
		st.button('Tickers (Data)',		use_container_width=True, on_click=set_st_button, args=(scope, 'route_config_tickers', ))
		st.button('Ticker Schema', 		use_container_width=True, on_click=set_st_button, args=(scope, 'route_config_tickers_schema', ))
	with col5: 
		st.button('Trials', 			use_container_width=True, on_click=set_st_button, args=(scope, 'route_config_trial', ))
		st.button('Strategies (WIP)', 	use_container_width=True, on_click=set_st_button, args=(scope, 'route_config_strategy', ))
	with col6:
		st.button('Page(s)', 			use_container_width=True, on_click=set_st_button, args=(scope, 'route_config_page', ))
		st.button('Charts', 			use_container_width=True, on_click=set_st_button, args=(scope, 'route_config_chart', ))

	st.divider()

def set_st_button(scope:dict, show_config:str):
	previous_value = scope.config['display_scope']['config_page']
	if previous_value == show_config: 
		scope.config['display_scope']['config_page'] = None
	else:
		scope.config['display_scope']['config_page'] = show_config














