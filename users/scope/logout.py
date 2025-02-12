import logging
from users.scope.save.controller import save_users_table
from users.scope.restore import set_user_config_to_default_values

def logout_user(scope):
	logging.warning("logout_user")
	# Save the Users Settings - 
	# must be done before we start over-writing other settings
	save_users_table(scope)

	set_user_config_to_default_values(scope)





