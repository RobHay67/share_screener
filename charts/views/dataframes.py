import streamlit as st


def view_chart_dfs(scope, page='all'):
	
	if page == 'all':
		st.subheader('All Charting Dataframes')
		col1,col2 = st.columns([6,2])
		with col1: st.write('Chart_df stored in > ')
		with col2: st.write("< scope.pages[page]['chart_df'] >")	
		st.markdown("""---""")
		list_of_pages = list(scope.pages.keys())
	else:
		list_of_pages = [page]

	# Create a disctionary of tickers to iterate over
	list_of_tickers = {}
	for page in list_of_pages:
		for ticker in scope.pages[page]['ticker_list']:
			if ticker != 'select a ticker':
				list_of_tickers[ticker] = page

	# Render the dataframes in alphabetical order
	for ticker in sorted(list_of_tickers.keys()):
		page = list_of_tickers[ticker]
		chart_df = scope.pages[page]['chart_df'][ticker]
		no_of_rows = str(len(chart_df))
		chart_df.sort_values(by=['date'], inplace=True, ascending=False)
		my_expander = st.expander(label=(ticker+' ( ' + no_of_rows + ' )'))
		my_expander.dataframe(chart_df, 2000, 2000)	
		chart_df.sort_values(by=['date'], inplace=True, ascending=True)