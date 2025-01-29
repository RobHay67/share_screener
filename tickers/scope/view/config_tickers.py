import streamlit as st
from app.scope.views.buttons.button_choose_scope import scope_button
from app.scope.views.buttons.button_data_type import data_type_button
from app.scope.views.buttons.show_config_value import show_config_single_value, show_config_values
from app.scope.views.buttons.dropdown_choose_scope import scope_dropdown


def show_config_tickers(scope):
	scope_button(scope, "Tickers (Data)", scope.tickers, make_red=True, suffix_only=False)
	scope_button(scope, "scope.tickers", scope.tickers, make_red=False, suffix_only=False)
	scope_button(scope, "[ticker] i.e. ANZ.AX", scope.tickers, make_red=False, suffix_only=False)
	
	ticker_list = scope.tickers.keys()
	ticker = scope_dropdown(scope, 'Ticker', ticker_list)

	if len(ticker_list)>0:
		col1,col2 = st.columns([1,5])
		with col1:scope_button(scope, "scope.tickers["+ticker+"]['df']", scope.tickers[ticker]['df'])
		with col2:scope_button(scope, "scope.tickers["+ticker+"]['page']", scope.config['page_list'])
		
		# page selector - with default of current page
		page = scope.config['display']
		page_list = scope.config['page_list']
		current_page_position = page_list.index(page)
		with col2:st.caption('Ticker Data for each page is also stored alongside the original ticker data file.')
		with col2:page = scope_dropdown(scope, 'Page', page_list, current_page_position )

		col1,col2,col3,col4,col5,col6 = st.columns([1,1,1,1,1,1])
		with col2:scope_button(scope, "scope.tickers['"+ticker+"']['"+page+"']['replace_df']", scope.tickers[ticker][page]['replace_df'])
		with col3:scope_button(scope, "scope.tickers['"+ticker+"']['"+page+"']['re_run_functions']", scope.tickers[ticker][page]['re_run_functions'])
		with col4:scope_button(scope, "scope.tickers['"+ticker+"']['"+page+"']['schema_group']", scope.tickers[ticker][page]['schema_group'])
		with col5:scope_button(scope, "scope.tickers['"+ticker+"']['"+page+"']['df']", scope.tickers[ticker][page]['df'])
		if page=='verdicts':
			with col6:scope_button(scope, "scope.tickers["+ticker+"]["+page+"][verdicts]", scope.tickers[ticker][page]['verdicts'])

		col1,col2,col3,col4,col5,col6 = st.columns([1,1,1,1,1,1])
		with col2:show_config_single_value("replace_df", scope.tickers[ticker][page]['replace_df'])
		# with col4:show_config_single_value("replace_column", scope.tickers[ticker][page]['re_run_functions'])
		with col4:show_config_single_value("schema_group", scope.tickers[ticker][page]['schema_group'])
	else:
		scope_button(scope, "Detailed Config Not Available until tickers loaded", scope.tickers, make_red=True, suffix_only=False)

		col1,col2 = st.columns([1,4])
		with col1:scope_button(scope, "scope.tickers['ticker']['df']", scope.tickers)
		with col2:scope_button(scope, "scope.tickers['ticker]['page']", scope.tickers)

		col1,col2,col3,col4,col5,col6 = st.columns([1,1,1,1,1,1])
		with col1:scope_button(scope, "scope.tickers['ticker]['page']['df']", scope.tickers)
		with col2:scope_button(scope, "scope.tickers['ticker]['page']['replace_df']", scope.tickers)
		with col3:scope_button(scope, "scope.tickers['ticker]['page']['re_run_functions']", scope.tickers)
		with col4:scope_button(scope, "scope.tickers['ticker]['page']['schema_group']", scope.tickers)
		with col5:scope_button(scope, "scope.tickers['ticker]['page']['df']", scope.tickers)
		if page=='verdicts':
			with col6:scope_button(scope, "scope.tickers['ticker]['page'][verdicts]", scope.tickers)

		col1,col2,col3,col4,col5,col6 = st.columns([1,1,1,1,1,1])
		with col2:show_config_single_value("replace_df", scope.tickers)
		with col3:show_config_single_value("re_run_functions", scope.tickers)
		with col4:show_config_single_value("schema_group", scope.tickers)

	st.divider()
	if scope.display['config_key'] != None:
		show_config_values(scope)

