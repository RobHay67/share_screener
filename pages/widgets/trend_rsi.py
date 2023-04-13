import streamlit as st

from tickers.events.edit_column_adder import edit_column_adder_event

from trials.config import trends_for_rsi


def edit_trend_rsi(scope, config_group, config_key ):
	widget_key = 'widget_trend_' + config_group + '_' + config_key
	display_name = 'Trend'
	previous_selection = scope[config_group]['config'][config_key]['add_columns']['trend']
	pos_for_previous = trends_for_rsi.index(previous_selection)	

	st.selectbox ( 
					label		=display_name, 
					options		=trends_for_rsi,
					index		=pos_for_previous, 
					on_change	=on_change_rsi_selection,
					args		=(scope, config_group, config_key, widget_key, ),
					key			=widget_key,
					) 


def on_change_rsi_selection(scope:dict, config_group:str, config_key:str, widget_key:str):

	changed_value = scope[widget_key]

	# store the selection
	scope[config_group]['config'][config_key]['add_columns']['trend'] = changed_value	

	# update the page data renew status
	edit_column_adder_event(scope, config_key)
	