import logging
import streamlit as st
from users.helpers.reset_page_to_defaults import reset_page_to_default_values


def button_reset_page(scope):
	logging.debug("button_reset_page")
	st.button(
			label='Reset', 
			use_container_width=True,
			on_click=reset_page_to_default_values, 
			args=(scope,),
			help='Reset the Page to the Initial State (hides everything)'
			)


