import streamlit as st

# from system.reports import render_3_columns


def scope_pages(scope):


	# Multi Analysis Page Variables  # TODO - thiese should be in with the misnames ticker_list
	# scope.selected['multi']['market'] 				= 'select entire market'	# for the multi ticker selection screen
	# scope.selected['multi']['industries'] 			= None
	# scope.selected['multi']['tickers'] 				= None


	# Page Specific Variables
	scope.selected={											# TODO - refactor to "selected"
					'multi'		:{'ticker_list':[], 				'market':'select entire market', 'industries':None, 'tickers':None  },
					'single'	:{'ticker_list':['select a ticker']},
					'intraday'	:{'ticker_list':['select a ticker']},
					'volume'	:{'ticker_list':['select a ticker']},
					'research'	:{'ticker_list':['select a ticker']},
					}

def render_pages(scope):
	col_size_list = [1.5, 1.5, 1.0, 2.2, 2.5, 2.5, 0.8]

	col1,col2,col3,col4,col5,col6,col7 = st.columns(col_size_list)

	st.subheader('Single Analysis Pages')
	st.markdown('#### Ticker Selectors')
	render_headings(scope, col_size_list)
	render_single(scope, col_size_list)
	render_intra_day(scope, col_size_list)
	render_volume(scope, col_size_list)
	render_research(scope, col_size_list)
	st.markdown("""---""")


	st.subheader('Multi Analysis Page')
	st.markdown('#### Ticker List Construction Selectors')
	render_headings(scope, col_size_list)
	render_market(scope, col_size_list)
	render_industry(scope, col_size_list)
	render_tickers(scope, col_size_list)
	st.markdown("""---""")
	

	st.subheader('Drop Down Lists (with Contents)')
	render_dropdowns(scope)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Components - Single Ticker Analysis
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

def render_headings(scope, col_size_list):
	col1,col2,col3,col4,col5,col6,col7 = st.columns(col_size_list)
	with col1: st.markdown('##### Selector')
	with col2: st.markdown('##### Contains')
	with col3: st.markdown('##### Widget')
	with col4: st.markdown('##### Populated from')
	with col5: st.markdown('##### Current Selection')
	with col6: st.markdown('##### Selection Stored In')

def render_single(scope, col_size_list):
	col1,col2,col3,col4,col5,col6,col7 = st.columns(col_size_list)
	with col1: st.write('Single Ticker')
	with col2: st.write('Ticker from Index')
	with col3: st.write('selectbox')
	with col4: st.write('< dropdown_ticker >')
	with col5: st.write(scope.selected['single']['ticker_list'][0])
	with col6: st.write("< ticker_list['single'] >")

def render_intra_day(scope, col_size_list):
	col1,col2,col3,col4,col5,col6,col7 = st.columns(col_size_list)
	with col1: st.write('Intra Day')
	with col2: st.write('Ticker from Index')
	with col3: st.write('selectbox')
	with col4: st.write('< dropdown_ticker >')
	with col5: st.write(scope.selected['intraday']['ticker_list'][0])
	with col6: st.write("< ticker_list['intraday'] >")

def render_volume(scope, col_size_list):
	col1,col2,col3,col4,col5,col6,col7 = st.columns(col_size_list)
	with col1: st.write('Volume Prediction')
	with col2: st.write('Ticker from Index')
	with col3: st.write('selectbox')
	with col4: st.write('< dropdown_ticker >')
	with col5: st.write(scope.selected['volume']['ticker_list'][0])
	with col6: st.write("< ticker_list['volume'] >")

def render_research(scope, col_size_list):
	col1,col2,col3,col4,col5,col6,col7 = st.columns(col_size_list)
	with col1: st.write('Research')
	with col2: st.write('Ticker from Index')
	with col3: st.write('selectbox')
	with col4: st.write('< dropdown_ticker >')
	with col5: st.write(scope.selected['research']['ticker_list'][0])
	with col6: st.write("< ticker_list['research'] >")
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Components - Multi Ticker Analysis
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

def render_market(scope, col_size_list):
	col1,col2,col3,col4,col5,col6,col7 = st.columns(col_size_list)
	with col1: st.write('Share Market')
	with col2: st.write('Selected Share Market')
	with col3: st.write('selectbox')
	with col4: st.write('< dropdown_markets >')
	with col5: st.write(scope.selected['multi']['market'])
	with col6: st.write('< selected_market >')

def render_industry(scope, col_size_list):
	col1,col2,col3,col4,col5,col6,col7 = st.columns(col_size_list)
	with col1: st.write('Selected Industry')
	with col2: st.write('Selected Industry(s)')
	with col3: st.write('multiselect')
	with col4: st.write('< dropdown_industries >')
	with col5: st.write(scope.selected['multi']['industries'])
	with col6: st.write('< selected_industries >')

def render_tickers(scope, col_size_list):
	col1,col2,col3,col4,col5,col6,col7 = st.columns(col_size_list)
	with col1: st.write('Selected Tickers (Multi)')
	with col2: st.write('Ticker(s) from Index')
	with col3: st.write('multiselect')
	with col4: st.write('< dropdown_tickers >')
	with col5: st.write(scope.selected['multi']['tickers'])
	with col6: st.write("< selected_tickers >")
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Components - Dropdowns
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

def render_dropdowns(scope):
	col1,col2,col3,col4,col5,col6 = st.columns([2,2,2,2,2,2])
	
	with col1: st.markdown('##### Page')
	with col1: st.markdown('##### Description')
	with col1: st.markdown('##### st.Type')
	with col1: st.markdown('##### Selection Store In')
	with col1: st.markdown('##### Defaults to')
	with col1: st.markdown('##### Selector Contents')
	
	with col2: st.markdown('##### Multi')
	with col2: st.write('Market')
	with col2: st.write('selectbox')
	with col2: st.markdown( ('##### < dropdown_markets >') )
	with col2: st.write('previous selection')
	with col2: st.selectbox(label='Add a Market to Ticker List', options=scope.dropdown_markets,	key='91')

	with col3: st.markdown('##### Multi')
	with col3: st.write('Industry')
	with col3: st.write('dropdown_industries')
	with col3: st.markdown( ('##### < dropdown_industries >') )
	with col3: st.write('previous selection')
	with col3: st.multiselect(label='Add an Industry or Industries', options=scope.dropdown_industries,	key='92')

	with col4: st.markdown('##### Multi')
	with col4: st.write('Tickers')
	with col4: st.write('multiselect')
	with col4: st.markdown( ('##### < dropdown_tickers >') )
	with col4: st.write('previous selection')
	with col4: st.multiselect(label='Add a Ticker or Tickers', options=scope.dropdown_tickers,	key='93')

	with col5: st.markdown('##### Single')
	with col5: st.write('Ticker')
	with col5: st.write('selectbox')
	with col5: st.markdown( ('##### < dropdown_ticker >') )
	with col5: st.write('previous selection')
	with col5: st.selectbox(label='Select a Ticker', options=scope.dropdown_ticker,	key='94')

	with col6: st.markdown('##### All')
	with col6: st.write('Ticker File Column')
	with col6: st.write('selectbox')
	with col6: st.markdown( ('##### < dropdown_ticker_columns >') )
	with col6: st.write('close')
	with col6: st.selectbox(label='Select a Column', options=scope.dropdown_ticker_columns,	key='95')



