
import streamlit as st


def chart_dfs_button(scope):
	
	# This will be a count of the tickers that have been selcted
	# for this app for mining

	app 					= scope.apps['display_app']
	ticker_list 			= scope.apps[app]['mined_tickers']
	chart_df_ticker_count	= len(ticker_list)
	total_chart_df_rows	  	= 0

	for ticker in ticker_list:
		chart_df_row_count	= len(scope.tickers[ticker]['apps'][app]['df'])
		total_chart_df_rows += chart_df_row_count

	chart_dfs_button_message 	= (str(chart_df_ticker_count) + ' chart (' + str(total_chart_df_rows) + ' rows)')
	
	return st.button(chart_dfs_button_message)


def view_chart_dfs(scope):

	st.write('**Chart DataFrames**')

	app = scope.apps['display_app']
	# render_expanded = False
	
	if app == 'scope':
		app = 'single'
		st.subheader('Charting app Dataframes')
		col1,col2 = st.columns([6,2])
		with col1: st.write('Chart_df stored in > ')
		with col2: st.write("< scope.apps[app]['dfs'] >")	
		st.markdown("""---""")
		
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
		chart_df = scope.tickers[ticker]['apps'][app]['df']
		no_of_rows = str(len(chart_df))
		my_expander = st.expander(label=(ticker+' ( ' + no_of_rows + ' )'), expanded=False)
		my_expander.dataframe(chart_df, 2000, 2000)	
