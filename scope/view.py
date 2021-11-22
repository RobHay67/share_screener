# import pandas as pd
import streamlit as st

from scope.user.view import view_user
from charts.views.primary import view_primary
from charts.views.secondary import view_secondary
from scope.pages.view import view_pages
from scope.strategy.view import view_strategy

from scope.download.view import view_download
from scope.results.view import view_results

from scope.project.view import view_project
from scope.app.view import view_app
from scope.folders.view import view_folders

# from index.download.controller import download_new_ticker_data
from index.download.controller import download_new_ticker_data
from index.view import view_index, view_industries
from ticker.views.all_tickers import view_all_loaded_ticker_files


def render_selected_scope_page(scope):

	scope_page = {
			# Column 1
			'view_user'				:view_user,
			'view_primary'			:view_primary,
			'view_secondary'		:view_secondary,
			'view_pages'			:view_pages,
			'view_strategy'			:view_strategy,
			# Column 2
			'view_download'			:view_download,
			'view_results'			:view_results,
			# Column 3
			'view_project'			:view_project,
			'view_app'				:view_app,
			'view_folders'			:view_folders,
			# Column 4
			'import_tickers'		:download_new_ticker_data,
			'view_ticker_index'		:view_index,
			'view_industries'		:view_industries,
			# Column 5			
			'view_ticker_files'		:view_all_loaded_ticker_files,
			# 'view_analysis'			:view_analysis,
			
			}

	scope_page[st.session_state.st_button](scope)

	scope.st_button =  None




def view_scope(scope):
	st.header('Application Setting')
	# button_selectors(scope)

	col1,col2,col3,col4,col5,col6 = st.columns([2,2,2,2,2,2])

	with col1: st.subheader('User Selections')
	with col1: st.button('User Defaults', on_click=set_st_button, args=('view_user', ))
	with col1: st.button('User Primary Charts', on_click=set_st_button, args=('view_primary', ))
	with col1: st.button('User Secondary Charts', on_click=set_st_button, args=('view_secondary', ))
	with col1: st.button('Page Selections', on_click=set_st_button, args=('view_pages', ))
	with col1: st.button('Strategy', on_click=set_st_button, args=('view_strategy', ))

	with col2: st.subheader('Application')
	with col2: st.button('Download', on_click=set_st_button, args=('view_download', ))
	with col2: st.button('Results', on_click=set_st_button, args=('view_results', ))
	
	with col3: st.subheader('System') # DONE
	with col3: st.button('Project', on_click=set_st_button, args=('view_project', ))
	with col3: st.button('Global', on_click=set_st_button, args=('view_app', ))
	with col3: st.button('Folders', on_click=set_st_button, args=('view_folders', ))
	
	with col4: st.subheader('Ticker Index') # DONE
	with col4: st.button('Import New Tickers', on_click=set_st_button, args=('import_tickers', ))
	with col4: st.button('Ticker Index Report ( ' + str((len(scope.ticker_index))) + ' )', on_click=set_st_button, args=('view_ticker_index', ))
	with col4: st.button('Industry Report', on_click=set_st_button, args=('view_industries', ))

	with col5: st.subheader('Ticker Files') # DONE
	with col5: st.button('Share Data Files ( ' + str(len(scope.ticker_data_files.keys())) + ' )', on_click=set_st_button, args=('view_ticker_files', ))
	
	st.markdown("""---""")
	if st.session_state.st_button != None:
		render_selected_scope_page(scope)

		
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def set_st_button(button:str):
	# print( 'Selected Button > ', button)
	st.session_state.st_button = button

