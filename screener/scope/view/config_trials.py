import streamlit as st
from app.views.widgets.cols_three import three_cols
from app.scope.views.buttons.button_choose_scope import scope_button
from app.scope.views.buttons.button_data_type import data_type_button
from app.scope.views.buttons.show_config_value import show_config_single_value, show_config_values
from app.scope.views.buttons.dropdown_choose_scope import scope_dropdown



def show_config_trials(scope):

	scope_button(scope, "Trials", scope.trials, make_red=True, suffix_only=False)
	scope_button(scope, "scope.trials", scope.trials, make_red=False, suffix_only=False)
	
	col1,col2,col3,col4 = st.columns([1,1,1,5])
	with col1:scope_button(scope, "scope.trials['trial_list']", scope.trials['trial_list'])
	with col2:scope_button(scope, "scope.trials['active_list']", scope.trials['active_list'])
	with col3:scope_button(scope, "scope.trials['template_col_adders']", scope.trials['template_col_adders'])
	with col4:scope_button(scope, "scope.trials['user_config']", scope.trials['user_config'])

	col1,col2 = st.columns([3,5])
	trial_list = scope.trials['trial_list']
	with col2:trial = scope_dropdown(scope, 'trial', trial_list )
	with col2:scope_button(scope, "['trial'] = "+trial, scope.trials['user_config'][trial], make_red=False, suffix_only=False)
	
	col1,col2,col3,col4,col5,col6 = st.columns([3,1,1,1,1,1])
	with col2:scope_button(scope, "scope.trials['user_config']["+trial+"]['active']", scope.trials['user_config'][trial]['active'])
	with col3:scope_button(scope, "scope.trials['user_config']["+trial+"]['name']", scope.trials['user_config'][trial]['name'])
	with col4:scope_button(scope, "scope.trials['user_config']["+trial+"]['short_name']", scope.trials['user_config'][trial]['short_name'])
	with col5:scope_button(scope, "scope.trials['user_config']["+trial+"]['definition']", scope.trials['user_config'][trial]['definition'])
	with col6:scope_button(scope, "scope.trials['user_config']["+trial+"]['function']", scope.trials['user_config'][trial]['function'])

	with col2:show_config_single_value("active", scope.trials['user_config'][trial]['active'])
	with col3:show_config_single_value("name", scope.trials['user_config'][trial]['name'])
	with col4:show_config_single_value("short_name", scope.trials['user_config'][trial]['short_name'])
	# with col5:show_config_single_value("definition", scope.trials['user_config'][trial]['definition'])
	# with col6:show_config_single_value("add_columns", scope.trials['user_config'][trial]['function'])

	st.divider()
	if scope.display['config_key'] != None:
		show_config_values(scope)


		
