import streamlit as st

from app.views.header.controller import show_page_header


# Page Configuration
scope = st.session_state
page = 'testing'
scope.config['display'] = page

show_page_header(scope)




# st.subheader (':blue[Need some code to test access the namespace]')

# print(scope.config['project_description'])
# print(type(scope))
# # print(scope.config.project_description)



st.subheader(':green[Come code to iterate through every key in the scope and output the key]')
# # print_tree_level(scope.config)


# def pretty_print_dict(d, indent=0):
# 	exception_dict = {
# 		'ticker_search':'{ dict of tickers - too many to display}'
# 		}
# 	for key, value in d.items():
# 		if key in exception_dict.keys():
# 			# print(key, 'contains too many records to go down a level')
# 			print('\t' * indent + str(key)+' : '+exception_dict[key])
# 		else:
# 			print('\t' * indent + str(key))
# 			if isinstance(value, dict):
# 				pretty_print_dict(value, indent+1)


# pretty_print_dict(scope)













