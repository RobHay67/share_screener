


from users.save import save_users_table

from users.defaults import set_user_defaults



def logout_user(scope):

	# Save the Users Settings - must be done before we start over-writing other settings
	save_users_table(scope)

	set_user_defaults(scope)




