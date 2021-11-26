
import streamlit as st



def set_refresh_analysis_for_all_pages():
	# reset STATUS to prevent unnecesary updates 
	# (as this applies to all pages - they all need a refresh)
	for page in st.session_state.pages:
		st.session_state.pages[page]['refresh_analysis_df'] = True
