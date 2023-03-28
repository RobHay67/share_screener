
import streamlit as st


# TODO - not sure that these are needed anymore - might be able to
# deprecate or delete these functions
# keep handy for a template for the minute



def reset_page_render(scope):
	st.button(
			label='Reset Page', 
			use_container_width=True,
			on_click=reset_render_status, 
			args=(scope,),
			help='Reset the Page to the Initial State (hides everything)'
			)



def reset_render_status(scope):
	app = scope.apps['display_app']

	scope.apps[app]['render']['ticker_file'] = 'Show/Hide Data'

	scope.apps[app]['render']['app_config'] = False
	scope.apps[app]['render']['chart_settings'] = False
	scope.apps[app]['render']['overlay_settings'] = False
	scope.apps[app]['render']['trial_settings'] = False

	scope.apps[app]['render']['strategy'] = False

	scope.apps[app]['search_results'] = {}
