
import streamlit as st
from ticker_index.scope.model.download import download_ticker_index_data


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

	scope.ticker_index['show']['industry_report'] = False
	scope.ticker_index['show']['ticker_index'] = False
	scope.ticker_index['show']['editable_df'] = False

	download_ticker_index_data(scope)


