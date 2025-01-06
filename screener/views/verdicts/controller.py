# Display the Results from all the tests run on the ticker data
# - limit to tickers in the page worklist
# - ensure we have actually added columns to the ticker
# - expecting the verdicts to be stored in scope.tickers[ticker]['trials']['verdict']


import streamlit as st

from screener.views.verdicts.failed_all_tests import show_all_verdicts_failed
from screener.views.verdicts.passed_too_many import show_too_many_verdicts
from screener.views.verdicts.passed_tests import show_passing_verdicts
from screener.views.active_trials.active_tests import show_active_trials
from screener.views.verdicts.passed_tests import passing_verdict_list


def show_verdicts(scope):
	tab_group_size 	= 10
	number_of_tabs 	= 30
	verdict_list 	= passing_verdict_list(scope)
	no_of_verdicts 	= len(verdict_list)

	if no_of_verdicts == 0:
		show_all_verdicts_failed()
	elif no_of_verdicts > (tab_group_size * number_of_tabs):
		show_too_many_verdicts(no_of_verdicts, number_of_tabs, tab_group_size)
	else:
		show_passing_verdicts(scope, no_of_verdicts, tab_group_size, verdict_list)

	show_active_trials(scope)



