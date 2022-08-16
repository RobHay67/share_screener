
from users.load import load_user_table


def scope_users(scope:dict):

	scope.users = {}
	scope.users['json'] = {}
	scope.users['user_list'] = []
	base_config_users(scope)

	load_user_table(scope)


def base_config_users(scope):
	# Setting can be changed for each user
	# so we need to be able to call when changing user

	scope.users['login_name'] = 'Login to Use the Application'