import streamlit as st


from pages.model.set_page_df_status import set_refresh_page_df_all


def set_page_row_limit():

	page_row_limit = st.sidebar.number_input( 
							'No of Rows for Analysis & Charts', 
							min_value=100, 
							key='89',
							on_change=set_refresh_page_df_all, 
							)
	return page_row_limit


