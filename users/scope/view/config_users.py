import streamlit as st
from config.scope.views.buttons.button_choose_scope import scope_button
from config.scope.views.buttons.button_data_type import data_type_button
from config.scope.views.buttons.show_config_value import show_config_single_value, show_config_values
from config.scope.views.buttons.dropdown_choose_scope import scope_dropdown


def show_config_users(scope):

	scope_button(scope, "Users", scope.users, make_red=True, suffix_only=False)
	scope_button(scope, "scope.users", scope.users, make_red=False, suffix_only=False)
	
	col1,col2,col3,col4 = st.columns([1,1,1,6])
	with col1:scope_button(scope, "scope.users['user_list']", scope.users['user_list'])
	with col2:scope_button(scope, "scope.users['login_name']", scope.users['login_name'])
	with col3:scope_button(scope, "scope.users['logged_in']", scope.users['logged_in'])
	with col4:scope_button(scope, "scope.users['json']", scope.users['json'])
	with col4:scope_button(scope, "scope.users['json']['Rob', 'Fliss']", "Rob, Fliss")
	
	col1,col2,col3,col4,col5,col6,col7,col8,col9 = st.columns(9)
	user = scope.users['login_name']
	with col4:scope_button(scope, "scope.users['json'][user]['chart_height']", scope.users['json'][user]['chart_height'])
	with col5:scope_button(scope, "scope.users['json'][user][download_days]", scope.users['json'][user]['download_days'])
	with col6:scope_button(scope, "scope.users['json'][user][row_limit]", scope.users['json'][user]['row_limit'])
	with col7:scope_button(scope, "scope.users['json'][user][password]", scope.users['json'][user]['password'])
	with col8:scope_button(scope, "scope.users['json'][user][charts]", scope.users['json'][user]['charts'])
	with col9:scope_button(scope, "scope.users['json'][user][trials]", scope.users['json'][user]['trials'])
	
	col1,col2,col3,col4,col5,col6,col7,col8,col9 = st.columns(9)
	with col1:data_type_button(scope, 'list', 1)
	with col2:data_type_button(scope, 'string', 1)
	with col3:data_type_button(scope, 'true_false', 1)
	with col4:data_type_button(scope, 'integer', 1)
	with col5:data_type_button(scope, 'integer', 2)
	with col6:data_type_button(scope, 'integer', 3)
	with col7:data_type_button(scope, 'password', 1)
	with col8:data_type_button(scope, 'dict', 1)
	with col9:data_type_button(scope, 'dict', 2)

	col1,col2,col3,col4,col5,col6,col7,col8,col9 = st.columns(9)
	with col2:show_config_single_value("login_name", scope.users['login_name'])
	with col3:show_config_single_value("logged_in", scope.users['logged_in'])
	with col4:show_config_single_value("chart_height", scope.users['json'][user]['chart_height'])
	with col5:show_config_single_value("download_days", scope.users['json'][user]['download_days'])
	with col6:show_config_single_value("row_limit", scope.users['json'][user]['row_limit'])

	st.divider()
	if scope.display['config_key'] != None:
		show_config_values(scope)
