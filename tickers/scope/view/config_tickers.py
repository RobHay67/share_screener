import streamlit as st
from app.scope.views.buttons.button_choose_scope import scope_button
from app.scope.views.buttons.button_data_type import data_type_button
from app.scope.views.buttons.show_scope_value import show_scope_single_value, show_scope_values
from app.scope.views.buttons.dropdown_choose_scope import scope_dropdown


def show_scope_tickers(scope):
	scope_button(scope, "scope.tickers", scope.tickers, make_red=True, suffix_only=False)
	scope_button(scope, "[ticker] i.e. ANZ.AX", scope.tickers, make_red=False, suffix_only=False)
	
	ticker_list = scope.tickers.keys()
	ticker = scope_dropdown(scope, ticker_list)

	if len(ticker_list)>0:
		col1,col2 = st.columns([1,4])
		with col1:scope_button(scope, "scope.tickers["+ticker+"]['df']", scope.tickers[ticker]['df'])
		with col2:scope_button(scope, "scope.tickers["+ticker+"]['page']", scope.config['page_list'])
		
		# page selector - with default of current page
		page = scope.config['display']
		page_list = scope.config['page_list']
		current_page_position = page_list.index(page)	
		with col2:page = scope_dropdown(scope, page_list, current_page_position )

		col1,col2,col3,col4,col5 = st.columns([1,1,1,1,1])
		with col2:scope_button(scope, "scope.tickers["+ticker+"]["+page+"][df]", scope.tickers[ticker][page]['df'])
		with col3:scope_button(scope, "scope.tickers["+ticker+"]["+page+"][replace_df]", scope.tickers[ticker][page]['replace_df'])
		with col4:scope_button(scope, "scope.tickers["+ticker+"]["+page+"][replace_column]", scope.tickers[ticker][page]['replace_column'])
		with col5:scope_button(scope, "scope.tickers["+ticker+"]["+page+"][schema_group]", scope.tickers[ticker][page]['schema_group'])

		col1,col2,col3,col4,col5 = st.columns([1,1,1,1,1])
		with col4:show_scope_single_value("replace_df", scope.tickers[ticker][page]['replace_df'])
		with col5:show_scope_single_value("schema_group", scope.tickers[ticker][page]['schema_group'])
	else:
		scope_button(scope, "Detailed Config Not Available until tickers loaded", scope.tickers, make_red=True, suffix_only=False)

		col1,col2 = st.columns([1,4])
		with col1:scope_button(scope, "scope.tickers['ticker']['df']", scope.tickers)
		with col2:scope_button(scope, "scope.tickers['ticker]['page']", scope.tickers)

		col1,col2,col3,col4,col5 = st.columns([1,1,1,1,1])
		with col2:scope_button(scope, "scope.tickers['ticker]['page'][df]", scope.tickers)
		with col3:scope_button(scope, "scope.tickers['ticker]['page'][replace_df]", scope.tickers)
		with col4:scope_button(scope, "scope.tickers['ticker]['page'][replace_column]", scope.tickers)
		with col5:scope_button(scope, "scope.tickers['ticker]['page'][schema_group]", scope.tickers)

		col1,col2,col3,col4,col5 = st.columns([1,1,1,1,1])
		with col4:show_scope_single_value("replace_df", scope.tickers)
		with col5:show_scope_single_value("schema_group", scope.tickers)

	st.divider()
	if scope.config['display_scope']['scope_key'] != None:
		show_scope_values(scope)

