
from screener.scope.model.schema import trials_schema

def user_config_trials(scope):
	# store the trial configuration dictionary (from below)
	scope.trials['user_config'] = {}
	for trial, configuration in trials_schema.items():
		scope.trials['user_config'][trial] = configuration.copy()



