import json

from users.save.trials_config import save_trials_config
from users.save.charts_config import save_charts_config



def save_users_table(scope):
	
	user = scope.users['login_name']
	
	if user != 'Login to Use the Application':
		
		# Set User Variables to the values currently stored in the application
		scope.users['json'][user]['chart_height'] = scope.charts['primary_height']
		scope.users['json'][user]['download_days'] = scope.pages['download_days']
		scope.users['json'][user]['row_limit'] = scope.pages['row_limit']

		# Set User Trial and Chart Variables to the values currently stored in the application
		user_trials = save_trials_config(scope)
		user_charts = save_charts_config(scope)

		scope.users['json'][user]['trials'] = user_trials
		scope.users['json'][user]['charts'] = user_charts

		with open(scope.files['paths']['users'], 'w') as file:
			json.dump(scope.users['json'], file)







	