import streamlit as st





def set_chart_height_primary(scope):

	previous_selection = int(scope.chart_config['primary_height'])
	display_name = 'Total Height of All Charts Combined (default = 500)'
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
	scope.chart_config['primary_height'] = changed_value

	# update the app data renew status
	# Does not require renewal of app data
