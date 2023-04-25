
import streamlit as st

from tickers.events.edit_column_adder import edit_column_adder_event

def edit_ohlc(scope, config_group, config_key ):
	
	widget_key = 'widget_' + config_group + '_' + config_key
	display_name =  ('Column for ' +  scope[config_group]['config'][config_key]['short_name'])
	previous_selection = scope[config_group]['config'][config_key]['add_columns']['column']
	pos_for_previous = scope.pages['dropdowns']['price_columns'].index(previous_selection)	

	st.selectbox ( 
					label		=display_name, 
					options		=scope.pages['dropdowns']['price_columns'],
					index		=pos_for_previous, 
					on_change	=on_change_ohlc,
					args		=(scope, config_group, config_key, widget_key, ),
					key			=widget_key,
					) 


def on_change_ohlc(scope:dict, config_group:str, config_key:str, widget_key:str):

	changed_value = scope[widget_key]

	# store the selection
	scope[config_group]['config'][config_key]['add_columns']['column'] = changed_value	

	# update the page data renew status
	edit_column_adder_event(scope, config_key)



def edit_ohlc_active_col(scope, config_group, config_key, col_name):
	
	active_ohlc_cols = scope[config_group]['config'][config_key]['active_columns']
	previous_selection = True if col_name in active_ohlc_cols else False

	widget_key = 'widget_active_col_' + config_group + '_' + config_key + '_' + col_name

	st.checkbox( 
				label		=col_name.title(), 
				value		=previous_selection,
				on_change	=on_change_active_column_status,
				args		=(scope, config_group, config_key, col_name, widget_key, ),
				key			=widget_key,
				)


def on_change_active_column_status(scope, config_group, config_key, col_name, widget_key):

	changed_value = scope[widget_key]

	active_columns = scope[config_group]['config'][config_key]['active_columns']

	if changed_value == True and col_name not in active_columns:
		active_columns.append(col_name)
	else:
		active_columns.remove(col_name)








