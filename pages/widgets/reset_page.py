
import streamlit as st



def reset_page_render(scope):
	st.button(
			label='Reset Page', 
			use_container_width=True,
			on_click=reset_render_status, 
			args=(scope,),
			help='Reset the Page to the Initial State (hides everything)'
			)


def reset_render_status(scope):
	page = scope.display_page
	scope.pages[page]['render']['ticker_file'] = 'Show/Hide Data'

	scope.pages[page]['render']['app_config'] = False
	scope.pages[page]['render']['chart_settings'] = False
	scope.pages[page]['render']['overlay_settings'] = False
	scope.pages[page]['render']['trial_settings'] = False

	scope.pages[page]['render']['strategy'] = False

	scope.pages[page]['search_results'] = {}

	if page == 'index':
		scope.ticker_index['render']['industry_report'] = False
