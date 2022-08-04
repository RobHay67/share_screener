
import streamlit as st
from datetime import datetime 

from progress.three_cols import three_cols


def view_app(scope):
	st.subheader('Application')
	three_cols( 'Project Description', scope.config['project_description'], 'scope.config.project_description' )

	start_time =  datetime.fromtimestamp(scope.config['project_start_time']).strftime('%Y-%m-%d %H:%M:%S %p')
	three_cols( 'Project Start Time', start_time, 'scope.config.project_start_time' )


	st.subheader('Share Market')
	three_cols( 'Current Share Market', scope.config['share_market'], 'scope.config.share_market' )

	st.subheader('System')
	three_cols( 'Initial Load ?', scope.initial_load, 'initial_load' )
	



def view_trials_config(scope):
	st.subheader('Trials Configuration')
	
	three_cols( 'Trends', scope.trials['trends'], 'scope.apps.trials.trends' )
	three_cols( 'Test List', scope.trials['trial_list'], 'scope.apps.trials.trial_list' )

	st.markdown("""---""")
	
	for trial in  scope.trials['trial_list']:
		st.subheader(trial)
		st.write('scope.trials['+trial+']')
		st.write(scope.trials[trial])


def view_charts_config(scope):
	st.subheader('Charts Configuration')
	
	three_cols( 'Colours', scope.charts['colours'], 'scope.apps.charts.colours' )
	three_cols( 'Total Chart Height', scope.charts['total_height'], 'scope.apps.charts.total_height' )
	three_cols( 'Height of Primary Charts', scope.charts['primary_height'], 'scope.apps.charts.primary_height' )
	three_cols( 'Chart List', scope.charts['chart_list'], 'scope.apps.charts.chart_list' )

	st.markdown("""---""")
	
	for chart in  scope.charts['chart_list']:
		st.subheader(chart)
		st.write('scope.config.charts['+chart+']')
		st.write(scope.charts[chart])
