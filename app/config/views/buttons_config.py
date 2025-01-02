import streamlit as st



def show_config_buttons(scope):
	col1,col2,col3,col4,col5 = st.columns(5)
	with col1: 
		st.button('Application', use_container_width=True, on_click=set_st_button, args=(scope, 'show_app_config', ))
		st.button('Folders and Paths', use_container_width=True, on_click=set_st_button, args=(scope, 'show_files_config', ))
	with col2: 
		st.button('Page(s)', use_container_width=True, on_click=set_st_button, args=(scope, 'show_page_config', ))
		st.button('Users', 			use_container_width=True, on_click=set_st_button, args=(scope, 'show_user_config', ))
	with col3: 
		st.button('Ticker Data', 	use_container_width=True, on_click=set_st_button, args=(scope, 'show_ticker_config', ))
		st.button('Missing Tickers',use_container_width=True, on_click=set_st_button, args=(scope, 'show_missing_ticker_config', ))
	with col4: 		
		st.button('Charts', 			use_container_width=True, on_click=set_st_button, args=(scope, 'show_chart_config', ))
		st.button('Y Finance', 		use_container_width=True, on_click=set_st_button, args=(scope, 'show_y_finance_config', ))
	with col5: 
		st.button('Trials', 			use_container_width=True, on_click=set_st_button, args=(scope, 'show_trial_config', ))
		st.button('Strategies (WIP)', 	use_container_width=True, on_click=set_st_button, args=(scope, 'show_strategy_config', ))
	

def set_st_button(scope:dict, show_config:str):
	previous_value = scope.pages['render_config']
	if previous_value == show_config: 
		scope.pages['render_config'] = None
	else:
		scope.pages['render_config'] = show_config













