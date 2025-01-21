import streamlit as st
from app.scope.views.buttons.button_choose_scope import scope_button
from app.scope.views.buttons.button_data_type import data_type_button
from app.scope.views.buttons.show_scope_value import show_scope_single_value, show_scope_values
from app.scope.views.buttons.dropdown_choose_scope import scope_dropdown


def show_scope_tickers(scope):
	scope_button(scope, "scope.tickers", scope.tickers, make_red=True, suffix_only=False)
	scope_button(scope, "[ticker] i.e. ANZ.AX", scope.tickers, make_red=False, suffix_only=False)
	
	ticker = scope_dropdown(scope, scope.tickers.keys())

	col1,col2 = st.columns([1,4])
	with col1:scope_button(scope, "scope.tickers["+ticker+"]['df']", scope.tickers[ticker]['df'])
	with col2:scope_button(scope, "scope.tickers["+ticker+"]['page']", scope.config['page_list'])
	with col2:page = scope_dropdown(scope, scope.config['page_list'])


	col1,col2,col3,col4,col5 = st.columns([1,1,1,1,1])
	with col2:scope_button(scope, "scope.tickers["+ticker+"]["+page+"][df]", scope.tickers[ticker][page]['df'])
	with col3:scope_button(scope, "scope.tickers["+ticker+"]["+page+"][replace_df]", scope.tickers[ticker][page]['replace_df'])
	with col4:scope_button(scope, "scope.tickers["+ticker+"]["+page+"][replace_column]", scope.tickers[ticker][page]['replace_column'])
	with col5:scope_button(scope, "scope.tickers["+ticker+"]["+page+"][schema_group]", scope.tickers[ticker][page]['schema_group'])

	col1,col2,col3,col4,col5 = st.columns([1,1,1,1,1])
	with col4:show_scope_single_value("replace_df", scope.tickers[ticker][page]['replace_df'])
	with col5:show_scope_single_value("schema_group", scope.tickers[ticker][page]['schema_group'])

	st.divider()
	if scope.config['display_scope']['scope_key'] != None:
		show_scope_values(scope)

# def build_ticker_list(scope):
# 	ticker_list = scope.tickers.keys()
# 	return ticker_list