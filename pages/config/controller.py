import streamlit as st

# Config (scope)
from pages.config.application import render_scope_config
from pages.config.files import view_files
from pages.config.pages import view_page_config
from pages.config.dropdowns import view_dropdowns
from pages.config.ticker_search import view_ticker_search
from pages.config.trials import view_trials_config
from pages.config.charts import view_charts_config
from pages.config.ticker_data import view_ticker_data
from pages.config.missing_tickers import view_missing_tickers
from pages.config.users import view_users
from pages.config.download import view_download
from pages.config.strategies import render_strategies

def render_selected_scope_page(scope):

	scope_page = {
			'application'			:render_scope_config,
			'view_files'			:view_files,
			'page'					:view_page_config,
			'dropdowns'				:view_dropdowns,
			'ticker_search'			:view_ticker_search,
			'trials'				:view_trials_config,
			'charts'				:view_charts_config,
			'view_ticker_data'		:view_ticker_data,
			'view_missing_tickers'	:view_missing_tickers,
			'view_users'			:view_users,
			'view_download'			:view_download,
			'view_strategies'		:render_strategies,
			}

	scope_page[scope.pages['button_for_scope']](scope)



def set_st_button(scope:dict, button:str):
	scope.pages['button_for_scope'] = button


def render_config_page(scope):
	# st.subheader('⚙️ Configuration Setting')
	col1,col2,col3,col4,col5,col6,col7,col8 = st.columns(8)
	
	with col1: 
		st.button('Application', use_container_width=True, on_click=set_st_button, args=(scope, 'application', ))
		st.button('Folders and Paths', use_container_width=True, on_click=set_st_button, args=(scope, 'view_files', ))
	with col2: 
		st.button('Page', use_container_width=True, on_click=set_st_button, args=(scope, 'page', ))
		st.button('Dropdowns', use_container_width=True, on_click=set_st_button, args=(scope, 'dropdowns', ))
		st.button('Ticker Search', use_container_width=True, on_click=set_st_button, args=(scope, 'ticker_search', ))
	with col3: 
		st.button('Trials  (column adders)', use_container_width=True, on_click=set_st_button, args=(scope, 'trials', ))
	with col4: 
		st.button('Charts (column adders)', use_container_width=True, on_click=set_st_button, args=(scope, 'charts', ))
	with col5: 
		st.button('Ticker Data', use_container_width=True, on_click=set_st_button, args=(scope, 'view_ticker_data', ))
		st.button('Missing Tickers', use_container_width=True, on_click=set_st_button, args=(scope, 'view_missing_tickers', ))
	with col6: 
		st.button('Users', use_container_width=True, on_click=set_st_button, args=(scope, 'view_users', ))
	with col7: 
		st.button('Download Info', use_container_width=True, on_click=set_st_button, args=(scope, 'view_download', ))
	with col8: 
		st.button('Strategies (WIP)', use_container_width=True, on_click=set_st_button, args=(scope, 'view_strategies', ))

	
	st.markdown("""---""")

	if scope.pages['button_for_scope'] != None:
		render_selected_scope_page(scope)



