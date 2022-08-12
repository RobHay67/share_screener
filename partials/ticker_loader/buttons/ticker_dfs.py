import streamlit as st


def ticker_dfs_button(scope):
	
	# How many tickers are available for the apps
	# this will be a count of the loaded (and download) files
	
	no_of_loaded_files 	= len(scope.tickers.keys())
	total_loaded_rows	= 0	
	
	for ticker in scope.tickers.keys():
		loaded_df_row_count = int(len(scope.tickers[ticker]['df']))
		total_loaded_rows += loaded_df_row_count

	file_desc = ' file (' if no_of_loaded_files == 1 else ' files ('

	loaded_dfs_button_message 	= (str(no_of_loaded_files) + file_desc + str(total_loaded_rows) + ' rows)')

	return st.button(loaded_dfs_button_message)


def view_ticker_files(scope):
	
	st.write('**Ticker Files (loaded data)**')

	app = scope.apps['display_app']	
	# render_expanded = False

	if app == 'scope':
		st.subheader('All Ticker Data Files')
		
		col1,col2 = st.columns([6,2])
		with col1: st.write('Loaded and Downloaded ticker data stored in > ')
		with col2: st.write('< scope.tickers >')	
		st.markdown("""---""")

	ticker_list = sorted(list(scope.tickers.keys()))
	no_of_tickers = len(ticker_list)

	for i in range(0, no_of_tickers, 3):
		col1,col2,col3=st.columns([2,2,2])
		with col1: render_df(scope, ticker_list, i, )
		with col2: render_df(scope, ticker_list, i+1)
		with col3: render_df(scope, ticker_list, i+2)


def render_df(scope, ticker_list, i):

	if i < len(ticker_list):
		ticker = ticker_list[i]
		ticker_data_file = scope.tickers[ticker]['df']

		no_of_rows = str(len(ticker_data_file))
		my_expander = st.expander(label=(ticker+' ( ' + no_of_rows + ' )'), expanded=False )
		my_expander.dataframe(ticker_data_file, 2000, 2000)	

		# print(i, ' - ', ticker_list[i])

