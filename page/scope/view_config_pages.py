import logging
import streamlit as st
from config.scope.buttons.button_choose_scope import scope_button
from config.scope.buttons.button_data_type import data_type_button
from config.scope.buttons.show_config_value import show_config_single_value, show_config_values, show_config_note
from config.scope.buttons.dropdown_choose_scope import scope_dropdown


def show_config_pages(scope):
	logging.info("show_config_pages")
	scope_button(scope, "Pages", scope.page, make_red=True, suffix_only=False)
	scope_button(scope, "scope.page", scope.page, make_red=False, suffix_only=False)

	page = scope.display['page']
	scope_button(scope, "scope.page[page]", scope.page[page], make_red=False, suffix_only=False)
	scope_button(scope, '[page] = '+page, scope.page[page], make_red=False, suffix_only=False)

	col1,col2,col3,col4,col5,col6,col7 = st.columns([1,1,1,1,1,1,1]) #12
	with col1:scope_button(scope, "scope.page["+page+"]['list_loaded_tickers']", scope.page[page]['list_loaded_tickers'])
	with col2:scope_button(scope, "scope.page["+page+"]['list_load_tickers']", scope.page[page]['list_load_tickers'])
	with col3:scope_button(scope, "scope.page["+page+"]['list_selected_tickers']", scope.page[page]['list_selected_tickers'])
	with col4:scope_button(scope, "scope.page["+page+"]['list_page_worklist']", scope.page[page]['list_page_worklist'])
	with col5:scope_button(scope, "scope.page["+page+"]['replace_worklist']", scope.page[page]['replace_worklist'])
	with col6:scope_button(scope, "scope.page["+page+"]['search_results']", scope.page[page]['search_results'])
	
	with col1:show_config_note("list_loaded_tickers", 'list of every ticker ever loaded for this page')
	with col2:show_config_note("list_load_tickers", 'List of Tickers that need to be loaded')
	with col3:show_config_note("list_selected_tickers", 'list of tickers determined by the Selectors')
	with col5:show_config_single_value("replace_worklist", scope.page[page]['replace_worklist'])
	with col6:show_config_note("search_results", 'list of ticker names which match the search string')

	# Show
	col1,col2 = st.columns([3,7])
	with col2:scope_button(scope, "scope.page["+page+"]['show']", scope.page[page]['show'])
	col1,col2,col3,col4,col5,col6,col7,col8 = st.columns([3,1,1,1,1,1,1,1])
	with col2:scope_button(scope, "scope.page["+page+"]['show']['trials']", scope.page[page]['show']['trials'])
	with col3:scope_button(scope, "scope.page["+page+"]['show']['strategy']", scope.page[page]['show']['strategy'])
	with col4:scope_button(scope, "scope.page["+page+"]['show']['charts']", scope.page[page]['show']['charts'])
	with col5:scope_button(scope, "scope.page["+page+"]['show']['overlays']", scope.page[page]['show']['overlays'])
	with col6:scope_button(scope, "scope.page["+page+"]['show']['config']", scope.page[page]['show']['config'])
	with col7:scope_button(scope, "scope.page["+page+"]['show']['active_trial_or_chart']", scope.page[page]['show']['active_trial_or_chart'])
	with col8:scope_button(scope, "scope.page["+page+"]['show']['ticker_file']", scope.page[page]['show']['ticker_file'])
	with col2:show_config_single_value("settings_trials", scope.page[page]['show']['trials'])
	with col3:show_config_single_value("strategy", scope.page[page]['show']['strategy'])
	with col4:show_config_single_value("settings_charts", scope.page[page]['show']['charts'])
	with col5:show_config_single_value("settings_overlay", scope.page[page]['show']['overlays'])
	with col6:show_config_single_value("config_to_show", scope.page[page]['show']['config'])
	with col7:show_config_single_value("active_trial_or_chart", scope.page[page]['show']['active_trial_or_chart'])
	with col8:show_config_single_value("ticker_file", scope.page[page]['show']['ticker_file'])
	# Selectors
	col1,col2 = st.columns([4,3])
	with col1:scope_button(scope, "scope.page["+page+"]['selectors']", scope.page[page]['selectors'], make_red=False, suffix_only=False)
	col1,col2,col3,col4,col5 = st.columns([1,1,1,1,3])
	with col1:scope_button(scope, "scope.page["+page+"]['selectors']['ticker']", scope.page[page]['selectors']['ticker'])
	with col2:scope_button(scope, "scope.page["+page+"]['selectors']['tickers']", scope.page[page]['selectors']['tickers'])
	with col3:scope_button(scope, "scope.page["+page+"]['selectors']['industries']", scope.page[page]['selectors']['industries'])
	with col4:scope_button(scope, "scope.page["+page+"]['selectors']['market']", scope.page[page]['selectors']['market'])
	# with col5:scope_button(scope, "scope.page["+page+"]['selectors']['ticker_worklist']", scope.page[page]['selectors']['ticker_worklist'])
	
	st.divider()
	if scope.display['config_key'] != None:
		show_config_values(scope)

