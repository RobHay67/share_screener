import streamlit as st



def view_ticker_data_files(scope, page='all'):
	if page == 'all':
		st.subheader('All Ticker Data Files')
		col1,col2 = st.columns([6,2])
		with col1: st.write('Loaded and Downloaded ticker data stored in > ')
		with col2: st.write('< scope.ticker_data_files >')	
		st.markdown("""---""")
		list_of_pages = list(scope.pages.keys())
		render_expanded = False
	else:
		list_of_pages = [page]
		render_expanded = True

	# Create a dictionary of tickers to iterate over
	list_of_tickers = {}
	for page in list_of_pages:
		for ticker in scope.pages[page]['ticker_list']:
			if ticker != 'select a ticker':
				list_of_tickers[ticker] = page

	for ticker in list_of_tickers:
		page = list_of_tickers[ticker]
		ticker_data_file = scope.ticker_data_files[ticker]
		no_of_rows = str(len(ticker_data_file))
		ticker_data_file.sort_values(by=['date'], inplace=True, ascending=False)
		my_expander = st.expander(label=(ticker+' ( ' + no_of_rows + ' )'), expanded=render_expanded )
		my_expander.dataframe(ticker_data_file, 2000, 2000)	
		ticker_data_file.sort_values(by=['date'], inplace=True, ascending=True)




