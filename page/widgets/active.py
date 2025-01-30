
import streamlit as st

from add_cols.events.edit_active import edit_active_event



def edit_active(scope, schema_group, schema_key ):

	widget_key = 'widget_active_' + schema_group + '_' + schema_key
	display_name =  '' + scope[schema_group]['user_config'][schema_key]['name']
	previous_selection = scope[schema_group]['user_config'][schema_key]['active']
	add_columns = scope[schema_group]['user_config'][schema_key]['function']
	
	if add_columns != None:
		# add some space above active for charts/trials that have column config
		st.write(' ')
		
	st.checkbox( 
				label		=display_name, 
				value		=previous_selection,
				on_change	=on_change_active_status,
				args		=(scope, schema_group, schema_key, widget_key, ),
				key			=widget_key,
				)


def on_change_active_status(scope:dict, schema_group:str, schema_key:str, widget_key:str):
	changed_value = scope[widget_key]

	# store the selection
	scope[schema_group]['user_config'][schema_key]['active'] = changed_value
	
	# Update the Column Adder Templates
	scope[schema_group]['template_col_adders'][schema_key] = changed_value

	# update the page data renew status
	edit_active_event(scope, schema_group, schema_key, changed_value)


