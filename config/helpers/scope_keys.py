import logging
import streamlit as st


def print_scope_keys(location='Not Specified'):
	logging.debug("print_scope_keys")
	print('='*66)
	print('\033[95m Called From > '+location+'\033[0m')
	counter = 0; widgets = 0;hide_widgets = True
	for key in sorted(st.session_state):
		# print(counter)
		if key[:6] == 'widget':
			widgets+=1
			if hide_widgets==False:print(widgets, key)
		else:
			counter+=1
			print(counter, key)
	print('-'*66)
	print('Total Scope Keys   = ', counter)
	print('Total Widgets Keys = ', widgets)
	print('='*66)


	# for key, item in scope.trials.items():
	# 	print( key, '   :    ', item)





# =======================================
# Testing code - show whats in scope
# =======================================



# def terminal_heading(heading):
# 	print('')
# 	print('='*70)
# 	print(heading.upper(), '   ( level_1 )')
# 	print('='*70)


# def level_2_details(level_1, level_2):
# 	# print('')
# 	print('-'*40)
# 	print(level_1, '/', level_2, ' ( level 2 )', )
# 	print('-'*40)
# 	if level_2 in st.session_state[level_1]:
# 		for key in st.session_state[level_1][level_2]:
# 			print(level_2 , ' - ', key)

# def level_3_details(level_1, level_2, level_3):
# 	print('-'*50)
# 	print(level_1, '/', level_2, '/', level_3, ' ( level 3 )')
# 	print('-'*50)
# 	if level_2 in st.session_state[level_1]:
# 		if level_3 in st.session_state[level_1][level_2]:
# 			# print(st.session_state[level_1][level_2])
# 			for key in st.session_state[level_1][level_2][level_3]:
# 				print(level_3 , ' - ', key)
# 				# print(type(st.session_state[level_1][level_2][level_3]))


# if 'initial_load' in st.session_state:
# 	print('')
# 	terminal_heading('All keys in st.session_state')
# 	for key in sorted(st.session_state):print(key)


# if 'initial_load' in st.session_state:
# 	scope = st.session_state
# 	# scope.users['user_list'] = [rob, Fliss]
# 	# json file has structure
# 	for key in sorted(scope.users):print(key)
# 	# for key in sorted(scope.users['json']['Rob']):print(key)


