import streamlit as st

from pages.config.three_cols import three_cols


def view_trials_config(scope):

	st.write('---')
	st.subheader('Trials Configuration - Raw Configuration Dictionaries')
	three_cols( 'Trials Configuration stored in', {}, 'scope.trials', widget_type='string' )
	for trial in scope.trials.keys():
		three_cols( trial, scope.trials[trial], 'scope.trials['+trial+']', widget_type='string' )		
