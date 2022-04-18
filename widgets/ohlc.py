
import streamlit as st

from pages.data.status import set_page_renew_status


def edit_ohlc(scope, config_name, expander ):
	
	widget_key = 'widget_' + config_name + '_' + expander
	display_name =  ('Column for ' +  scope.config[config_name][expander]['name'])
	previous_selection = scope.config[config_name][expander]['add_columns']['column']
	pos_for_previous = scope.config['dropdowns']['price_columns'].index(previous_selection)	

	st.selectbox ( 
					label		=display_name, 
					options		=scope.config['dropdowns']['price_columns'],
					index		=pos_for_previous, 
					on_change	=on_change_ohlc,
					args		=(scope, config_name, expander, widget_key, ),
					key			=widget_key,
					) 


def on_change_ohlc(scope:dict, config_name:str, expander:str, widget_key:str):

	changed_value = scope[widget_key]

	# store the selection
	scope.config[config_name][expander]['add_columns']['column'] = changed_value	

	# update the page data renew status
	set_page_renew_status(scope, expanders=expander, caller='edit_ohlc')