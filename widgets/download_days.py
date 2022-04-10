import streamlit as st



def render_download_days(scope):
	scope.data['download']['days'] = st.sidebar.number_input( 
															'Days to Download (recent)', 
															min_value=7, 
															)