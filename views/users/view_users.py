import streamlit as st


from users.save import save_users_table
# from targets.model.export import convert_df


def render_user_maintenance(scope):

	st.header('User Maintenance')

	col1,col2,col3,col4,col5 = st.columns([1,2,2,2,2])

	with col3:
		st.button(	
				'Save Changes to User Table', 
				on_click=save_users_table, 
				args=(scope, ), 
				key='save_user_table',
				)
	with col1:
		add_user = st.button(	
								'Add New User', 
								key='add_user_button',
								)
	with col2:
		if add_user:
			custom_label = 'Enter Name for the new User'
			render_new_user_name(scope, custom_label)
	
	with col4:
		widget_key = scope.user_name + '_download_users'
		st.download_button( 
									"Download Users Table", 
									data=convert_df(scope.user_df),
									file_name='users.csv', 
									mime='text/csv', 
									key=widget_key,
									)

	st.divider()

	list_of_users = list(scope.user_df.index.values)
	

	for user_name in list_of_users:
		col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12 = st.columns([2,2,2,2,2,2,2,2,2,2,2,2])
		with col1: 
			# Row Name
			
			st.subheader(user_name)

		with col2: # Password
			custom_label = 'Password'
			df_col_name = 'pword'
			widget_key = 'widget_' + user_name + '_' + df_col_name
			current_value = scope.user_df.loc[user_name].at[df_col_name]
			render_password_control(scope, custom_label, user_name, current_value, df_col_name, widget_key )

		with col3: # Password
			custom_label = 'View Countries (codes)'
			df_col_name = 'country_codes'
			widget_key = 'widget_' + user_name + '_' + df_col_name
			current_value = scope.user_df.loc[user_name].at[df_col_name]
			render_country_code_selector(scope, custom_label, user_name, current_value, df_col_name, widget_key )

		with col4:
			custom_label = 'Can Edit Targets'
			df_col_name = 'can_edit_targets'
			widget_key = 'widget_' + user_name + '_' + df_col_name
			current_value = scope.user_df.loc[user_name].at[df_col_name]
			render_true_or_false_control(scope, custom_label, user_name, current_value, df_col_name, widget_key )
	
		with col5: 
			custom_label = 'Can See Total Movember'
			df_col_name = 'can_see_total_movember'
			widget_key = 'widget_' + user_name + '_' + df_col_name
			current_value = scope.user_df.loc[user_name].at[df_col_name]
			render_true_or_false_control(scope, custom_label, user_name, current_value, df_col_name, widget_key )
		with col6: 
			custom_label = 'Can Edit Forex Rates'
			df_col_name = 'can_edit_forex_rates'
			widget_key = 'widget_' + user_name + '_' + df_col_name
			current_value = scope.user_df.loc[user_name].at[df_col_name]
			render_true_or_false_control(scope, custom_label, user_name, current_value, df_col_name, widget_key )
		with col7: 
			custom_label = 'Can Edit Previous Rates'
			df_col_name = 'can_edit_previous_rates'
			widget_key = 'widget_' + user_name + '_' + df_col_name
			current_value = scope.user_df.loc[user_name].at[df_col_name]
			render_true_or_false_control(scope, custom_label, user_name, current_value, df_col_name, widget_key )
		with col8: 
			custom_label = 'Can Edit Config'
			df_col_name = 'can_edit_config'
			widget_key = 'widget_' + user_name + '_' + df_col_name
			current_value = scope.user_df.loc[user_name].at[df_col_name]
			render_true_or_false_control(scope, custom_label, user_name, current_value, df_col_name, widget_key )
		with col9: 
			custom_label = 'Can Edit Users'
			df_col_name = 'can_edit_users'
			widget_key = 'widget_' + user_name + '_' + df_col_name
			current_value = scope.user_df.loc[user_name].at[df_col_name]
			render_true_or_false_control(scope, custom_label, user_name, current_value, df_col_name, widget_key )
		with col10: 
			custom_label = 'Can Download Target Rates'
			df_col_name = 'can_download_rates_table'
			widget_key = 'widget_' + user_name + '_' + df_col_name
			current_value = scope.user_df.loc[user_name].at[df_col_name]
			render_true_or_false_control(scope, custom_label, user_name, current_value, df_col_name, widget_key )

		with col11: 
			st.write('Target Setting Method')
			st.write(scope.user_df.loc[user_name].at['target_setting_method'])

		with col12: 
			st.write('Selected Country')
			st.write(scope.user_df.loc[user_name].at['selected_country'])

	st.divider()
	st.write(scope.user_df)

def render_new_user_name(scope, custom_label):
	widget_key = 'new_user'
	st.text_input(
					label=custom_label, 
					on_change=on_add_new_user,
					args=(scope, widget_key, ),
					key=(widget_key)
					)

def render_true_or_false_control(scope, custom_label, user_name, current_value, df_col_name, widget_key):
	st.write('')
	st.checkbox(
					label=custom_label, 
					# type='password',
					value=current_value,
					on_change=on_change_true_or_false,
					args=(scope, user_name, df_col_name, widget_key, ),
					key=(widget_key)
					)

def render_country_code_selector(scope, custom_label, user_name, current_value, df_col_name, widget_key ):
	st.text_input(
					label=custom_label, 
					# type='password',
					value=current_value,
					on_change=on_change_country_codes,
					args=(scope, user_name, df_col_name, widget_key, ),
					key=(widget_key)
					)



def render_password_control(scope, custom_label, user_name, current_value, df_col_name, widget_key ):
	st.text_input(
					label=custom_label, 
					# type='password',
					value=current_value,
					on_change=on_change_password,
					args=(scope, user_name, df_col_name, widget_key, ),
					key=(widget_key)
					)

def on_change_true_or_false(scope:dict, user_name:str, df_col_name:str, widget_key:str ):
	changed_value = scope[widget_key]
	# store the selection
	scope.user_df.at[user_name, df_col_name] = changed_value


def on_change_password(scope:dict, user_name:str, df_col_name:str, widget_key:str ):
	changed_value = scope[widget_key]
	# store the selection
	scope.user_df.at[user_name, df_col_name] = changed_value

def on_add_new_user(scope:dict,widget_key:str ):
	changed_value = scope[widget_key]
	
	default_user_settings = ['password', 'all', False, True, False, False, False, False, False, 'Country',  'Australia' ]

	if changed_value not in scope.user_df.index:
		scope.user_df.loc[changed_value] = default_user_settings
	else:
		st.error(changed_value + ' already exists in the users table. Try editing the user instead')




def on_change_country_codes(scope:dict, user_name:str, df_col_name:str, widget_key:str ):

	# TODO - add in some sense checking on the string to make sure it is in the correct format

	changed_value = scope[widget_key]

	# store the selection
	scope.user_df.at[user_name, df_col_name] = changed_value
