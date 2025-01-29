import streamlit as st
from app.scope.views.buttons.button_choose_scope import scope_button
from app.scope.views.buttons.button_data_type import data_type_button
from app.scope.views.buttons.show_config_value import show_config_single_value, show_config_values
from app.scope.views.buttons.dropdown_choose_scope import scope_dropdown


def show_config_tickers_schema(scope):
	scope_button(scope, "Ticker Schema", scope.ticker_schema, make_red=True, suffix_only=False)
	scope_button(scope, "scope.ticker_schema", scope.ticker_schema, make_red=False, suffix_only=False)

	col1,col2,col3,col4,col5 = st.columns([1,1,1,1,5])
	with col1:scope_button(scope, "scope.ticker_schema['schema']", scope.ticker_schema['schema'])
	with col2:scope_button(scope, "scope.ticker_schema['usecols']", scope.ticker_schema['usecols'])
	with col3:scope_button(scope, "scope.ticker_schema['dtypes']", scope.ticker_schema['dtypes'])
	with col4:scope_button(scope, "scope.ticker_schema['dates']", scope.ticker_schema['dates'])
	with col5:scope_button(scope, "scope.ticker_schema['missing'] tickers", scope.ticker_schema['missing'])

	col1,col2,col3,col4,col5 = st.columns([4,2,1,1,1])
	with col2:scope_button(scope, "scope.ticker_schema['missing']['errors']", scope.ticker_schema['missing']['errors'])
	with col3:scope_button(scope, "scope.ticker_schema['missing']['local']", scope.ticker_schema['missing']['local'])
	with col4:scope_button(scope, "scope.ticker_schema['missing']['cloud']", scope.ticker_schema['missing']['cloud'])
	with col5:scope_button(scope, "scope.ticker_schema['missing']['list']", scope.ticker_schema['missing']['list'])

	col1,col2,col3 = st.columns([4,2,3])
	with col2:scope_button(scope,"['errors']['ticker'] i.e. CBA.AX", scope.ticker_schema['missing']['errors'], make_red=False, suffix_only=False)
	
	missing_ticker_list = list(scope.ticker_schema['missing']['errors'].keys())	
	with col2:ticker = scope_dropdown(scope, 'ticker', missing_ticker_list)

	col1,col2,col3,col4 = st.columns([4,1,1,3])
	if len(missing_ticker_list)>0:
		
		with col2:scope_button(scope, "scope.ticker_schema['missing']['errors']["+ticker+"]['load']", scope.ticker_schema['missing']['errors'][ticker]['load'])
		with col3:scope_button(scope, "scope.ticker_schema['missing']['errors']["+ticker+"]['yf']", scope.ticker_schema['missing']['errors'][ticker]['yf'])
	else:
		with col2:scope_button(scope, "scope.ticker_schema['missing']['errors']['ticker']['load']", scope.ticker_schema['missing']['errors'])
		with col3:scope_button(scope, "scope.ticker_schema['missing']['errors']['ticker']['yf']", scope.ticker_schema['missing']['errors'])

	st.divider()
	if scope.display['config_key'] != None:
		show_config_values(scope)




	














