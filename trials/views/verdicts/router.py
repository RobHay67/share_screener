# Display the Results from all the tests run on the ticker data
# - limit to tickers in the page worklist
# - ensure we have actually added columns to the ticker
# - expecting the verdicts to be stored in scope.tickers[ticker]['trials']['overall_verdict']


import logging

from trials.helpers.verdicts_passing import build_passing_verdict_list
from trials.views.verdicts.failed_all_tests import show_all_verdicts_failed
from trials.views.verdicts.passed_too_many import show_too_many_verdicts
from trials.views.verdicts.passed_tests import show_passing_verdicts



def router_show_verdicts(scope):
	logging.debug("router_show_verdicts")
	tab_group_size 	= 10
	number_of_tabs 	= 30
	verdict_list 	= build_passing_verdict_list(scope)
	qty_of_verdicts	= len(verdict_list)
	match qty_of_verdicts:
		case 0:
			show_all_verdicts_failed()
		case _ if qty_of_verdicts > (tab_group_size * number_of_tabs):
			show_too_many_verdicts(qty_of_verdicts, number_of_tabs, tab_group_size)
		case _:
			show_passing_verdicts(scope, qty_of_verdicts, tab_group_size, verdict_list)

