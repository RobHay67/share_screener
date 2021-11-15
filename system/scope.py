import pandas as pd
import streamlit as st



from system.app import scope_app, view_app
from system.pages import scope_pages, view_pages
from system.download import scope_download, view_download, view_download_days
from system.results import scope_results, view_results

from system.project import scope_project, view_project
from system.folders import scope_folders, view_folders

from system.analysis import scope_analysis, view_analysis, view_analysis_row_limit
from system.strategy import scope_strategy, view_strategy
from system.chart import scope_chart, view_chart

from index.download import new_tickers_from_web
from system.ticker_index import scope_index, view_index
from system.industries import view_industries

from system.ticker_files import scope_ticker_files, view_all_loaded_ticker_files


def set_scope(scope, project_description):
	if 'initial_load' not in scope:					# set the initial load state - keep this to a minimum
		scope.initial_load = True
		scope_project(scope, project_description)
		scope_app(scope)						# This contains all the application settings
		scope_pages(scope)							# This contains all the page Specific settings
		scope_folders(scope)						# Required before we can attempt to load the data
		scope_download(scope)
		scope_analysis(scope)
		scope_strategy(scope)
		scope_chart(scope)
		scope_results(scope)
		scope_ticker_files(scope)

	if scope.initial_load:
		scope_index(scope)
		st.session_state.initial_load = False		# Prevent session_state from re-running during its use


def view_scope(scope):
	st.title('User Setting')
	col1,col2,col3,col4,col5,col6 = st.columns([2,2,2,2,2,2])
	with col1: st.subheader('Download Days')
	with col1: view_download_days(scope)
	with col2: st.subheader('Analysis Row Limit')
	with col2: view_analysis_row_limit(scope)


	st.markdown("""---""")
	st.subheader('Application Setting')

	button_selectors(scope)
	st.markdown("""---""")

	if st.session_state.st_button != None:
		show_settings_page(scope)

		
		
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Components
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def show_settings_page(scope):

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
			'show_analysis'			:view_analysis,
			'show_strategy'			:view_strategy,
			'show_charting'			:view_chart,
			# Column 4
			'import_tickers'		:new_tickers_from_web,
			'show_ticker_index'		:view_index,
			'show_industries'		:view_industries,
			# Column 5			
			'show_ticker_files'		:view_all_loaded_ticker_files,
			}

	scope_page[st.session_state.st_button](scope)

	scope.st_button =  None

def button_selectors(scope):
	col1,col2,col3,col4,col5,col6 = st.columns([2,2,2,2,2,2])

	with col1: st.subheader('Application')
	with col1: st.button('Global', on_click=set_st_button, args=('show_app', ))
	with col1: st.button('Page Selections', on_click=set_st_button, args=('show_pages', ))
	with col1: st.button('Download', on_click=set_st_button, args=('show_download', ))
	with col1: st.button('Results', on_click=set_st_button, args=('show_results', ))
	
	with col2: st.subheader('System') # DONE
	with col2: st.button('Project', on_click=set_st_button, args=('show_project', ))
	with col2: st.button('Folders', on_click=set_st_button, args=('show_folders', ))
		
	with col3: st.subheader('Analysis') # DONE
	with col3: st.button('Analysis', on_click=set_st_button, args=('show_analysis', ))
	with col3: st.button('Strategy', on_click=set_st_button, args=('show_strategy', ))
	with col3: st.button('Charting', on_click=set_st_button, args=('show_charting', ))	
	
	with col4: st.subheader('Ticker Index') # DONE
	with col4: st.button('Import New Tickers', on_click=set_st_button, args=('import_tickers', ))
	with col4: st.button('Ticker Index Report ( ' + str((len(scope.ticker_index))) + ' )', on_click=set_st_button, args=('show_ticker_index', ))
	with col4: st.button('Industry Report', on_click=set_st_button, args=('show_industries', ))

	with col5: st.subheader('Ticker Files') # DONE
	with col5: st.button('Share Data Files ( ' + str(len(scope.ticker_data_files.keys())) + ' )', on_click=set_st_button, args=('show_ticker_files', ))
	
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def set_st_button(button:str):
	# print( 'Selected Button > ', button)
	st.session_state.st_button = button



