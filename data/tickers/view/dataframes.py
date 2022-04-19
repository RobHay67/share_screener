import streamlit as st



def view_ticker_data_files(scope, page='all'):
	print('here')
	# page = scope.pages['display_page']
	
	if page == 'all':
		st.subheader('All Ticker Data Files')
		
		col1,col2 = st.columns([6,2])
		with col1: st.write('Loaded and Downloaded ticker data stored in > ')
		with col2: st.write('< scope.data[ticker_files] >')	
		st.markdown("""---""")
		list_of_pages = scope.pages['page_list'] 	# all of the pages
		render_expanded = False
	else:
		list_of_pages = [page]
		render_expanded = False


	# Create a dictionary of tickers to iterate over
	ticker_to_page_map = {}

	for page in list_of_pages:
		for ticker in scope.pages[page]['ticker_list']:
			print(ticker)
			if ticker != 'select a ticker':
				if ticker in scope.data['ticker_files']:
					ticker_to_page_map[ticker] = page

	for ticker in ticker_to_page_map:
		page = ticker_to_page_map[ticker]
		ticker_data_file = scope.data['ticker_files'][ticker]

		no_of_rows = str(len(ticker_data_file))
		ticker_data_file.sort_values(by=['date'], inplace=True, ascending=False)
		my_expander = st.expander(label=(ticker+' ( ' + no_of_rows + ' )'), expanded=render_expanded )
		my_expander.dataframe(ticker_data_file, 2000, 2000)	
		ticker_data_file.sort_values(by=['date'], inplace=True, ascending=True)




