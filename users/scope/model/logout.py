import logging
from users.scope.model.save.controller import save_users_table
from users.scope.model.restore import restore_user_config


def logout_user(scope):
	logging.warning("logout_user")
	# Save the Users Settings - 
	# must be done before we start over-writing other settings
	save_users_table(scope)

	restore_user_config(scope)




