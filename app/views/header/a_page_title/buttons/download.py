import streamlit as st

from tickers.scope.model.download import download_ticker_data


def download_button(scope):

	download_button_msg = 'Download (' + str(scope.config['download_days'] + ')')
		
	button = st.button(
		label=download_button_msg, 
		# help="Press to download the previous X days. If button disabled, select ticker(s)",
		on_click=download_tickers,
		args=(scope, ),
		use_container_width=True, 
		)

	return button


def download_tickers(scope):
	st.write('Reset Progress Bar')
	download_ticker_data(scope)


