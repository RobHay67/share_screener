
import streamlit as st

from pages.data.status import set_page_renew_status
	


def edit_number(scope, config_name, expander, measure ):

	widget_key = 'widget_' + config_name + '_' + expander + '_' + measure
	display_name 	= measure.capitalize() + ' for ' + scope.config[config_name][expander]['name']
	previous_selection = int(scope.config[config_name][expander]['add_columns'][measure])	

	st.number_input( 	
					label		=display_name, 
					min_value	=1,
					step		=1, 
					value		=previous_selection,
					on_change	=on_change_number,
					args		=(scope, config_name, expander, measure, widget_key, ),
					key			=widget_key,
					)  


def on_change_number(scope:dict, config_name:str, expander:str, measure:str, widget_key:str):

	changed_value = scope[widget_key]

	# store the selection
	scope.config[config_name][expander]['add_columns'][measure] != changed_value

	# update the page data renew status
	set_page_renew_status(scope, expanders=expander, caller='on_change_number')
