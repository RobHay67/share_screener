


from users.save import save_users_table

from users.restore import restore_base_config



def logout_user(scope):

	# Save the Users Settings - 
	# must be done before we start over-writing other settings
	save_users_table(scope)

	restore_base_config(scope)




