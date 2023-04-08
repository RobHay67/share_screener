import streamlit as st

from tickers.download.config import set_yf_period



def download_button(scope):

	# page = scope.display_page

	download_button_msg = 'Download Prior ' + str(int(scope.download['days'])) + ' day'

	if scope.download['days'] > 1: 
		download_button_msg += 's'
		
	button = st.button(
		label=download_button_msg, 
		# help="Press to download the previous X days. If button disabled, select ticker(s)",
		use_container_width=True, 
		)

	return button

	
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

	# update the yf download days
	set_yf_period(scope)

