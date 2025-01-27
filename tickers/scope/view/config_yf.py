import streamlit as st
from app.scope.views.buttons.button_choose_scope import scope_button
from app.scope.views.buttons.button_data_type import data_type_button
from app.scope.views.buttons.show_config_value import show_config_single_value, show_config_values
from app.scope.views.buttons.dropdown_choose_scope import scope_dropdown


def show_config_yf(scope):

	scope_button(scope, "Y Finance", scope.users, make_red=True, suffix_only=False)
	scope_button(scope, "scope.yf", scope.users, make_red=False, suffix_only=False)

	col1,col2,col3,col4,col5,col6,col7,col8 = st.columns([1,2,1,1,1,1,1,1])
	with col1:scope_button(scope, "scope.yf['periods']", scope.yf['periods'])
	with col2:scope_button(scope, "scope.yf['schemas']", scope.yf['schemas'])
	with col3:scope_button(scope, "scope.yf['batch_ticker_string']", scope.yf['batch_ticker_string'])
	with col4:scope_button(scope, "scope.yf['batch_type']", scope.yf['batch_type'])
	with col5:scope_button(scope, "scope.yf['batch_data']", scope.yf['batch_data'])
	with col6:scope_button(scope, "scope.yf['batch_errors']", scope.yf['batch_errors'])
	with col7:scope_button(scope, "scope.yf['all_data']", scope.yf['all_data'])
	with col8:scope_button(scope, "scope.yf['all_errors']", scope.yf['all_errors'])

	col1,col2,col3,col4 = st.columns([1,1,1,6])
	with col2:scope_button(scope, "scope.yf['schemas']['single_ticker']", scope.yf['schemas']['single_ticker'])
	with col3:scope_button(scope, "scope.yf['schemas']['multiple_tickers']", scope.yf['schemas']['multiple_tickers'])

	
	st.divider()
	if scope.config['display_scope']['scope_key'] != None:
		show_config_values(scope)
