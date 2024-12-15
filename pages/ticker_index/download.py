
import streamlit as st
from ticker_index.download import download_ticker_index_data


def button_download_ticker_index(scope):
	
	widget_key = 'widget_button_download_ticker_index'
	
	button = st.button(
						label='Download latest Ticker Index data', 
						use_container_width=True, 
						type='primary',
						key=widget_key,
						on_click=download_ticker_index_data,
						args=(scope, )
						)
	
	return button




