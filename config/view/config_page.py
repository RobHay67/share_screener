# import pandas as pd
import streamlit as st

from pages.view.pages import view_pages

from charts.view.config_primary_charts import view_primary
from charts.view.config_secondary_charts import view_secondary

from strategies.config import view_strategy
from tickers.config import view_download

from results.config import view_results

from config.view.app import view_app
from files.config import view_folders

from index.download import download_ticker_index_data
from index.view.index import view_index
from index.view.industries import view_industries
from tickers.view.dataframes import view_ticker_data_files
from pages.view.dataframes import view_screener_dfs
from pages.view.dataframes import view_chart_dfs


from config.model.set_scope_button import set_st_button

def render_selected_scope_page(scope):

	scope_page = {
			# Column 1
			'view_pages'			:view_pages,
			'view_primary'			:view_primary,
			'view_secondary'		:view_secondary,
			
			'view_strategy'			:view_strategy,
			# Column 2
			'view_download'			:view_download,
			'view_results'			:view_results,
			# Column 3
			'view_app'				:view_app,
			'view_folders'			:view_folders,
			# Column 4
			'import_tickers'		:download_ticker_index_data,
			'view_ticker_index'		:view_index,
			'view_industries'		:view_industries,
			# Column 5			
			'view_ticker_files'		:view_ticker_data_files,
			'view_analysis_dfs'		:view_screener_dfs,
			'view_chart_dfs'		:view_chart_dfs,
			
			}

	scope_page[st.session_state.st_button](scope)

	scope.st_button =  None




def view_scope(scope):
	st.header('Configuration Setting')

	col1,col2,col3,col4,col5,col6 = st.columns([2,2,2,2,2,2])

	with col1: st.subheader('Session Settings')
	with col1: st.button('Page(s)', on_click=set_st_button, args=('view_pages', ))
	with col1: st.button('Download', on_click=set_st_button, args=('view_download', ))
	with col1: st.button('Strategy', on_click=set_st_button, args=('view_strategy', ))
	with col1: st.button('Results', on_click=set_st_button, args=('view_results', ))

	with col2: st.subheader('Chart Settings')
	with col2: st.button('User Primary Charts', on_click=set_st_button, args=('view_primary', ))
	with col2: st.button('User Secondary Charts', on_click=set_st_button, args=('view_secondary', ))
	
	with col3: st.subheader('System') # DONE
	with col3: st.button('Application', on_click=set_st_button, args=('view_app', ))
	with col3: st.button('Folders', on_click=set_st_button, args=('view_folders', ))
	
	with col4: st.subheader('Ticker Index') # DONE
	with col4: st.button('Import New Tickers', on_click=set_st_button, args=('import_tickers', ))
	with col4: st.button('Ticker Index Report ( ' + str((len(scope.ticker_index))) + ' )', on_click=set_st_button, args=('view_ticker_index', ))
	with col4: st.button('Industry Report', on_click=set_st_button, args=('view_industries', ))

	with col5: st.subheader('Ticker DataFrames') # DONE
	with col5: st.button('Loaded Ticker Data Files ( ' + str(len(scope.ticker_data_files.keys())) + ' )', on_click=set_st_button, args=('view_ticker_files', ))
	with col5: st.button('Analysis Dataframes ( ?? )', on_click=set_st_button, args=('view_analysis_dfs', ))
	with col5: st.button('Charting Dataframes ( ?? )', on_click=set_st_button, args=('view_chart_dfs', ))
	
	st.markdown("""---""")
	if st.session_state.st_button != None:
		render_selected_scope_page(scope)

