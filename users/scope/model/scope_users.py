import logging
from users.scope.model.load import load_user_table



def scope_users(scope):
	logging.warning("scope_users")
	scope.users = {}
	scope.users['json'] = {}
	scope.users['user_list'] = []
	scope_users_for_users(scope)
	load_user_table(scope)


def scope_users_for_users(scope):
	logging.warning("scope_users_for_users")
	# Setting can be changed for each user
	# so we need to be able to call when changing user

	scope.users['login_name'] = 'Login to Use the Application'
	scope.users['logged_in'] = False






