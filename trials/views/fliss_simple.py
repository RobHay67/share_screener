import streamlit as st
import logging


def show_fliss_simple_strategy(scope):
	logging.debug("show_fliss_simple_strategy")
	st.divider()
	st.subheader('Fliss Simple Strategy')
	st.write('Closing Price is up n times over the last x days')
	st.write('Volume is up n times over the last x days')

