
import streamlit as st

from apps.config_app.three_cols import three_cols



def view_trials_config(scope):
	st.caption('Trials Configuration - Raw Dictionary and Lists')
	three_cols( 'Trial List', scope.trial_config['trial_list'], 'scope.trial_config.trial_list' )
	three_cols( 'Trial Active List', scope.trial_config['active_list'], 'scope.trial_config.active_list' )
	three_cols( 'Trial Column Adders', scope.trial_config['column_adders'], 'scope.trial_config.column_adders' )

	st.markdown("""---""")
	
	for trial in  scope.trial_config['trial_list']:
		st.subheader(trial)
		st.write('scope.trials['+trial+']')
		st.write(scope.trials[trial])