import pandas as pd
import streamlit as st





from system.session import scope_session, render_session
from system.pages import scope_pages, render_pages
from system.session import render_download
from system.results import scope_results, render_results

from system.project import scope_project, render_project
from system.folders import scope_folders, render_folders

from system.strategy import scope_strategy, render_strategy
from system.chart import scope_chart, render_chart

from index.download import new_tickers_from_web
# from index.ticker_index import ticker_index_report
from index.industries import industry_report

from ticker.files import ticker_files_report



from system.dataframes import scope_dataframes, render_ticker_index



# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Welcome Page # TODO - this should be a page or the system variables page - nice i like this idea
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def welcome_page(scope):
	st.title(scope.project_description)
	st.success('Loaded and Ready for Analysis')




# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Scope Variables
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def set_scope(scope, project_description):
	if 'initial_load' not in scope:					# set the initial load state - keep this to a minimum
		scope.initial_load = True
		scope_project(scope, project_description)
		scope_session(scope)						# This contains all the application settings
		scope_pages(scope)							# This contains all the page Specific settings
		scope_folders(scope)						# Required before we can attempt to load the data
		scope_strategy(scope)
		scope_chart(scope)
		scope_results(scope)

	if scope.initial_load:
		scope_dataframes(scope)
		st.session_state.initial_load = False		# Prevent session_state from re-running during its use

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Render Scope Variables (by Group)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def scope_page(scope):
	st.title('Application Parameters')

	button_selectors(scope)

	if st.session_state.st_button != None:
		scope_page = {
			# Column 1

			# Column 2
			'show_session'			:render_session,
			'show_pages'			:render_pages,
			'show_results'			:render_results,
			'show_download'			:render_download,
			# Column 3
			'show_project'			:render_project,
			'show_folders'			:render_folders,

			# Column 4
			'show_strategy'			:render_strategy,
			'show_charting'			:render_chart,
			
			# Column 5
			'import_tickers'		:new_tickers_from_web,
			'show_ticker_index'		:render_ticker_index,
			'show_industries'		:industry_report,

			# Column 6			
			'show_ticker_files'		:ticker_files_report,
			

			}

		scope_page[st.session_state.st_button](scope)
		
	scope.st_button =  None



		
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Components
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def button_selectors(scope):
	col1,col2,col3,col4,col5,col6,col7 = st.columns([2,2,2,2,2,2,2])

	with col1: st.subheader('Settings')


	with col2: st.subheader('Session')
	with col2: st.button('Session', on_click=set_st_button, args=('show_session', ))
	with col2: st.button('Page Selections', on_click=set_st_button, args=('show_pages', ))
	with col2: st.button('Download', on_click=set_st_button, args=('show_download', ))
	with col2: st.button('Results', on_click=set_st_button, args=('show_results', ))
	
	with col3: st.subheader('System') # DONE
	with col3: st.button('Project', on_click=set_st_button, args=('show_project', ))
	with col3: st.button('Folders', on_click=set_st_button, args=('show_folders', ))
		
	with col4: st.subheader('Analysis') # DONE
	with col4: st.button('Strategy', on_click=set_st_button, args=('show_strategy', ))
	with col4: st.button('Charting', on_click=set_st_button, args=('show_charting', ))	
	
	with col5: st.subheader('Ticker Index') # DONE
	with col5: st.button('Import New Tickers', on_click=set_st_button, args=('import_tickers', ))
	with col5: st.button('Ticker Index Report ( ' + str((len(scope.ticker_index))) + ' )', on_click=set_st_button, args=('show_ticker_index', ))
	with col5: st.button('Industry Report', on_click=set_st_button, args=('show_industries', ))

	with col6: st.subheader('Ticker Files') # DONE
	with col6: st.button('Share Data Files ( ' + str(len(scope.ticker_data_files.keys())) + ' )', on_click=set_st_button, args=('show_ticker_files', ))
	
	


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def set_st_button(button:str):
	# print( 'Selected Button > ', button)
	st.session_state.st_button = button



