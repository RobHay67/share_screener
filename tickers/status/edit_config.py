


# -------------------------------------------------------------
# set col_adder status for a SINGLE col_adder function
# -------------------------------------------------------------

def set_replace_col_status_for_col_adder(scope, col_adder, new_status=True):
	# Called when one of the widgets has been changed
	# so this will be the chart or the trial col_adder variables
	# we only want to make changes where the trial or chart exists

	for app in scope.apps['app_list']:

		ticker_list = list(scope.apps[app]['replace_cols'].keys())

		for ticker in ticker_list:

			col_adder_list = list(scope.apps[app]['replace_cols'][ticker].keys())

			if col_adder in col_adder_list:
				status = scope.apps[app]['replace_cols'][ticker][col_adder]

			# current_status = replace_cols_status(scope, app, ticker, col_adder_list, col_adder)

				if status != new_status:
					# only change the status if its different to the existing status

					scope.apps[app]['replace_cols'][ticker][col_adder] = new_status

					# TODO - delete this later - just for making sure we are not doing unnecesary updates
					print_status = '\033[91m' + str(new_status) + '\033[0m' if new_status == True else  '\033[92m' + str(new_status) + '\033[0m'
					print((" - scope.apps[" + app + "]['replace_cols'][" + ticker + "][" + col_adder + "] = ").ljust(80) + str(print_status) )

