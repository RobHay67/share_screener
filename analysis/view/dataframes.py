import streamlit as st


def view_analysis_dfs(scope, page='all'):

	if page == 'all':
		st.subheader('All Analysis Dataframes')
		col1,col2 = st.columns([6,2])
		with col1: st.write('Analysis DataFrames stored in > ')
		with col2: st.write("< scope.pages[page]['analysis_df'] >")	
		st.markdown("""---""")
		list_of_pages = list(scope.pages.keys())
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
				if ticker in scope.pages[page]['analysis_df']:
					list_of_tickers[ticker] = page

	# Render the dataframes in alphabetical order
	for ticker in sorted(list_of_tickers.keys()):
		page = list_of_tickers[ticker]
		analysis_df = scope.pages[page]['analysis_df'][ticker]
		no_of_rows = str(len(analysis_df))
		analysis_df.sort_values(by=['date'], inplace=True, ascending=False)
		my_expander = st.expander(label=(ticker+' ( ' + no_of_rows + ' )'), expanded=render_expanded)
		my_expander.dataframe(analysis_df, 2000, 2000)	
		analysis_df.sort_values(by=['date'], inplace=True, ascending=True)



