import logging
import streamlit as st



def button_reset_page(scope):
	logging.debug("button_reset_page")
	st.button(
			label='Reset', 
			use_container_width=True,
			on_click=clicked_reset_page_to_default_values, 
			args=(scope,),
			help='Reset the Page to the Initial State (hides everything)'
			)


def clicked_reset_page_to_default_values(scope):
	logging.warning("clicked_reset_page_to_default_values")
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

	# Reset the ticker selectors
	scope.page[page]['selectors']['ticker'] = None
	scope.page[page]['selectors']['tickers'] = []
	scope.page[page]['selectors']['industries'] = []
	scope.page[page]['selectors']['market'] = None
	scope.page[page]['list_selected_tickers'] = []
