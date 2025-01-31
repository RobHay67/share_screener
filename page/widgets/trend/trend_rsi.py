import logging
import streamlit as st

from add_cols.events.edit_column_adder import edit_column_adder_event

from trials.scope.model.schema import trends_for_rsi


def edit_trend_rsi(scope, schema_group, schema_key ):
	logging.debug("edit_trend_rsi")
	widget_key = 'widget_trend_' + schema_group + '_' + schema_key
	display_name = 'Trend'
	previous_selection = scope[schema_group]['user_config'][schema_key]['function']['trend']
	# previous_selection = 'up'
	pos_for_previous = trends_for_rsi.index(previous_selection)	

	st.selectbox ( 
					label		=display_name, 
					options		=trends_for_rsi,
					index		=pos_for_previous, 
					on_change	=on_change_rsi_selection,
					args		=(scope, schema_group, schema_key, widget_key, ),
					key			=widget_key,
					) 


def on_change_rsi_selection(scope:dict, schema_group:str, schema_key:str, widget_key:str):
	logging.debug("on_change_rsi_selection")
	changed_value = scope[widget_key]

	# store the selection
	scope[schema_group]['user_config'][schema_key]['function']['trend'] = changed_value	

	# update the page data renew status
	edit_column_adder_event(scope, schema_key)
	