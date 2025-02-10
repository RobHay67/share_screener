import logging
import streamlit as st


def show_all_verdicts_failed():
	logging.debug("show_all_verdicts_failed")

	st.subheader('No Passing Verdicts to Render')
	st.error('No Passing Verdicts to Render')

