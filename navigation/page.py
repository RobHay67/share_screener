
import streamlit as st



# Helper - stores the selected page from the sidebar so we stay where we are on re-renders
def store_page(page:str):
	st.session_state.display_page = page