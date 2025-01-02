import streamlit as st
from app.views.widgets.cols_three import three_cols


def show_trial_general_config(scope):
	with st.expander("Trial Settings (General)", expanded=False):
		three_cols( 'Trials Configuration stored in', {}, "scope.trials", 					widget_type='string' )
		three_cols( 'Trials User Settings stored in', {}, "scope.trials['user_config']", 	widget_type='string' )
	
		st.divider()
		three_cols( 'List of Every Trial', 				scope.trials['trial_list'], 		"scope.trials['trial_list']" )
		three_cols( 'Active Trial List', 				scope.trials['active_list'], 		"scope.trials['active_list']" )
		three_cols( 'Trials that require extra Columns',scope.charts['template_col_adders'],"scope.trials['template_col_adders']" )
		# st.divider()
		


def show_trial_user_settings(scope):
	diff_col_size=[2,5,3]
	with st.expander("User Settings", expanded=False):
		for trial in scope.trials['user_config'].keys():
			three_cols( trial, scope.trials['user_config'][trial], "scope.trials['user_config']["+trial+"]", diff_col_size=diff_col_size, widget_type='string')



def show_trial_verdicts(scope):
	diff_col_size=[2,5,3]
	verdict_keys = list(scope.tickers.keys())
	with st.expander("Trial Results (Trial Verdicts)", expanded=False):
		if len(verdict_keys)>0:
			for ticker in verdict_keys:
				st.subheader(ticker)
				three_cols( 'Passed every Test', 						scope.tickers[ticker]['screener']['verdict'], 			"scope.tickers["+ticker+"]['screener']['verdict']"			, widget_type='string' )
				three_cols( 'Do we need to update the verdict', 		scope.tickers[ticker]['screener']['replace_verdict'], 	"scope.tickers["+ticker+"]['screener']['replace_verdict']"	, widget_type='string' )
				three_cols( 'Individual Trial that ran and the verdict',scope.tickers[ticker]['screener']['trials'], 			"scope.tickers["+ticker+"]['screener']['trials']"			, widget_type='string' )
		else:
			st.write('No verdicts to display. Run some tests')


