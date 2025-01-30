import streamlit as st


def dropdown_select_config(scope):
	page = scope.display['page']
	widget_key = 'widget_' + page + '_select_config'
	
	match page:
		case 'screener':config_list 	= ['Nothing','Page Config','Ticker Data', 'Verdicts', 'Trials', 'Strategies',]
		case 'chart':config_list 		= ['Nothing','Page Config','Ticker Data', 'Charts']
		case 'intraday':config_list 	= ['Nothing','Page Config','Ticker Data']
		case 'volume':config_list 		= ['Nothing','Page Config','Ticker Data']
		case 'research':config_list 	= ['Nothing','Page Config']
		case 'websites':config_list 	= ['Nothing','Page Config']
		case 'ticker_index':config_list	= ['Nothing','Page Config','Ticker Index',]
		case 'testing':config_list 		= ['Nothing','Page Config']
		case _:st.write(":red[Unknown Page Called = "+page+"]")

	# config_list = sorted(config_list)
	
	with st.popover('Config', use_container_width=True):
		st.radio(
				label="Choose Configuration to Display",
				options=config_list,
				on_change	=on_change_show_config_selection,
				args		=(scope, page, widget_key, ),
				key			=widget_key,
				
				),
		


def on_change_show_config_selection(scope, page, widget_key):
	selected_config = scope[widget_key]
	scope.page[page]['show']['config'] = selected_config
