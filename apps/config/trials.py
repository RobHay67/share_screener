import streamlit as st

from apps.config.three_cols import three_cols


def view_trials_config(scope):

	st.subheader('Global Trial Configuration')
	three_cols( 'Global Trial Configuration stored in', {}, 'scope.trial_config', widget_type='string' )
	three_cols( 'Every available Trial', scope.trial_config['trial_list'], "scope.trial_config['trial_list']" )
	three_cols( 'Active Trial List', scope.trial_config['active_list'], "scope.trial_config['active_list']" )
	three_cols( 'Trials which require Column Adders', scope.trial_config['column_adders'], "scope.trial_config['column_adders']" )


	st.write('---')
	st.subheader('Trials Configuration - Raw Configuration Dictionaries')
	three_cols( 'Trials Configuration stored in', {}, 'scope.trials', widget_type='string' )
	for trial in  scope.trial_config['trial_list']:
		three_cols( trial, scope.trials[trial], 'scope.trials['+trial+']', widget_type='string' )		
