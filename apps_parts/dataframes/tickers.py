import streamlit as st



def view_ticker_files(scope):
	app = scope.apps['display_app']
	print('display_app = ', app)
	render_expanded = False

	if app == 'scope':
		st.subheader('All Ticker Data Files')
		
		col1,col2 = st.columns([6,2])
		with col1: st.write('Loaded and Downloaded ticker data stored in > ')
		with col2: st.write('< scope.data.ticker_files >')	
		st.markdown("""---""")

	ticker_list = sorted(list(scope.data['ticker_files'].keys()))
	no_of_tickers = len(ticker_list)

	for i in range(0, no_of_tickers, 3):
		col1,col2,col3=st.columns([2,2,2])
		with col1: render_df(scope, ticker_list, i, )
		with col2: render_df(scope, ticker_list, i+1)
		with col3: render_df(scope, ticker_list, i+2)




def render_df(scope, ticker_list, i):

	if i < len(ticker_list):
		ticker = ticker_list[i]
		ticker_data_file = scope.data['ticker_files'][ticker]

		no_of_rows = str(len(ticker_data_file))
		my_expander = st.expander(label=(ticker+' ( ' + no_of_rows + ' )'), expanded=False )
		my_expander.dataframe(ticker_data_file, 2000, 2000)	

		print(i, ' - ', ticker_list[i])


