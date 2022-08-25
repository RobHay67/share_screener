import streamlit as st


def download_button(scope):

	# Note - this has been moved to the sidebar to imporve readibility of the limited screen realestate


	# download_button_msg = 'Download most recent ' + str(int(scope.download['days'])) + ' day'
	download_button_msg = 'Download Prior ' + str(int(scope.download['days'])) + ' day'

	if scope.download['days'] > 1: 
		download_button_msg += 's'

	return st.button(download_button_msg)

	
def edit_download_days(scope):

	previous_selection = int(scope.download['days'])
	display_name = 'Days to Download (recent)'
	widget_key = 'widget_download_days'

	st.sidebar.number_input( 	
							label		=display_name, 
							min_value	=7, 
							value		=previous_selection,
							on_change	=on_change_download_days,
							args		=(scope, widget_key, ),
							key			=widget_key,
							)  


def on_change_download_days(scope:dict, widget_key:str):

	changed_value = scope[widget_key]

	# store the selection
	scope.download['days'] = changed_value
