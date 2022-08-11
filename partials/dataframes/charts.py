import streamlit as st

def view_chart_dfs(scope):

	app = scope.apps['display_app']
	render_expanded = False
	
	if app == 'scope':
		app = 'single'
		st.subheader('Charting app Dataframes')
		col1,col2 = st.columns([6,2])
		with col1: st.write('Chart_df stored in > ')
		with col2: st.write("< scope.apps[app]['dfs'] >")	
		st.markdown("""---""")
		
	# ticker_list = sorted(list(scope.apps[app]['dfs'].keys()))
	ticker_list = scope.apps[app]['mined_tickers']
	no_of_tickers = len(ticker_list)

	for i in range(0, no_of_tickers, 3):
		col1,col2,col3=st.columns([2,2,2])
		with col1: render_chart_df(scope, app, ticker_list, i, )
		with col2: render_chart_df(scope, app, ticker_list, i+1)
		with col3: render_chart_df(scope, app, ticker_list, i+2)


def render_chart_df(scope, app, ticker_list, i):
	if i < len(ticker_list):
		ticker = ticker_list[i]
		# chart_df = scope.apps[app]['dfs'][ticker]
		chart_df = scope.tickers[ticker]['apps'][app]['df']
		no_of_rows = str(len(chart_df))
		my_expander = st.expander(label=(ticker+' ( ' + no_of_rows + ' )'), expanded=False)
		my_expander.dataframe(chart_df, 2000, 2000)	