import streamlit as st
from config.views.button_choose_scope import scope_button
from config.views.show_scope_value import show_scope_single_value, show_scope_values




def show_scope_page(scope):

	st.divider()
	scope_button(scope, "scope.page", scope.page, make_red=True, suffix_only=False)

	page = scope.config['display']
	scope_button(scope, "scope.page[page]", scope.page[page], make_red=False, suffix_only=False)
	scope_button(scope, '[page] = '+page, scope.page[page], make_red=False, suffix_only=False)

	# 12 and then 5 for the selectors
	col1,col2,col3,col4,col5 = st.columns([1,1,1,1,7])
	with col1:scope_button(scope, "scope.page["+page+"]['loaded_ticker_list']", scope.page[page]['loaded_ticker_list'])
	with col2:scope_button(scope, "scope.page["+page+"]['worklist']", scope.page[page]['worklist'])
	with col3:scope_button(scope, "scope.page["+page+"]['worklist_long_desc']", scope.page[page]['worklist_long_desc'])
	with col4:scope_button(scope, "scope.page["+page+"]['search_results']", scope.page[page]['search_results'])
	with col5:scope_button(scope, "scope.page["+page+"]['render']", scope.page[page]['render'])

	col1,col2,col3,col4,col5,col6,col7,col8 = st.columns([4,1,1,1,1,1,1,1])
	with col2:scope_button(scope, "scope.page["+page+"]['render']['page_config']", scope.page[page]['render']['page_config'])
	with col3:scope_button(scope, "scope.page["+page+"]['render']['chart_settings']", scope.page[page]['render']['chart_settings'])
	with col4:scope_button(scope, "scope.page["+page+"]['render']['overlay_settings']", scope.page[page]['render']['overlay_settings'])
	with col5:scope_button(scope, "scope.page["+page+"]['render']['trial_settings']", scope.page[page]['render']['trial_settings'])
	with col6:scope_button(scope, "scope.page["+page+"]['render']['ticker_file']", scope.page[page]['render']['ticker_file'])
	with col7:scope_button(scope, "scope.page["+page+"]['render']['ticker_config']", scope.page[page]['render']['ticker_config'])
	with col8:scope_button(scope, "scope.page["+page+"]['render']['strategy']", scope.page[page]['render']['strategy'])

	col1,col2,col3,col4,col5,col6,col7,col8 = st.columns([4,1,1,1,1,1,1,1])
	with col2:show_scope_single_value("page_config", scope.page[page]['render']['page_config'])
	with col3:show_scope_single_value("chart_settings", scope.page[page]['render']['chart_settings'])
	with col4:show_scope_single_value("overlay_settings", scope.page[page]['render']['overlay_settings'])
	with col5:show_scope_single_value("trial_settings", scope.page[page]['render']['trial_settings'])
	with col6:show_scope_single_value("ticker_file", scope.page[page]['render']['ticker_file'])
	with col7:show_scope_single_value("ticker_config", scope.page[page]['render']['ticker_config'])
	with col8:show_scope_single_value("strategy", scope.page[page]['render']['strategy'])

	col1,col2 = st.columns([5,6])
	with col1:scope_button(scope, "scope.page["+page+"]['selectors']", scope.page[page]['selectors'], make_red=False, suffix_only=False)
	col1,col2,col3,col4,col5,col6 = st.columns([1,1,1,1,1,6])
	with col1:scope_button(scope, "scope.page["+page+"]['selectors']['ticker']", scope.page[page]['selectors']['ticker'])
	with col2:scope_button(scope, "scope.page["+page+"]['selectors']['tickers']", scope.page[page]['selectors']['tickers'])
	with col3:scope_button(scope, "scope.page["+page+"]['selectors']['industries']", scope.page[page]['selectors']['industries'])
	with col4:scope_button(scope, "scope.page["+page+"]['selectors']['market']", scope.page[page]['selectors']['market'])
	with col5:scope_button(scope, "scope.page["+page+"]['selectors']['ticker_worklist']", scope.page[page]['selectors']['ticker_worklist'])
	
	# st.divider()
	if scope.config['display_scope']['scope_key'] != None:
		show_scope_values(scope)

