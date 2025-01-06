
import os
import json


def load_user_table(scope):

	if os.path.exists( scope.files['paths']['users'] ):
		file = open(scope.files['paths']['users'])
		user_table = json.load(file)

		list_of_users = list(user_table.keys())

		scope.users['json'] = user_table
		scope.users['user_list'] = list_of_users
	else:
		print('='*77)
		print('ERROR - Users File does not exist > ', scope.files['paths']['users'])
		print('='*77)
		quit()
