
import streamlit as st
from ticker_index.download import download_ticker_index_data


def button_download_ticker_index(scope):
	
	widget_key = 'widget_button_download_ticker_index'
	
	button = st.button(
						label='🌐 Download new Data', 
						use_container_width=True, 
						type='secondary',
						key=widget_key,
						on_click=perform_the_download,
						args=(scope, )
						)
	
	return button


def perform_the_download(scope):

	scope.ticker_index['render']['industry_report'] = False
	scope.ticker_index['render']['ticker_index'] = False
	scope.ticker_index['render']['editable_df'] = False

	download_ticker_index_data(scope)


