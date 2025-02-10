
import logging
import streamlit as st




def set_streamlit_page_config():
	logging.warning("set_streamlit_page_config")
	# This code should only run the one time (on initial load)
	
	# Set the Browser Tab Name for the Page
	st.set_page_config( 
			page_title='Share Picker', 
			page_icon='📊',
			layout="wide",								# Allow wide Screen to be taken advantage of
			)
	
	# Padding Between Controls
	# padding = 1.0
	# st.markdown(f""" <style>
	# 	.reportview-container .main .block-container{{
	# 		padding-top: {padding}rem;
	# 		padding-right: {padding}rem;
	# 		padding-left: {padding}rem;
	# 		padding-bottom: {padding}rem;
	# 	}} </style> """, unsafe_allow_html=True)

	# Remove whitespace from the top of the page and sidebar
	# st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True) # this is heaps better
	# st.write('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)
	# st.markdown("""
	# 				<style>
	# 					.css-o18uir.e16nr0p33 {
	# 					margin-top: -75px;
	# 					}
	# 				</style>
	# 				""", unsafe_allow_html=True)

	# st.markdown(
    #         f'''
    #         <style>
    #             .reportview-container .sidebar-content {{
    #                 padding-top: {1}rem;
    #             }}
    #             .reportview-container .main .block-container {{
    #                 padding-top: {1}rem;
    #             }}
    #         </style>
    #         ''',unsafe_allow_html=True)


	# st.markdown("""
    #     <style>
    #         #    .css-18e3th9 {
    #         #         padding-top: 0rem;
    #         #         padding-bottom: 10rem;
    #         #         padding-left: 5rem;
    #         #         padding-right: 5rem;
    #         #     }
    #         #    .css-1d391kg {
    #         #         padding-top: 1rem;
    #         #         padding-right: 1rem;
    #         #         padding-bottom: 3.5rem;
    #         #         padding-left: 1rem;
    #         #     }
    #     </style>
    #     """, unsafe_allow_html=True)

