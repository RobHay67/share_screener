import streamlit as st





def set_chart_height_primary(scope):

	previous_selection = int(scope.config['charts']['primary_height'])
	display_name = 'Primary Chart Height'
	widget_key = 'widget_chart_height'

	st.number_input( 	
					label		=display_name, 
					min_value	=0, 
					value		=previous_selection,
					on_change	=on_change_chart_height,
					args		=(scope, widget_key, ),
					key			=widget_key,
					)  


def on_change_chart_height(scope:dict, widget_key:str):

	changed_value = scope[widget_key]

	# store the selection
	scope.config['charts']['primary_height'] = changed_value

	# update the page data renew status
	# Does not require renewal of page data
