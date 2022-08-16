
import streamlit as st




# Callers - so that the embedded functions will still work without adding additional function variable attributes

def render_ticker_dfs(scope):
	df_locations = 'tickers'
	ticker_list = sorted(list(scope.tickers.keys()))
	render_dfs(scope, 'tickers', df_locations, ticker_list )

def render_chart_dfs(scope):
	df_locations = 'single'
	ticker_list = sorted(scope.apps['single']['mined_tickers'])
	render_dfs(scope, 'charts', df_locations, ticker_list )

def render_trial_dfs(scope):
	df_locations = 'screener'
	ticker_list = sorted(scope.apps['screener']['mined_tickers'])
	render_dfs(scope, 'trials', df_locations, ticker_list )


def render_dfs(scope, type_df, df_location, ticker_list):

	st.write( "**" + "DataFrames > " +type_df.capitalize() + "**")

	# if called by the scope app, add some header information first
	if scope.apps['display_app'] == 'scope':
		st.subheader(type_df.capitalize() + ' DataFrames')
		# render a 2 column matrix for the df cache location
		col1,col2 = st.columns([6,2])
		line_1 = (type_df + ' dfs cached in > ')
		if type_df == 'tickers':
			line_2 = "< scope.tickers >"
		else:
			line_2 = "< scope.apps['" + df_location + "']['dfs'] >"
		with col1: st.write(line_1)
		with col2: st.write(line_2)
		st.markdown("""---""")

	# No of dfs required
	dfs_total = len(ticker_list)

	# render dfs in 3 column matrix
	for i in range(0, dfs_total, 3):	
		col1,col2,col3=st.columns([2,2,2])
		with col1: render_df(scope, type_df, ticker_list, i, )
		with col2: render_df(scope, type_df, ticker_list, i+1)
		with col3: render_df(scope, type_df, ticker_list, i+2)


def render_df(scope, type_df, ticker_list, i):
	
	# Only execute if we are before the end of the ticker list
	if i < len(ticker_list):
		ticker = ticker_list[i]

		if type_df=='tickers':
			df = scope.tickers[ticker]['df']
		# to cope with scope also calling these functions
		if type_df == 'charts':
			df = scope.tickers[ticker]['apps']['single']['df']
		if type_df == 'trials':
			df = scope.tickers[ticker]['apps']['screener']['df']

		no_of_rows = str(len(df))
		my_expander = st.expander(label=(ticker+' ( ' + no_of_rows + ' )'), expanded=False )
		my_expander.dataframe(df, 2000, 2000)	



