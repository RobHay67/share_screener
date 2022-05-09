import streamlit as st



def render_chart_df(scope, page, ticker_list, i):
	if i < len(ticker_list):
		ticker = ticker_list[i]
		chart_df = scope.pages[page]['dfs'][ticker]
		no_of_rows = str(len(chart_df))
		my_expander = st.expander(label=(ticker+' ( ' + no_of_rows + ' )'), expanded=False)
		my_expander.dataframe(chart_df, 2000, 2000)	


def render_screener_df(scope, page, ticker_list, i):
	if i < len(ticker_list):
		ticker = ticker_list[i]
		screener_df = scope.pages[page]['dfs'][ticker]
		no_of_rows = str(len(screener_df))
		my_expander = st.expander(label=(ticker+' ( ' + no_of_rows + ' )'), expanded=False)
		my_expander.dataframe(screener_df, 2000, 2000)	




def view_chart_dfs(scope):

	page = scope.pages['display_page']
	render_expanded = False
	
	if page == 'scope':
		page = 'single'
		st.subheader('All Charting Dataframes')
		col1,col2 = st.columns([6,2])
		with col1: st.write('Chart_df stored in > ')
		with col2: st.write("< scope.pages[page]['dfs'] >")	
		st.markdown("""---""")
		
	ticker_list = sorted(list(scope.pages[page]['dfs'].keys()))
	no_of_tickers = len(ticker_list)

	for i in range(0, no_of_tickers, 3):
		col1,col2,col3=st.columns([2,2,2])
		with col1: render_chart_df(scope, page, ticker_list, i, )
		with col2: render_chart_df(scope, page, ticker_list, i+1)
		with col3: render_chart_df(scope, page, ticker_list, i+2)



def view_screener_dfs(scope):

	page = scope.pages['display_page']
	render_expanded = False

	if page == 'scope':
		page='screener'
		st.subheader('Page Dataframes')
		col1,col2 = st.columns([6,2])
		with col1: st.write('Analysis DataFrames stored in > ')
		with col2: st.write("< scope.pages[page]['dfs'] >")	
		st.markdown("""---""")

	ticker_list = sorted(list(scope.pages[page]['dfs'].keys()))
	no_of_tickers = len(ticker_list)
	
	for i in range(0, no_of_tickers, 3):
		col1,col2,col3=st.columns([2,2,2])
		with col1: render_screener_df(scope, page, ticker_list, i, )
		with col2: render_screener_df(scope, page, ticker_list, i+1)
		with col3: render_screener_df(scope, page, ticker_list, i+2)

