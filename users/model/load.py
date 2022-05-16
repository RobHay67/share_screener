
import pandas as pd
import os
import json

# user_file_dictionary = {
# 						'name':'str', 
# 						'password':'str',
# 						}


def load_user_table(scope):
	print(scope.files['paths']['users'])

	if os.path.exists( scope.files['paths']['users'] ):
		file = open(scope.files['paths']['users'])
		user_table = json.load(file)

		print('Loaded User Table looks like this')
		print(user_table)

		list_of_users = list(user_table.keys())

		scope.users['json'] = user_table
		scope.users['user_list'] = list_of_users

		# update the test and chart config with the user preferences




	else:
		print('='*77)
		print('ERROR - Users File does not exist > ', scope.files['paths']['users'])
		print('='*77)
		quit()




