import streamlit as st


def view_all_loaded_ticker_files(scope): # 
	st.subheader('Loaded and downloaded Ticker Files')
	col1,col2 = st.columns([6,2])
	with col1: st.write('Loaded and Downloaded ticker data stored in > ')
	with col2: st.write('< ticker_data_files >')	
	st.markdown("""---""")

	list_of_loaded_tickers = list(scope.ticker_data_files.keys())
	list_of_loaded_tickers.sort()

	for ticker in list_of_loaded_tickers:
		ticker_data_file = scope.ticker_data_files[ticker]
		ticker_data_file.sort_values(by=['date'], inplace=True, ascending=False)
		no_of_rows = str(len(ticker_data_file))
		my_expander = st.expander(label=(ticker+' ( ' + no_of_rows + ' )'))
		# TODO - this is where the sorting of the dataframes should occur - we can probably do it in one go and then undo it at the end
		my_expander.dataframe(ticker_data_file, 2000, 2000)	



