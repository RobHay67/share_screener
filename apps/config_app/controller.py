import streamlit as st

# Config (scope)
from apps.config_app.app import view_app
from apps.config_app.dropdowns import view_dropdowns
from apps.config_app.trials import view_trials_config
from apps.config_app.charts import view_charts_config
# Files
from apps.config_app.files import view_folders
# Data
from apps.config_app.download import view_download



def render_selected_scope_page(scope):

	scope_page = {
			'application'			:view_app,
			'dropdowns'				:view_dropdowns,
			'trials'				:view_trials_config,
			'charts'				:view_charts_config,
			'view_folders'			:view_folders,
			'view_download'			:view_download,
			}

	scope_page[scope.apps['button_for_scope']](scope)

	scope.apps['button_for_scope'] =  None



def set_st_button(scope:dict, button:str):
	scope.apps['button_for_scope'] = button


def render_scope_categories(scope):
	st.subheader('Configuration Setting')
	st.write('Current Page = ', scope.apps['display_app'])
	# col1,col2,col3,col4,col5,col6 = st.columns([2,2,2,2,2,2])
	col1,col2,col3,col4,col5,col6 = st.columns(6)
	
	with col1: 
		st.button('Application', use_container_width=True, on_click=set_st_button, args=(scope, 'application', ))
	with col2: 
		st.button('Dropdowns', use_container_width=True, on_click=set_st_button, args=(scope, 'dropdowns', ))
	with col3: 
		st.button('Trials  (column adders)', use_container_width=True, on_click=set_st_button, args=(scope, 'trials', ))
	with col4: 
		st.button('Charts (column adders)', use_container_width=True, on_click=set_st_button, args=(scope, 'charts', ))
	with col5: 
		st.button('Folders and Paths', use_container_width=True, on_click=set_st_button, args=(scope, 'view_folders', ))

	with col6: 
		st.button('Download Dictionaries', use_container_width=True, on_click=set_st_button, args=(scope, 'view_download', ))

	st.markdown("""---""")

	if scope.apps['button_for_scope'] != None:
		
		render_selected_scope_page(scope)

