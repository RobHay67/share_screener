import streamlit as st

from pages.config.three_cols import three_cols


def render_trials_config(scope):
	diff_col_size=[2,5,3]

	with st.expander("Trial Settings", expanded=False):
		three_cols( 'Trials Configuration stored in', {}, "scope.trials", widget_type='string' )
		three_cols( 'Trials Config Dictionaries stored in', {}, "scope.trials['config']", widget_type='string' )
	
		st.divider()
		three_cols( 'Every Trial in Config Dictionary', scope.trials['trial_list'], "scope.trials['trial_list']" )
		three_cols( 'Active Trial List', scope.trials['active_list'], "scope.trials['active_list']" )
		three_cols( 'Trials that require Extra Columns', scope.trials['template_col_adders'], "scope.trials['template_col_adders']" )
	

	with st.expander("Trial Results (Trial Verdicts)", expanded=False):
		for ticker in list(scope.tickers.keys()):
			st.subheader(ticker)
			three_cols( 'Passed every Test', 						scope.tickers[ticker]['screener']['verdict'], 			"scope.tickers["+ticker+"]['screener']['verdict']"			, widget_type='string' )
			three_cols( 'Do we need to update the verdict', 		scope.tickers[ticker]['screener']['replace_verdict'], 	"scope.tickers["+ticker+"]['screener']['replace_verdict']"	, widget_type='string' )
			three_cols( 'Individual Trial that ran and the verdict',scope.tickers[ticker]['screener']['trials'], 			"scope.tickers["+ticker+"]['screener']['trials']"			, widget_type='string' )

	with st.expander("Trial Dictionaries (python code)", expanded=False):
		for trial in scope.trials['config'].keys():
			three_cols( trial, scope.trials['config'][trial], "scope.trials['config']["+trial+"]", diff_col_size=diff_col_size, widget_type='string')