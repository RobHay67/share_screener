
import streamlit as st


def trial_dfs_button(scope):

	# This will be a count of the tickers that have been selcted
	# for this app for mining

	app 						= scope.apps['display_app']
	ticker_list 				= scope.apps[app]['mined_tickers']
	screener_df_ticker_count 	= len(ticker_list)
	total_screener_df_rows	 	= 0

	for ticker in ticker_list:
		screener_df_row_count	= len(scope.tickers[ticker]['apps'][app]['df'])
		total_screener_df_rows 	+= screener_df_row_count

	analysis_dfs_button_message 	= (str(screener_df_ticker_count) + ' trial (' + str(total_screener_df_rows) + ' rows)')

	return st.button(analysis_dfs_button_message)



import streamlit as st


def view_trials_dfs(scope):
	
	st.write('**Trial DataFrames**')
	
	app = scope.apps['display_app']
	# render_expanded = False

	if app == 'scope':
		app='screener'
		st.subheader('Screener app Dataframes')
		col1,col2 = st.columns([6,2])
		with col1: st.write('Analysis DataFrames stored in > ')
		with col2: st.write("< scope.apps[app]['dfs'] >")	
		st.markdown("""---""")

	# ticker_list = sorted(list(scope.apps[app]['dfs'].keys()))
	ticker_list = sorted(scope.apps['screener']['mined_tickers'])
	no_of_tickers = len(ticker_list)
	
	for i in range(0, no_of_tickers, 3):
		col1,col2,col3=st.columns([2,2,2])
		with col1: render_trial_df(scope, app, ticker_list, i, )
		with col2: render_trial_df(scope, app, ticker_list, i+1)
		with col3: render_trial_df(scope, app, ticker_list, i+2)



def render_trial_df(scope, app, ticker_list, i):
	if i < len(ticker_list):
		ticker = ticker_list[i]
		screener_df = scope.tickers[ticker]['apps'][app]['df']
		no_of_rows = str(len(screener_df))
		my_expander = st.expander(label=(ticker+' ( ' + no_of_rows + ' )'), expanded=False)
		my_expander.dataframe(screener_df, 2000, 2000)	


