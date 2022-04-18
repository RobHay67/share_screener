import streamlit as st

from pages.data.status import set_page_renew_status


def edit_trend_direction(scope, config_name, expander ):

	widget_key = 'widget_' + config_name + '_' + expander
	display_name =  '' + ('Direction for ' + scope.config[config_name][expander]['name'] )
	previous_selection = scope.config[config_name][expander]['add_columns']['trend']
	pos_for_previous = scope.config['tests']['trends'].index(previous_selection)	
	

	st.selectbox ( 
					label		=display_name, 
					options		=scope.config['tests']['trends'],
					index		=pos_for_previous, 
					on_change	=on_change_trend_selection,
					args		=(scope, config_name, expander, widget_key, ),
					key			=widget_key,
					) 


def on_change_trend_selection(scope:dict, config_name:str, expander:str, widget_key:str):

	changed_value = scope[widget_key]

	# store the selection
	scope.config[config_name][expander]['add_columns']['trend'] = changed_value	

	# update the page data renew status
	set_page_renew_status(scope, expanders=expander, caller='edit_trend_direction')