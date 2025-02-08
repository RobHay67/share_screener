import logging
import streamlit as st

from tickers.model.download import download_ticker_data


def button_download_ticker(scope):
	logging.debug("button_download_ticker")
	download_button_msg = 'Download (' + str(scope.config['download_days'] + ')')
		
	button = st.button(
		label=download_button_msg, 
		# help="Press to download the previous X days. If button disabled, select ticker(s)",
		on_click=clicked_download_tickers,
		args=(scope, ),
		use_container_width=True, 
		)

	return button


def clicked_download_tickers(scope):
	logging.warning("clicked_download_tickers")
	logging.error('Reset Progress Bar')
	download_ticker_data(scope)


