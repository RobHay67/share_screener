
import streamlit as st
from app.scope.views.buttons.button_choose_scope import scope_button
from app.scope.views.buttons.show_config_value import show_config_values


def show_config_summary(scope):

	scope_button(scope, "Summary", { }, make_red=True, suffix_only=False)
	scope_button(scope, "scope", { }, make_red=False, suffix_only=False)
	
	col1,col2,col3,col4,col5,col6 = st.columns([1,1,1,1,3,2]) #10
	with col1:scope_button(scope, "scope.config", scope.config)
	with col2:scope_button(scope, "scope.files", scope.files)
	with col3:scope_button(scope, "scope.users", scope.users)
	with col4:scope_button(scope, "scope.ticker_index", scope.ticker_index)
	with col5:scope_button(scope, "scope.tickers", scope.tickers, suffix_only=True)
	with col6:scope_button(scope, "scope.page", scope.page, suffix_only=True)

	# Tickers
	col1,col2,col3,col4,col5,col6 = st.columns([4,1,1,1,1,1])
	with col2:scope_button(scope, "scope.ticker_schema", scope.ticker_schema)
	with col3:scope_button(scope, "scope.yf", scope.yf)
	with col4:scope_button(scope, "scope.verdicts", scope.ticker_schema, make_red=True)
	# # Pages
	with col5:scope_button(scope, "scope.trials", scope.trials)
	with col6:scope_button(scope, "scope.strategy", scope.strategy)


	st.divider()
	if scope.config['display_scope']['scope_key'] != None:
		show_config_values(scope)
