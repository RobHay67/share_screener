# Function to open the expander if any of the settings are currently active
import logging

def set_expander_status(scope, settings_group):
	logging.warning("set_expander_status")
	open_expanded = False
	for trial in settings_group:
		if scope.trials['user_config'][trial]['active']:
			open_expanded=True
			break
	return open_expanded

