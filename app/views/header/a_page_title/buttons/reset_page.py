
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
	page = scope.display['page']
	
	scope.page[page]['show']['trials'] 		= False
	scope.page[page]['show']['strategy'] 	= False
	scope.page[page]['show']['charts'] 		= False
	scope.page[page]['show']['overlays'] 	= False
	scope.page[page]['show']['config'] 		= None
	scope.page[page]['show']['ticker_file'] = 'Show/Hide Data'

	scope.page[page]['search_results'] 		= {}

	if page == 'index':
		scope.ticker_index['show']['industry_report'] = False
