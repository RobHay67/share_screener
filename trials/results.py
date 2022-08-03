
import pandas as pd


from trials.active_trials import scope_active_trial_list



def create_summary_of_trial_results(scope):

	app = scope.apps['display_app']
	active_trial_list = scope_active_trial_list(scope)
	column_list = ['ticker'] + active_trial_list + ['summary_result']

	# Create an overall df to store the results for every ticker and trial
	trial_results_df = pd.DataFrame(columns=column_list)

	# Iterate through the ticker_list and extract the trial results
	for ticker in scope.apps[app]['ticker_list']:

		ticker_trial_results = []
		ticker_trial_results.append(ticker)

		# Set default result to pass as a single trial 'fail'
		# will over-write the summary_result
		summary_result = 'pass'

		# Check that we have some data for this ticker
		if ticker in scope.apps[app]['dfs'].keys():
			
			ticker_df = scope.apps[app]['dfs'][ticker]

			for trial in active_trial_list:

				# trial_result = ticker_df[trial].iloc[-1]
				trial_result = ticker_df[trial].iloc[0]

				if trial_result != 'pass':
					# not all trials have passed so we fail overall
					summary_result = 'fail'		

				# Store the result for this trial in the temp dictionary
				ticker_trial_results.append(trial_result)

			# Store the overall summary result
			ticker_trial_results.append(summary_result)

			# Store tickers every trial result and the overall result in a dataframe 
			trial_results_df.loc[len(trial_results_df.index)] = ticker_trial_results


	return trial_results_df

