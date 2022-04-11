import streamlit as st


def view_chart_dfs(scope, page='all'):
	
	if page == 'all':
		st.subheader('All Charting Dataframes')
		col1,col2 = st.columns([6,2])
		with col1: st.write('Chart_df stored in > ')
		with col2: st.write("< scope.pages[page]['df'] >")	
		st.markdown("""---""")
		# list_of_pages = list(scope.pages.keys())
		list_of_pages = scope.pages['page_list']
		render_expanded = False
	elif page == 'screener':
		list_of_pages = [page]
		render_expanded = False
	else:
		list_of_pages = [page]
		render_expanded = True

	# Create a disctionary of tickers to iterate over
	list_of_tickers = {}
	for page in list_of_pages:
		for ticker in scope.pages[page]['ticker_list']:
			if ticker != 'select a ticker':
				if ticker in scope.pages[page]['df']:
					list_of_tickers[ticker] = page

	# Render the dataframes in alphabetical order
	for ticker in sorted(list_of_tickers.keys()):
		page = list_of_tickers[ticker]
		chart_df = scope.pages[page]['df'][ticker]
		no_of_rows = str(len(chart_df))
		chart_df.sort_values(by=['date'], inplace=True, ascending=False)
		my_expander = st.expander(label=(ticker+' ( ' + no_of_rows + ' )'), expanded=render_expanded)
		my_expander.dataframe(chart_df, 2000, 2000)	
		chart_df.sort_values(by=['date'], inplace=True, ascending=True)



def view_screener_dfs(scope, page='all'):

	if page == 'all':
		st.subheader('All Analysis Dataframes')
		col1,col2 = st.columns([6,2])
		with col1: st.write('Analysis DataFrames stored in > ')
		with col2: st.write("< scope.pages[page]['df'] >")	
		st.markdown("""---""")
		# list_of_pages = list(scope.pages.keys())
		list_of_pages = scope.pages['page_list']
		render_expanded = False
	elif page == 'screener':
		list_of_pages = [page]
		render_expanded = False
	else:
		list_of_pages = [page]
		render_expanded = True

	# Create a disctionary of tickers to iterate over
	list_of_tickers = {}
	for page in list_of_pages:
		for ticker in scope.pages[page]['ticker_list']:
			if ticker != 'select a ticker':
				if ticker in scope.pages[page]['df']:
					list_of_tickers[ticker] = page

	# Render the dataframes in alphabetical order
	for ticker in sorted(list_of_tickers.keys()):
		page = list_of_tickers[ticker]
		screener_df = scope.pages[page]['df'][ticker]
		no_of_rows = str(len(screener_df))
		screener_df.sort_values(by=['date'], inplace=True, ascending=False)
		my_expander = st.expander(label=(ticker+' ( ' + no_of_rows + ' )'), expanded=render_expanded)
		my_expander.dataframe(screener_df, 2000, 2000)	
		screener_df.sort_values(by=['date'], inplace=True, ascending=True)

