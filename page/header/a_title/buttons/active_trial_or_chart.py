import logging
import streamlit as st


def button_show_active_trials_or_charts(scope):
	logging.debug("button_show_active_trials_or_charts")
	page = scope.display['page']
	current_value = scope.page[page]['show']['active_trial_or_chart']
	type_of_button = 'primary' if current_value == True else 'secondary'

	button = st.button(
					label = '💡', 
					use_container_width=True, 
					on_click=clicked_show_active_trials_or_charts, args=(scope, page, ),
					type=type_of_button,
					help='Active - Charts or Trials'
					)
	return 

def clicked_show_active_trials_or_charts(scope, page):
	logging.warning("clicked_show_active_trials_or_charts")
	previous_value = scope.page[page]['show']['active_trial_or_chart']
	new_value = True if previous_value == False else False

	scope.page[page]['show']['active_trial_or_chart'] = new_value