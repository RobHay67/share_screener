# import pandas as pd
import streamlit as st

from scope.app.view import view_app
from scope.pages.view import view_pages
from scope.results.view import view_results
from scope.download.view import view_download


from scope.project.view import view_project
from scope.folders.view import view_folders

from scope.user.view import view_user
from scope.strategy.view import view_strategy
from analysis.charts.view import view_chart

from index.download.controller import download_new_ticker_data
from index.view import view_index, view_industries

from ticker.view.all_tickers import view_all_loaded_ticker_files



def render_selected_scope_page(scope):

	scope_page = {
			# Column 1
			'show_app'				:view_app,
			'show_pages'			:view_pages,
			'show_results'			:view_results,
			'show_download'			:view_download,
			# Column 2
			'show_project'			:view_project,
			'show_folders'			:view_folders,
			# Column 3
			# 'show_analysis'			:view_analysis,
			'show_user'				:view_user,
			'show_strategy'			:view_strategy,
			'show_charting'			:view_chart,
			# Column 4
			'import_tickers'		:download_new_ticker_data,
			'show_ticker_index'		:view_index,
			'show_industries'		:view_industries,
			# Column 5			
			'show_ticker_files'		:view_all_loaded_ticker_files,
			}

	scope_page[st.session_state.st_button](scope)

	scope.st_button =  None




def view_scope(scope):
	st.header('Application Setting')
	# button_selectors(scope)

	col1,col2,col3,col4,col5,col6 = st.columns([2,2,2,2,2,2])

	with col1: st.subheader('User Selections')
	with col1: st.button('User Defaults', on_click=set_st_button, args=('show_user', ))
	with col1: st.button('User Charting', on_click=set_st_button, args=('show_charting', ))
	with col1: st.button('Page Selections', on_click=set_st_button, args=('show_pages', ))
	with col1: st.button('Strategy', on_click=set_st_button, args=('show_strategy', ))

	with col2: st.subheader('Application')
	with col2: st.button('Download', on_click=set_st_button, args=('show_download', ))
	with col2: st.button('Results', on_click=set_st_button, args=('show_results', ))
	
	with col3: st.subheader('System') # DONE
	with col3: st.button('Project', on_click=set_st_button, args=('show_project', ))
	with col3: st.button('Global', on_click=set_st_button, args=('show_app', ))
	with col3: st.button('Folders', on_click=set_st_button, args=('show_folders', ))
	
	with col4: st.subheader('Ticker Index') # DONE
	with col4: st.button('Import New Tickers', on_click=set_st_button, args=('import_tickers', ))
	with col4: st.button('Ticker Index Report ( ' + str((len(scope.ticker_index))) + ' )', on_click=set_st_button, args=('show_ticker_index', ))
	with col4: st.button('Industry Report', on_click=set_st_button, args=('show_industries', ))

	with col5: st.subheader('Ticker Files') # DONE
	with col5: st.button('Share Data Files ( ' + str(len(scope.ticker_data_files.keys())) + ' )', on_click=set_st_button, args=('show_ticker_files', ))
	
	st.markdown("""---""")
	if st.session_state.st_button != None:
		render_selected_scope_page(scope)

		
		
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Components
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def set_st_button(button:str):
	# print( 'Selected Button > ', button)
	st.session_state.st_button = button

