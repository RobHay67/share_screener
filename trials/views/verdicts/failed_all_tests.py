import logging
import streamlit as st


def show_all_verdicts_failed():
	logging.debug("show_all_verdicts_failed")
	st.error('No Passing Verdicts to Render')

