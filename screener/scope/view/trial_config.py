import streamlit as st
from app.views.widgets.cols_three import three_cols
from app.scope.views.buttons.button_choose_scope import scope_button
from app.scope.views.buttons.button_data_type import data_type_button
from app.scope.views.buttons.show_scope_value import show_scope_single_value, show_scope_values
from app.scope.views.buttons.dropdown_choose_scope import scope_dropdown



def show_scope_trials(scope):

	st.divider()
	scope_button(scope, "scope.trials", scope.trials, make_red=True, suffix_only=False)
	
	col1,col2,col3,col4 = st.columns([1,1,1,5])
	with col1:scope_button(scope, "scope.trials['trial_list']", scope.trials['trial_list'])
	with col2:scope_button(scope, "scope.trials['active_list']", scope.trials['active_list'])
	with col3:scope_button(scope, "scope.trials['template_col_adders']", scope.trials['template_col_adders'])
	with col4:scope_button(scope, "scope.trials['user_config']", scope.trials['user_config'])

	col1,col2 = st.columns([3,5])
	trial = next(iter(scope.trials['user_config'].keys()))
	with col2:scope_button(scope, "scope.trials['user_config'][trial]", scope.trials['user_config'], make_red=False, suffix_only=False)
	with col2:scope_button(scope, '[trial] = '+trial, scope.trials['user_config'], make_red=False, suffix_only=False)

	
	col1,col2,col3,col4,col5,col6 = st.columns([3,1,1,1,1,1])
	with col2:scope_button(scope, "scope.trials['user_config']["+trial+"]['active']", scope.trials['user_config'][trial]['active'])
	with col3:scope_button(scope, "scope.trials['user_config']["+trial+"]['name']", scope.trials['user_config'][trial]['name'])
	with col4:scope_button(scope, "scope.trials['user_config']["+trial+"]['short_name']", scope.trials['user_config'][trial]['short_name'])
	with col5:scope_button(scope, "scope.trials['user_config']["+trial+"]['definition']", scope.trials['user_config'][trial]['definition'])
	with col6:scope_button(scope, "scope.trials['user_config']["+trial+"]['add_columns']", scope.trials['user_config'][trial]['add_columns'])


	# st.divider()
	if scope.config['display_scope']['scope_key'] != None:
		show_scope_values(scope)


		


def show_trial_verdicts(scope):
	verdict_keys = list(scope.tickers.keys())
	with st.expander("Trial Results (Verdicts)", expanded=False):
		if len(verdict_keys)>0:
			for ticker in verdict_keys:
				st.subheader(ticker)
				three_cols( 'Passed every Test', 						scope.tickers[ticker]['screener']['verdict'], 			"scope.tickers["+ticker+"]['screener']['verdict']"			, widget_type='string' )
				three_cols( 'Do we need to update the verdict', 		scope.tickers[ticker]['screener']['replace_verdict'], 	"scope.tickers["+ticker+"]['screener']['replace_verdict']"	, widget_type='string' )
				three_cols( 'Individual Trial that ran and the verdict',scope.tickers[ticker]['screener']['trials'], 			"scope.tickers["+ticker+"]['screener']['trials']"			, widget_type='string' )
		else:
			st.write('No verdicts to display. Run some tests')


