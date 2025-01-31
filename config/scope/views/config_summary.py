import logging
import streamlit as st


def show_config_summary(scope):
	logging.debug("show_config_summary")
	st.button('Overview (basic structure of App)', use_container_width=True, on_click=set_st_button, args=(scope, 'route_config_summary', ))

	col1,col2,col3,col4,col5,col6 = st.columns([1,1,1,1,3,3])
	
	with col1:st.button('Config (App)', 	use_container_width=True, on_click=set_st_button, args=(scope, 'route_config_config', ))
	with col2:st.button('Folders and Paths',use_container_width=True, on_click=set_st_button, args=(scope, 'route_config_files', ))
	with col3:st.button('Users', 			use_container_width=True, on_click=set_st_button, args=(scope, 'route_config_users', ))
	with col4:st.button('Ticker Index',		use_container_width=True, on_click=set_st_button, args=(scope, 'route_config_ticker_index', ))
	with col5:st.button('Tickers (Data)',	use_container_width=True, on_click=set_st_button, args=(scope, 'route_config_tickers', ))
	with col6:st.button('Page(s)', 			use_container_width=True, on_click=set_st_button, args=(scope, 'route_config_page', ))

	col1,col2,col3,col4,col5,col6,col7,col8 = st.columns([1,3,1,1,1,1,1,1])
	with col1:st.button('Display Config', 	use_container_width=True, on_click=set_st_button, args=(scope, 'route_config_display', ))
	with col3:st.button('Ticker Schema', 	use_container_width=True, on_click=set_st_button, args=(scope, 'route_config_tickers_schema', ))
	with col4:st.button('Y Finance', 		use_container_width=True, on_click=set_st_button, args=(scope, 'route_config_yf', ))
	with col5:st.button('Verdicts', 		use_container_width=True, on_click=set_st_button, args=(scope, 'route_config_verdicts', ))
	with col6: st.button('Trials', 			use_container_width=True, on_click=set_st_button, args=(scope, 'route_config_trial', ))
	with col7: st.button('Strategies (WIP)',use_container_width=True, on_click=set_st_button, args=(scope, 'route_config_strategy', ))
	with col8: st.button('Charts', 			use_container_width=True, on_click=set_st_button, args=(scope, 'route_config_chart', ))

	st.divider()


def set_st_button(scope:dict, show_config:str):
	logging.debug("set_st_button")
	previous_value = scope.display['config_page']
	if previous_value == show_config: 
		scope.display['config_page'] = None
	else:
		scope.display['config_page'] = show_config














