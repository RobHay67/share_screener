import logging
import streamlit as st
from config.scope.views.buttons.button_choose_scope import scope_button
from config.scope.views.buttons.button_data_type import data_type_button
from config.scope.views.buttons.show_config_value import show_config_single_value, show_config_values, show_config_note
from config.scope.views.buttons.dropdown_choose_scope import scope_dropdown


def show_config_ticker_index(scope):
	logging.debug("show_config_ticker_index")
	scope_button(scope, "Ticker Index", scope.ticker_index, make_red=True, suffix_only=False)
	scope_button(scope, "scope.ticker_index", scope.ticker_index, make_red=False, suffix_only=False)

	col1,col2,col3,col4,col5,col6 = st.columns([1,1,1,1,1,3]) #8
	with col1:scope_button(scope, "scope.ticker_index['schema']", scope.ticker_index['schema'])
	with col2:scope_button(scope, "scope.ticker_index['df']", scope.ticker_index['df'])
	with col3:scope_button(scope, "scope.ticker_index['download_cache']", scope.ticker_index['download_cache'])
	with col4:scope_button(scope, "scope.ticker_index['save_edited_df']", scope.ticker_index['save_edited_df'])
	with col5:scope_button(scope, "scope.ticker_index['editable_df_key']", scope.ticker_index['editable_df_key'])
	with col6:scope_button(scope, "scope.ticker_index['show']", scope.ticker_index['show'])

	col1,col2,col3,col4,col5,col6,col7,col8 = st.columns([1,1,1,1,1,1,1,1]) #8
	with col6:scope_button(scope, "scope.ticker_index['show']['ticker_index']", scope.ticker_index['show']['ticker_index'])
	with col7:scope_button(scope, "scope.ticker_index['show']['industry_report']", scope.ticker_index['show']['industry_report'])
	with col8:scope_button(scope, "scope.ticker_index['show']['editable_df']", scope.ticker_index['show']['editable_df'])
	
	col1,col2,col3,col4,col5,col6,col7,col8 = st.columns([1,1,1,1,1,1,1,1]) #8
	with col4:show_config_single_value("save_edited_df", scope.ticker_index['save_edited_df'])
	with col5:show_config_single_value("editable_df_key", scope.ticker_index['editable_df_key'])
	with col6:show_config_single_value("show_ticker_index", scope.ticker_index['show']['ticker_index'])
	with col7:show_config_single_value("show_industry_report", scope.ticker_index['show']['industry_report'])
	with col8:show_config_single_value("show_editable_df", scope.ticker_index['show']['editable_df'])

	col1,col2 = st.columns([6,2]) #8
	with col1:scope_button(scope, "scope.ticker_index['lists']", scope.ticker_index['lists'])
	col1,col2,col3,col4,col5,col6,col7 = st.columns([1,1,1,1,1,1,2]) #8
	with col1:scope_button(scope, "scope.ticker_index['lists']['csv_dates']", scope.ticker_index['lists']['csv_dates'])
	with col2:scope_button(scope, "scope.ticker_index['lists']['csv_dtypes']", scope.ticker_index['lists']['csv_dtypes'])
	with col3:scope_button(scope, "scope.ticker_index['lists']['data_types']", scope.ticker_index['lists']['data_types'])
	with col4:scope_button(scope, "scope.ticker_index['lists']['default_values']", scope.ticker_index['lists']['default_values'])
	with col5:scope_button(scope, "scope.ticker_index['lists']['editable_columns']", scope.ticker_index['lists']['editable_columns'])
	with col6:scope_button(scope, "scope.ticker_index['lists']['uneditable_columns']", scope.ticker_index['lists']['uneditable_columns'])

	col1,col2,col3,col4,col5,col6,col7 = st.columns([1,1,1,1,1,1,2]) #8
	with col1:show_config_note("csv_dates", 'Utilised by the file loader')
	with col2:show_config_note("csv_dtypes", 'Utilised by the file loader')
	with col3:show_config_note("data_types", 'Used to complete missing fields')
	with col4:show_config_note("default_values", 'Used to complete missing fields')
	with col5:show_config_note("editable_columns", 'These columns can be edited within the application')
	with col6:show_config_note("chart_list", 'Not changes permitted to these columns')

	st.divider()
	if scope.display['config_key'] != None:
		show_config_values(scope)



