
import logging
import streamlit as st

from add_cols.events.edit_column_adder import edit_column_adder_event


def edit_ohlc(scope, schema_group, schema_key ):
	logging.debug("edit_ohlc")
	widget_key = 'widget_' + schema_group + '_' + schema_key
	display_name =  ('Column for ' +  scope[schema_group]['user_config'][schema_key]['short_name'])
	previous_selection = scope[schema_group]['user_config'][schema_key]['function']['column']
	pos_for_previous = scope.config['dropdowns']['price_columns'].index(previous_selection)	

	st.selectbox ( 
					label		=display_name, 
					options		=scope.config['dropdowns']['price_columns'],
					index		=pos_for_previous, 
					on_change	=changed_ohlc,
					args		=(scope, schema_group, schema_key, widget_key, ),
					key			=widget_key,
					) 


def changed_ohlc(scope:dict, schema_group:str, schema_key:str, widget_key:str):
	logging.warning("changed_ohlc")
	changed_value = scope[widget_key]

	# store the selection
	scope[schema_group]['user_config'][schema_key]['function']['column'] = changed_value	

	# update the page data renew status
	edit_column_adder_event(scope, schema_key)



def edit_ohlc_active_col(scope, schema_group, schema_key, col_name):
	logging.warning("edit_ohlc_active_col")
	active_ohlc_cols = scope[schema_group]['user_config'][schema_key]['active_columns']
	previous_selection = True if col_name in active_ohlc_cols else False

	widget_key = 'widget_active_col_' + schema_group + '_' + schema_key + '_' + col_name

	st.checkbox( 
				label		=col_name.title(), 
				value		=previous_selection,
				on_change	=changed_active_column_status,
				args		=(scope, schema_group, schema_key, col_name, widget_key, ),
				key			=widget_key,
				)


def changed_active_column_status(scope, schema_group, schema_key, col_name, widget_key):
	logging.warning("changed_active_column_status")
	changed_value = scope[widget_key]

	active_columns = scope[schema_group]['user_config'][schema_key]['active_columns']

	if changed_value == True and col_name not in active_columns:
		active_columns.append(col_name)
	else:
		active_columns.remove(col_name)








