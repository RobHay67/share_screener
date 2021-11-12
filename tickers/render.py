



import streamlit as st








def ticker_data_files(scope): # DONE
	st.header('Loaded and Downloaded share data.')
	list_of_loaded_tickers = list(scope.share_data_files.keys())
	list_of_loaded_tickers.sort()

	for ticker in list_of_loaded_tickers:
		ticker_data_file = scope.share_data_files[ticker]
		ticker_data_file.sort_values(by=['date'], inplace=True, ascending=False)
		my_expander = st.expander(label=ticker)
		my_expander.dataframe(ticker_data_file, 2000, 2000)	


def ticker_list(scope): # DONE
	st.header('Ticker List')
	st.subheader('target tickers for analysis')
	st.write('use sidebar to add tickers to this list)')

	ticker_list_message = ''
	for count, ticker in enumerate(scope.ticker_list):
		ticker_list_message = ticker_list_message + ticker
		if count < len(scope.ticker_list) - 1:
			ticker_list_message += '  '

	st.success(ticker_list_message)


