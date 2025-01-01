import streamlit as st
from app.views.widgets.cols_three import three_cols


def show_trial_verdicts(scope):
	diff_col_size=[2,5,3]
	with st.expander("Trial Results (Trial Verdicts)", expanded=False):
		for ticker in list(scope.tickers.keys()):
			st.subheader(ticker)
			three_cols( 'Passed every Test', 						scope.tickers[ticker]['screener']['verdict'], 			"scope.tickers["+ticker+"]['screener']['verdict']"			, widget_type='string' )
			three_cols( 'Do we need to update the verdict', 		scope.tickers[ticker]['screener']['replace_verdict'], 	"scope.tickers["+ticker+"]['screener']['replace_verdict']"	, widget_type='string' )
			three_cols( 'Individual Trial that ran and the verdict',scope.tickers[ticker]['screener']['trials'], 			"scope.tickers["+ticker+"]['screener']['trials']"			, widget_type='string' )




	
