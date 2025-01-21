
import streamlit as st



def button_reset_page(scope):
	st.button(
			label='Reset', 
			use_container_width=True,
			on_click=reset_render_status, 
			args=(scope,),
			help='Reset the Page to the Initial State (hides everything)'
			)


def reset_render_status(scope):
	page = scope.config['display']
	
	scope.page[page]['show']['settings_trials'] 	= False
	scope.page[page]['show']['settings_strategy'] 	= False
	scope.page[page]['show']['settings_charts'] 	= False
	scope.page[page]['show']['settings_overlay'] 	= False
	scope.page[page]['show']['config_ticker_data'] 	= False
	scope.page[page]['show']['config_page'] 		= False
	scope.page[page]['show']['ticker_file'] 		= 'Show/Hide Data'

	scope.page[page]['search_results'] 			= {}

	if page == 'index':
		scope.ticker_index['render']['industry_report'] = False
