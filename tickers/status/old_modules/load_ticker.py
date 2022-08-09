



# -------------------------------------------------------------
# Set replace_df and col_adder status for a SINGLE ticker
# -------------------------------------------------------------

def set_replace_df_status_for_ticker(scope, ticker, new_status=True):
	# For every app, set the update_df status for this ticker
	
	# If the ticker is not in the replace_status dictionary, then add it first
	# Only attempt to do the update if the status has changed. This ensures we
	# are not doing unncesasary update

	# status is usually true exept where a share data load has failed or
	# after the ticker has actually been replaced in the app dfs object and we
	# want to prevent further updates)

	for app in scope.apps['app_list']:
		
		ticker_list = list(scope.apps[app]['replace_dfs'].keys())

		current_status = replace_df_status(scope, app, ticker_list, ticker)

		if current_status != new_status:

			# only change the status if its different to the existing status

			scope.apps[app]['replace_dfs'][ticker] = new_status

			# TODO - delete this later - just for making sure we are not doing unnecesary updates
			print_status = '\033[91m' + str(new_status) + '\033[0m' if new_status == True else  '\033[92m' + str(new_status) + '\033[0m'
			print((" - scope.apps[" + app + "]['replace_dfs'][" + ticker + "] = ").ljust(80) + str(print_status) )


def set_replace_col_status_for_ticker(scope, ticker, new_status):
	# We know which ticker needs to have its status set
	# we need a list of col_adders for this ticker on this app
	# We dont know if the ticker is in the replace_cols yet so
	# we should check for that and add a default record

	for app in scope.apps['app_list']:
		
		ticker_list = list(scope.apps[app]['replace_cols'].keys())
		config_group = 'trials' if app == 'screener' else 'charts'
		col_adder_template = scope.apps['templates'][config_group].copy()
		col_adder_list = col_adder_template.keys()

		if ticker in ticker_list:
			# col_adder_list = list(scope.apps[app]['replace_cols'][ticker].keys())

			for col_adder in col_adder_list:
				# Only change the status if the col_adder is active
				if col_adder_template[col_adder]:
					scope.apps[app]['replace_cols'][ticker][col_adder] = new_status
				else:
					# Ensure it is not active
					scope.apps[app]['replace_cols'][ticker][col_adder] = False
			print_status = '\033[91m' + str(new_status) + '\033[0m' if new_status == True else  '\033[92m' + str(new_status) + '\033[0m'
			print((" - scope.apps[" + app + "]['replace_cols'][" + ticker + "][" + col_adder + "] = ").ljust(80) + str(print_status) )
		else:
			# add the ticker with the template dictionary of col_adders
			scope.apps[app]['replace_cols'][ticker] = col_adder_template
			
			# TODO - delete this later - just for making sure we are not doing unnecesary updates
			print((" - scope.apps[" + app + "]['replace_cols'][" + ticker + "] = ").ljust(80) + 'not updating')





def replace_df_status(scope, app, ticker_list, ticker):
	status = None

	if ticker in ticker_list:
		status = scope.apps[app]['replace_dfs'][ticker]
	else:
		# add a status record for this ticker
		scope.apps[app]['replace_dfs'][ticker] = status
	
	return status
