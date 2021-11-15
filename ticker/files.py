
import streamlit as st


from system.reports import render_3_columns


def ticker_files_report(scope):
	st.subheader('Loaded and Downloaded share data.')

	col1,col2 = st.columns([6,2])
	with col1: st.write('Loaded and Downloaded share data stored in > ')
	with col2: st.write('< ticker_data_files >')								# TODO this needs to be renamed

	list_of_loaded_tickers = list(scope.ticker_data_files.keys())

	for ticker in list_of_loaded_tickers:
		my_expander = st.expander(label=ticker)
		# TODO - this is where the sorting of the dataframes should occur - we can probably do it in one go and then undo it at the end
		my_expander.dataframe(scope.ticker_data_files[ticker], 2000, 2000)


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Reports
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

def render_ticker_files(scope): # 
	st.subheader('Loaded and downloaded Ticker data.')
	st.markdown("""---""")

	list_of_loaded_tickers = list(scope.ticker_data_files.keys())
	list_of_loaded_tickers.sort()

	for ticker in list_of_loaded_tickers:
		ticker_data_file = scope.ticker_data_files[ticker]
		ticker_data_file.sort_values(by=['date'], inplace=True, ascending=False)
		my_expander = st.expander(label=ticker)
		my_expander.dataframe(ticker_data_file, 2000, 2000)	

def render_ticker_file(scope, ticker): # WIP
	if ticker in list(scope.ticker_data_files.keys()):
		ticker_data_file = scope.ticker_data_files[ticker]
		ticker_data_file.sort_values(by=['date'], inplace=True, ascending=False)
		my_expander = st.expander(label=ticker, expanded=True)
		my_expander.dataframe(ticker_data_file, 2000, 2000)	

def selected_tickers_for_each_page(scope): # 
	st.subheader('Selected Ticker(s) for each Page')

	col1,col2 = st.columns([2,10])

	with col1: st.markdown('##### Single Ticker Analysis')
	with col2: st.write(scope.selected['single']['ticker_list'][0])

	with col1: st.markdown('##### Intra Day Analysis')
	with col2: st.write(scope.selected['intraday']['ticker_list'][0])

	with col1: st.markdown('##### Volume Prediction')
	with col2: st.write(scope.selected['volume']['ticker_list'][0])

	with col1: st.markdown('##### Research Ticker')
	with col2: st.write(scope.selected['research']['ticker_list'][0])

	with col1: st.markdown('##### Multi Ticker Analysis List')
	ticker_list_message = ''
	for count, ticker in enumerate(scope.selected['multi']['ticker_list']):
		ticker_list_message = ticker_list_message + ticker
		if count < len(scope.selected['multi']['ticker_list']) - 1:
			ticker_list_message += '  '

	with col2: st.write(ticker_list_message)

