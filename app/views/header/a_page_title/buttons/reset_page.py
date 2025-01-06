
import streamlit as st



def reset_page_button(scope):
	st.button(
			label='Reset', 
			use_container_width=True,
			on_click=reset_render_status, 
			args=(scope,),
			help='Reset the Page to the Initial State (hides everything)'
			)


def reset_render_status(scope):
	page = scope.config['display']
	scope.page[page]['render']['ticker_file'] 		= 'Show/Hide Data'

	scope.page[page]['render']['page_config'] 		= False
	scope.page[page]['render']['chart_settings'] 	= False
	scope.page[page]['render']['overlay_settings'] = False
	scope.page[page]['render']['trial_settings'] 	= False
	scope.page[page]['render']['strategy'] 		= False
	scope.page[page]['render']['ticker_config'] 	= False

	scope.page[page]['search_results'] 			= {}

	if page == 'index':
		scope.ticker_index['render']['industry_report'] = False
