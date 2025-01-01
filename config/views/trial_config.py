import streamlit as st
from app.views.widgets.cols_three import three_cols


def show_trial_global_config(scope):
	diff_col_size=[2,5,3]
	with st.expander("Trial Settings", expanded=False):
		three_cols( 'Trials Configuration stored in', 		{}, "scope.trials", 			widget_type='string' )
		three_cols( 'Trials Config Dictionaries stored in', {}, "scope.trials['user_config']", 	widget_type='string' )
	
		st.divider()
		three_cols( 'Every Trial in Config Dictionary', 	scope.trials['trial_list'], 		"scope.trials['trial_list']" )
		three_cols( 'Active Trial List', 					scope.trials['active_list'], 		"scope.trials['active_list']" )
		three_cols( 'Trials that require Extra Columns', 	scope.trials['template_col_adders'],"scope.trials['template_col_adders']" )
	
	with st.expander("Trial Schemas (python dictionaries)", expanded=False):
		for trial in scope.trials['user_config'].keys():
			three_cols( trial, scope.trials['user_config'][trial], "scope.trials['user_config']["+trial+"]", diff_col_size=diff_col_size, widget_type='string')