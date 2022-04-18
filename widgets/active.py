
import streamlit as st

from pages.data.status import set_page_renew_status




def edit_active(scope, config_name, expander ):

	widget_key = 'widget_' + config_name + '_' + expander
	display_name =  '' + scope.config[config_name][expander]['name']
	previous_selection = scope.config[config_name][expander]['active']
	

	st.checkbox( 
				label		=display_name, 
				value		=previous_selection,
				on_change	=on_change_active_status,
				args		=(scope, config_name, expander, widget_key, ),
				key			=widget_key,
				)



def on_change_active_status(scope:dict, config_name:str, expander:str, widget_key:str):

	changed_value = scope[widget_key]

	# store the selection
	scope.config[config_name][expander]['active'] = changed_value

	# update the page data renew status
	set_page_renew_status(scope, expanders=expander, caller='on_change_active_status')