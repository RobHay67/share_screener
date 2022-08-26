
from unittest import result
import pandas as pd


# from trials.active_trials import scope_active_trial_list



def trial_results(scope):

	app = scope.apps['display_app']
	# TODO - this should be stored in scope???
	# active_trial_list = scope_active_trial_list(scope)
	active_trial_list = scope.trial_config['active_list']

	column_list = ['ticker'] + active_trial_list + ['overall_result']

	trial_results_df = pd.DataFrame(columns=column_list)
	
	for ticker in scope.apps[app]['worklist']:

		trial_results_for_ticker = []
		trial_results_for_ticker.append(ticker)

		# Set default result to pass as a single trial 'fail'
		# will over-write the overall_result
		overall_result = 'pass'

		# Check that we have some data for this ticker
		# if ticker in scope.apps[app]['dfs'].keys():
		if ticker in scope.apps[app]['mined_tickers']:
			
			# ticker_df = scope.tickers[ticker][app]['df']

			# if ticker == 'MIN.AX':
			# 	print(ticker_df)

			for trial in active_trial_list:

				# trial_result = ticker_df[trial].iloc[-1]
				# trial_result = ticker_df[trial].iloc[0]
				trial_result = scope.tickers[ticker][app]['df'][trial].iloc[0]

				if trial_result != 'pass':
					# not all trials have passed so we fail overall
					overall_result = 'fail'		

				# Store the result for this trial in the temp dictionary
				trial_results_for_ticker.append(trial_result)

			# Store the overall summary result
			trial_results_for_ticker.append(overall_result)

			# Store tickers every trial result and the overall result in a dataframe 
			trial_results_df.loc[len(trial_results_df.index)] = trial_results_for_ticker


	return trial_results_df




# ticker  : { trial1 : result,
# 			trial2 : result,
# 			trial3 : result, }