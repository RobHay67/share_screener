import streamlit as st

# Config (scope)
from apps.config.config import view_app
from apps.config.dropdowns import view_dropdowns
from apps.config.ticker_search import view_ticker_search
from apps.config.trials import view_trials_config
from apps.config.charts import view_charts_config
# Files
from apps.config.files import view_files
# Data
from apps.config.download import view_download
from apps.config.users import view_users
from apps.config.missing_tickers import view_missing_tickers
from apps.config.ticker_data import view_ticker_data


def render_selected_scope_page(scope):

	scope_page = {
			'application'			:view_app,
			'dropdowns'				:view_dropdowns,
			'ticker_search'			:view_ticker_search,
			# 'apps'
			'trials'				:view_trials_config,
			'charts'				:view_charts_config,
			'view_files'			:view_files,
			'view_download'			:view_download,
			'view_users'			:view_users,
			'view_missing_tickers'	:view_missing_tickers,
			'view_ticker_data'		:view_ticker_data,
			}

	scope_page[scope.apps['button_for_scope']](scope)

	# scope.apps['button_for_scope'] =  None



def set_st_button(scope:dict, button:str):
	scope.apps['button_for_scope'] = button


def render_lconfig_page(scope):
	st.subheader('⚙️ Configuration Setting')
	col1,col2,col3,col4,col5,col6,col7,col8,col9,col10 = st.columns(10)
	
	with col1: 
		st.button('Application', use_container_width=True, on_click=set_st_button, args=(scope, 'application', ))
	with col2: 
		st.button('Dropdowns', use_container_width=True, on_click=set_st_button, args=(scope, 'dropdowns', ))
	with col3: 
		st.button('Ticker Search', use_container_width=True, on_click=set_st_button, args=(scope, 'ticker_search', ))
	with col4: 
		st.button('Trials  (column adders)', use_container_width=True, on_click=set_st_button, args=(scope, 'trials', ))
	with col5: 
		st.button('Charts (column adders)', use_container_width=True, on_click=set_st_button, args=(scope, 'charts', ))
	with col6: 
		st.button('Folders and Paths', use_container_width=True, on_click=set_st_button, args=(scope, 'view_files', ))
	with col7: 
		st.button('Download Dictionaries', use_container_width=True, on_click=set_st_button, args=(scope, 'view_download', ))
	with col8: 
		st.button('Users', use_container_width=True, on_click=set_st_button, args=(scope, 'view_users', ))
	with col9: 
		st.button('Missing Tickers', use_container_width=True, on_click=set_st_button, args=(scope, 'view_missing_tickers', ))
	with col10: 
		st.button('Ticker Data', use_container_width=True, on_click=set_st_button, args=(scope, 'view_ticker_data', ))
	st.markdown("""---""")

	if scope.apps['button_for_scope'] != None:
		
		render_selected_scope_page(scope)

