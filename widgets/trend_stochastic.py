import streamlit as st

from tickers.events.edit_column_adder import edit_column_adder_event

from trials.config import trends_for_stochastic


def edit_trend_stochastic(scope, type_config, column_adder ):
	widget_key = 'widget_trend_' + type_config + '_' + column_adder
	display_name = 'Trend'
	previous_selection = scope[type_config][column_adder]['add_columns']['trend']
	pos_for_previous = trends_for_stochastic.index(previous_selection)	

	st.selectbox ( 
					label		=display_name, 
					options		=trends_for_stochastic,
					index		=pos_for_previous, 
					on_change	=on_change_stochastic_selection,
					args		=(scope, type_config, column_adder, widget_key, ),
					key			=widget_key,
					) 


def on_change_stochastic_selection(scope:dict, type_config:str, column_adder:str, widget_key:str):

	changed_value = scope[widget_key]

	# store the selection
	scope[type_config][column_adder]['add_columns']['trend'] = changed_value	

	# update the app data renew status
	edit_column_adder_event(scope, column_adder)
	