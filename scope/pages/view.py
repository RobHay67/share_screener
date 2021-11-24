import streamlit as st


def view_pages(scope):
	col_size_list = [1.5, 1.5, 1.0, 2.2, 2.5, 2.5, 0.8]

	col1,col2,col3,col4,col5,col6,col7 = st.columns(col_size_list)

	st.subheader('Single Analysis Pages + Settings')
	st.markdown('#### Ticker Selectors')
	view_headings(scope, col_size_list)
	view_single(scope, col_size_list)
	view_intra_day(scope, col_size_list)
	view_volume(scope, col_size_list)
	view_research(scope, col_size_list)
	st.markdown("""---""")


	st.subheader('Multi Analysis Page + Settings')
	st.markdown('#### Ticker List Construction Selectors')
	view_headings(scope, col_size_list)
	view_market(scope, col_size_list)
	view_industry(scope, col_size_list)
	view_tickers(scope, col_size_list)
	st.markdown("""---""")
	

	st.subheader('Drop Down Lists (with Contents)')
	view_dropdowns(scope)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Components - Single Ticker Analysis
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

def view_headings(scope, col_size_list):
	col1,col2,col3,col4,col5,col6,col7 = st.columns(col_size_list)
	with col1: st.markdown('##### Selector')
	with col2: st.markdown('##### Contains')
	with col3: st.markdown('##### Widget')
	with col4: st.markdown('##### Populated from')
	with col5: st.markdown('##### Current Selection')
	with col6: st.markdown('##### Selection Stored In')

def view_single(scope, col_size_list):
	col1,col2,col3,col4,col5,col6,col7 = st.columns(col_size_list)
	with col1: st.write('Single Ticker')
	with col2: st.write('Ticker from Index')
	with col3: st.write('selectbox')
	with col4: st.write('< dropdown_ticker >')
	with col5: st.write(scope.pages['single']['ticker_list'][0])
	with col6: st.write("< ticker_list['single'] >")

def view_intra_day(scope, col_size_list):
	col1,col2,col3,col4,col5,col6,col7 = st.columns(col_size_list)
	with col1: st.write('Intra Day')
	with col2: st.write('Ticker from Index')
	with col3: st.write('selectbox')
	with col4: st.write('< dropdown_ticker >')
	with col5: st.write(scope.pages['intraday']['ticker_list'][0])
	with col6: st.write("< ticker_list['intraday'] >")

def view_volume(scope, col_size_list):
	col1,col2,col3,col4,col5,col6,col7 = st.columns(col_size_list)
	with col1: st.write('Volume Prediction')
	with col2: st.write('Ticker from Index')
	with col3: st.write('selectbox')
	with col4: st.write('< dropdown_ticker >')
	with col5: st.write(scope.pages['volume']['ticker_list'][0])
	with col6: st.write("< ticker_list['volume'] >")

def view_research(scope, col_size_list):
	col1,col2,col3,col4,col5,col6,col7 = st.columns(col_size_list)
	with col1: st.write('Research')
	with col2: st.write('Ticker from Index')
	with col3: st.write('selectbox')
	with col4: st.write('< dropdown_ticker >')
	with col5: st.write(scope.pages['research']['ticker_list'][0])
	with col6: st.write("< ticker_list['research'] >")
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Components - Multi Ticker Analysis
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

def view_market(scope, col_size_list):
	col1,col2,col3,col4,col5,col6,col7 = st.columns(col_size_list)
	with col1: st.write('Share Market')
	with col2: st.write('Selected Share Market')
	with col3: st.write('selectbox')
	with col4: st.write('< dropdown_markets >')
	with col5: st.write(scope.pages['multi']['market'])
	with col6: st.write('< selected_market >')

def view_industry(scope, col_size_list):
	col1,col2,col3,col4,col5,col6,col7 = st.columns(col_size_list)
	with col1: st.write('Selected Industry')
	with col2: st.write('Selected Industry(s)')
	with col3: st.write('multiselect')
	with col4: st.write('< dropdown_industries >')
	with col5: st.write(scope.pages['multi']['industries'])
	with col6: st.write('< selected_industries >')

def view_tickers(scope, col_size_list):
	col1,col2,col3,col4,col5,col6,col7 = st.columns(col_size_list)
	with col1: st.write('Selected Tickers (Multi)')
	with col2: st.write('Ticker(s) from Index')
	with col3: st.write('multiselect')
	with col4: st.write('< dropdown_tickers >')
	with col5: st.write(scope.pages['multi']['tickers'])
	with col6: st.write("< selected_tickers >")
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Components - Dropdowns
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

def view_dropdowns(scope):
	col1,col2,col3,col4,col5,col6,col7 = st.columns([2,2,2,2,2,2,2])
	
	with col1: 
		st.markdown('##### Page')
		st.markdown('##### Description')
		st.markdown('##### st.Type')
		st.markdown('##### Selection Store In')
		st.markdown('##### Defaults to')
		st.markdown('##### Selector Contents')
	
	with col2:
		st.markdown('##### Multi')
		st.write('Market')
		st.write('selectbox')
		st.markdown( ('##### < dropdown_markets >') )
		st.write('previous selection')
		st.selectbox(label='Add a Market to Ticker List', options=scope.dropdown_markets,	key='91')

	with col3: 
		st.markdown('##### Multi')
		st.write('Industry')
		st.write('dropdown_industries')
		st.markdown( ('##### < dropdown_industries >') )
		st.write('previous selection')
		st.multiselect(label='Add an Industry or Industries', options=scope.dropdown_industries,	key='92')

	with col4: 
		st.markdown('##### Multi')
		st.write('Tickers')
		st.write('multiselect')
		st.markdown( ('##### < dropdown_tickers >') )
		st.write('previous selection')
		st.multiselect(label='Add a Ticker or Tickers', options=scope.dropdown_tickers,	key='93')

	with col5: 
		st.markdown('##### Single')
		st.write('Ticker')
		st.write('selectbox')
		st.markdown( ('##### < dropdown_ticker >') )
		st.write('previous selection')
		st.selectbox(label='Select a Ticker', options=scope.dropdown_ticker,	key='94')

	with col6: 
		st.markdown('##### All')
		st.write('Ticker OHLCV Columns')
		st.write('selectbox')
		st.markdown( ('##### < dropdown_ticker_columns >') )
		st.write('close')
		st.selectbox(label='Select a Column', options=scope.dropdown_ohlcv_columns,	key='95')

	with col7: 
		st.markdown('##### All')
		st.write('Ticker File Columns')
		st.write('selectbox')
		st.markdown( ('##### < dropdown_ticker_columns >') )
		st.write('close')
		st.selectbox(label='Select a Column', options=scope.dropdown_price_columns,	key='96')


# TODO - rob - this was the original report showing all the ticker selectors

# def selected_tickers_for_each_page(scope): # 
# 	st.subheader('Selected Ticker(s) for each Page')

# 	col1,col2 = st.columns([2,10])

# 	with col1: st.markdown('##### Single Ticker Analysis')
# 	with col2: st.write(scope.pages['single']['ticker_list'][0])

# 	with col1: st.markdown('##### Intra Day Analysis')
# 	with col2: st.write(scope.pages['intraday']['ticker_list'][0])

# 	with col1: st.markdown('##### Volume Prediction')
# 	with col2: st.write(scope.pages['volume']['ticker_list'][0])

# 	with col1: st.markdown('##### Research Ticker')
# 	with col2: st.write(scope.pages['research']['ticker_list'][0])

# 	with col1: st.markdown('##### Multi Ticker Analysis List')
# 	ticker_list_message = ''
# 	for count, ticker in enumerate(scope.pages['multi']['ticker_list']):
# 		ticker_list_message = ticker_list_message + ticker
# 		if count < len(scope.pages['multi']['ticker_list']) - 1:
# 			ticker_list_message += '  '

# 	with col2: st.write(ticker_list_message)