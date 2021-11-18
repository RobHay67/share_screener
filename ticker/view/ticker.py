import streamlit as st


def view_a_ticker_file(scope, ticker): # WIP
	if ticker in list(scope.ticker_data_files.keys()):
		ticker_data_file = scope.ticker_data_files[ticker]
		ticker_data_file.sort_values(by=['date'], inplace=True, ascending=False)
		no_of_rows = str(len(ticker_data_file))
		my_expander = st.expander(label=(ticker+' ( ' + no_of_rows + ' )'), expanded=True)
		my_expander.dataframe(ticker_data_file, 2000, 2000)	
		ticker_data_file.sort_values(by=['date'], inplace=True, ascending=True)

