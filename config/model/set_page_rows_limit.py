import streamlit as st


from config.model.set_page_df_refresh import set_refresh_df_all_tickers_in_all_pages



def set_page_row_limit():

	page_row_limit = st.sidebar.number_input( 
							'No of Rows for Analysis & Charts', 
							min_value=100, 
							key='89',
							on_change=set_refresh_df_all_tickers_in_all_pages, 
							)
	return page_row_limit


