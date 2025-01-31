import logging
import streamlit as st
from config.scope.views.buttons.button_choose_scope import scope_button
from config.scope.views.buttons.button_data_type import data_type_button
from config.scope.views.buttons.show_config_value import show_config_single_value, show_config_values, show_config_note
from config.scope.views.buttons.dropdown_choose_scope import scope_dropdown



def show_config_trials(scope):
	logging.debug("show_config_trials")
	scope_button(scope, "Trials", scope.trials, make_red=True, suffix_only=False)
	scope_button(scope, "scope.trials", scope.trials, make_red=False, suffix_only=False)
	
	col1,col2,col3,col4,col5 = st.columns([1,1,1,1,5])
	with col1:scope_button(scope, "scope.trials['schema']", scope.trials['schema'])
	with col2:scope_button(scope, "scope.trials['trial_list']", scope.trials['trial_list'])
	with col3:scope_button(scope, "scope.trials['active_list']", scope.trials['active_list'])
	with col4:scope_button(scope, "scope.trials['template_col_adders']", scope.trials['template_col_adders'])
	with col5:scope_button(scope, "scope.trials['user_config']", scope.trials['user_config'])

	col1,col2,col3,col4,col5 = st.columns([1,1,1,1,5])
	trial_list = scope.trials['trial_list']
	with col1:show_config_note("schema", 'actual code for every trial')
	with col2:show_config_note("trial_list", 'list of every trial available')
	with col3:show_config_note("active_list", 'list of every ACTIVE trial')
	with col4:show_config_note("template_col_adders", 'dictionary of every trial which has column adders. Value is the active status')

	with col5:trial = scope_dropdown(scope, 'Trial', trial_list )
	with col5:scope_button(scope, "['trial'] = "+trial, scope.trials['user_config'][trial], make_red=False, suffix_only=False)
	
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


		
