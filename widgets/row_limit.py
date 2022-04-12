
import streamlit as st

from pages.data.status import set_page_renew_status


def render_row_limit(scope):
	scope.pages['row_limit'] =  st.sidebar.number_input( 
														'No of Rows for Analysis & Charts', 
														min_value=100, 
														on_change=on_change_row_limit,
														args=(scope, )
														)



def on_change_row_limit(scope:dict):
	set_page_renew_status(scope, ticker_data=True, expanders='all', caller='on_change_row_limit' )