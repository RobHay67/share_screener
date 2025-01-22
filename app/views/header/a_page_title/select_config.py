import streamlit as st


def select_config_to_show(scope):
	page = scope.config['display']

	widget_key = 'widget_' + page + '_select_config'
	previous_selection = scope.page[page]['show']['config_to_show']

	match page:
		case 'screener':config_list = ['Configuration','Page Config','Ticker Data']
		case 'chart':config_list = ['Configuration','Page Config','Ticker Data']
		case 'intraday':config_list = ['Page Config','Ticker Data']
		case 'volume':config_list = ['Page Config','Ticker Data']
		case 'research':config_list = ['Page Config']
		case 'website':config_list = ['Page Config']
		case 'ticker_index':config_list = ['Configuration', 'Page Config']
		# case 'scope':config_list = []
		# case 'logout':config_list = []
		# case 'testing':config_list = []
		case _:st.write(":red[Unknown Page Called = "+page+"]")

	if previous_selection == None:
		pos_for_previous = 0
	else:
		pos_for_previous = config_list.index(previous_selection)	


	st.selectbox(
			# label=':red[Select Somthing]',
			# label="🎛 Show Config",
			label='',
			options=config_list,
			index		=pos_for_previous, 
			# help		='Select the type of config to display',
			on_change	=on_change_show_config_selection,
			args		=(scope, page, widget_key, ),
			key			=widget_key,
			)

def on_change_show_config_selection(scope, page, widget_key):
	selected_config = scope[widget_key]
	scope.page[page]['show']['ticker_file'] = selected_config	

