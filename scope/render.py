
import streamlit as st

from datetime import datetime 





def welcome_page(scope):
	st.title(scope.project_description)
	st.success('Loaded and Ready for Analysis')


# ==============================================================================================================================================================
# Render all Scope Variables
# ==============================================================================================================================================================

def scope_page(scope):
	st.title('Application Parameters')

	button_selectors(scope)

	if st.session_state.st_button != None:
		scope_page = {
			'show_ticker_index'	:ticker_index,
			'show_ticker_files'	:ticker_files,
			'show_industries'	:industries,
			'show_strategy'		:strategy,
			'show_charting'		:charting,
			'show_session'		:session,
			'show_selectors'	:selectors,
			'show_download'		:download,
			'show_results'		:results,
			'show_application'	:application,
			'show_folders'		:folders,
			'show_market'		:market,
			}

		scope_page[st.session_state.st_button](scope)
		
	scope.st_button =  None

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Components
# --------------------------------------------------------------------------------------------------------------------------------------------------------------



def button_selectors(scope):
	col1,col2,col3,col4,col5,col6 = st.columns([2,2,2,2,2,2])

	with col1: st.subheader('Data')
	with col1: st.button('Ticker Index File ( ' + str((len(scope.ticker_index_file))) + ' )', on_click=set_st_button, args=('show_ticker_index', ))
	with col1: st.button('Share Data Files ( ' + str(len(scope.share_data_files.keys())) + ' )', on_click=set_st_button, args=('show_ticker_files', ))
	with col1: st.button('Industries', on_click=set_st_button, args=('show_industries', ))
	
	with col2: st.subheader('Analysis')
	with col2: st.button('Strategy', on_click=set_st_button, args=('show_strategy', ))
	with col2: st.button('Charting', on_click=set_st_button, args=('show_charting', ))

	with col3: st.subheader('Session')
	with col3: st.button('Session', on_click=set_st_button, args=('show_session', ))
	with col3: st.button('Selectors', on_click=set_st_button, args=('show_selectors', ))
	with col3: st.button('Download', on_click=set_st_button, args=('show_download', ))
	with col3: st.button('Results', on_click=set_st_button, args=('show_results', ))

	with col4: st.subheader('System')
	with col4: st.button('Application', on_click=set_st_button, args=('show_application', ))
	with col4: st.button('Folders', on_click=set_st_button, args=('show_folders', ))
	with col4: st.button('Share Market', on_click=set_st_button, args=('show_market', ))



def ticker_index(scope):
	col1,col2 = st.columns([6,2])
	with col1: st.subheader('Ticker Index File')
	with col2: st.write('< ticker_index_file >')
	st.dataframe(scope.ticker_index_file, 2000, 1200)

def ticker_files(scope):
	st.subheader('Loaded Ticker Files')
	render_3_columns( 'Loaded Ticker List', scope.downloaded_loaded_list, 'downloaded_loaded_list' )

	col1,col2 = st.columns([6,2])
	with col1: st.subheader('Loaded and Downloaded share data.')
	with col2: st.write('< share_data_files >')

	list_of_loaded_tickers = list(scope.share_data_files.keys())

	for ticker in list_of_loaded_tickers:
		my_expander = st.expander(label=ticker)
		my_expander.dataframe(scope.share_data_files[ticker], 2000, 2000)

def industries(scope):
	st.subheader('Share Index File contains the following Industries')
	industry_group_count = pd.DataFrame(scope.ticker_index_file['industry_group'].value_counts())
	industry_group_count.index.name = 'Industry'
	industry_group_count.columns =['No of Codes']
	st.dataframe(industry_group_count, 2000, 1200)



def strategy(scope):
	st.subheader('Strategy Parameters')
	# TODO not sure what the final format of some of these objects should be

	render_3_columns( 'Strategy Name', scope.strategy_name, 'strategy_name' )
	render_3_columns( 'Print Header', scope.strategy_print_header, 'strategy_print_header' )

	col1,col2,col3 = st.columns([2,4,2])
	with col1: st.write('Price Columns')
	with col2: st.dataframe(scope.strategy_price_columns, 100, 200)
	with col3: st.write('< strategy_price_columns >')
	
	render_3_columns( 'Print Count', scope.strategy_print_count, 'strategy_print_count' )
	render_3_columns( 'Build Header', scope.strategy_build_header, 'strategy_build_header' )
	render_3_columns( 'Header', scope.strategy_header, 'strategy_header' )
	render_3_columns( 'Print Line', scope.strategy_print_line, 'strategy_print_line' )
	
	col1,col2 = st.columns([6,2])
	with col1: st.write('Json Dicitionary')
	with col2: st.write('< strategy_json_dict >')
	st.write(scope.strategy_json_dict)

	col1,col2 = st.columns([6,2])
	with col1: st.write('Results Dataframe')
	with col2: st.write('< strategy_results >')
	st.dataframe(scope.strategy_results, 2000, 1200)

def charting(scope):
	st.subheader('Charting Parameters')
	render_3_columns( 'Chart Line', scope.chart_lines, 'chart_lines' )
	render_3_columns( 'Chart MACD on Price', scope.chart_macd_on_price, 'chart_macd_on_price' )
	render_3_columns( 'Chart MACD on Volume', scope.chart_macd_on_volume, 'chart_macd_on_volume' )



def session(scope):
	st.subheader('Session Variables')

	render_3_columns( 'Initial Load Description', scope.initial_load, 'initial_load' )
	render_3_columns( 'Current Page to Display', scope.display_page, 'display_page' )
	render_3_columns( 'Current Share Market', scope.share_market, 'share_market' )
	render_3_columns( 'Streamlit Latest Button', scope.st_button, 'st_button' )
	

def selectors(scope):
	st.subheader('Ticker Selectors and Selections')

	render_3_columns( 'Initial Run / load', scope.initial_load, 'initial_load' )
	render_3_columns( 'Do the Dropdown Lists Need Refreshing ?', scope.dropdown_lists_need_updating, 'dropdown_lists_need_updating' )

	st.markdown("""---""")
	st.subheader('Ticker Selectors')
	col1,col2,col3,col4,col5,col6,col7 = st.columns([1.5, 1.5, 1.0, 2.2, 2.5, 2.5, 0.8])

	# Column Headings
	with col1: st.markdown('##### Selector')
	with col2: st.markdown('##### Contains')
	with col3: st.markdown('##### Widget')
	with col4: st.markdown('##### Populated from')
	with col5: st.markdown('##### Current Selection')
	with col6: st.markdown('##### Selection Stored In')

	# Share Market
	with col1: st.write('Share Market')
	with col2: st.write('Target Market')
	with col3: st.write('To Be Config')
	with col4: st.write('**Hard Coded')
	with col5: st.write(scope.share_market)
	with col6: st.write('< share_market >')

	# Research
	with col1: st.write('Research')
	with col2: st.write('Ticker in Index')
	with col3: st.write('selectbox')
	with col4: st.write('< dropdown_ticker >')
	with col5: st.write(scope.ticker_list['research'])
	with col6: st.write("< ticker['research'] >")
	# Volume Prediction
	with col1: st.write('Volume Prediction')
	with col2: st.write('Ticker in Index')
	with col3: st.write('selectbox')
	with col4: st.write('< dropdown_ticker >')
	with col5: st.write(scope.ticker_list['volume'])
	with col6: st.write("< ticker['volume_predict'] >")
	# Intrad-Day Analysis
	with col1: st.write('Intra-Day')
	with col2: st.write('Ticker in Index')
	with col3: st.write('selectbox')
	with col4: st.write('< dropdown_ticker >')
	with col5: st.write(scope.ticker_list['intraday'])
	with col6: st.write("< ticker['intraday'] >")
	# Single Ticker Selector
	with col1: st.write('Single Ticker')
	with col2: st.write('Ticker in Index')
	with col3: st.write('selectbox')
	with col4: st.write('< dropdown_ticker >')
	with col5: st.write(scope.ticker_list['single'])
	with col6: st.write("< ticker['single'] >")
	# Share Market
	with col1: st.write('Share Market')
	with col2: st.write('Share Markets')
	with col3: st.write('selectbox')
	with col4: st.write('< dropdown_markets >')
	with col5: st.write(scope.tickers_market)
	with col6: st.write('< tickers_market >')

	# Industry Selector
	with col1: st.write('Industry')
	with col2: st.write('Industry in Index')
	with col3: st.write('multiselect')
	with col4: st.write('< dropdown_industries >')
	with col5: st.write(scope.tickers_industries)
	with col6: st.write('< tickers_industries >')

	# Share Market
	with col1: st.write('Tickers')
	with col2: st.write('Ticker in Index')
	with col3: st.write('multiselect')
	with col4: st.write('< dropdown_tickers >')
	with col5: st.write(scope.tickers_multi)
	with col6: st.write('< tickers_multi >')

	# Ticker Indicator Column O-H-L-C-V
	with col1: st.write('Ticker Column')
	with col2: st.write('Calculate on col')
	with col3: st.write('multiselect')
	with col4: st.write('< dropdown_ticker_columns >')
	with col5: st.write('  not stored ')
	with col6: st.write('  not stored ')			#TODO - we may need to store this for different indicators 

	
	st.markdown("""---""")
	st.subheader('Dropdown Lists (per above)')
	render_3_columns( 'Share Market  ( selectbox )'  , scope.dropdown_markets		, 'dropdown_markets' )
	render_3_columns( 'Industry      ( multiselect )', scope.dropdown_industries	, 'dropdown_industries' )
	render_3_columns( 'Tickers       ( multiselect )', scope.dropdown_tickers		, 'dropdown_tickers' )
	render_3_columns( 'Ticker        ( selectbox )'  , scope.dropdown_ticker		, 'dropdown_ticker' )
	render_3_columns( 'Ticker Column ( selectbox )'  , scope.dropdown_ticker_columns, 'dropdown_ticker_columns' )

def download(scope):
	st.markdown('##### Download Variables')
	render_3_columns( 'Number of Days to Download', scope.download_days, 'download_days' )

	st.markdown("""---""")
	st.markdown('##### Most Recent Download Variables and Data')
	render_3_columns( 'Industry Groups for y_finance to iterate over', scope.download_industries, 'download_industries' )
	render_3_columns( 'Loaded Ticker List', scope.downloaded_loaded_list, 'downloaded_loaded_list' )
	render_3_columns( 'Missing Ticker List', scope.downloaded_missing_list, 'downloaded_missing_list' )
	render_3_columns( 'Downloaded Data from y_finance', scope.downloaded_yf_ticker_data, 'downloaded_yf_ticker_data' )
	render_3_columns( 'Error Messages  from y_finance', scope.downloaded_yf_anomolies  , 'downloaded_yf_anomolies' )

	st.markdown("""---""")
	st.markdown('##### Most Recent Ticker List which would have been utilised by the above variables')
	render_3_columns( 'Current Ticker List', (str(len(scope.ticker_list)) + ' ticker(s)'), 'ticker_list' )
	ticker_list_message = ''
	for count, ticker in enumerate(scope.ticker_list):
		ticker_list_message = ticker_list_message + ticker
		if count < len(scope.ticker_list) - 1:
			ticker_list_message += '  '
	st.info(ticker_list_message)

	st.markdown("""---""")
	st.subheader('Available Schemas for the different downloads from y_finance')
	col1,col2,col3 = st.columns([2,4,2])
	list_of_schemas = list(scope.download_schemas.keys())
	for schema in list_of_schemas:
		with col1: st.write(schema)
		# schema_definition = scope.download_schemas[schema]
		# schema_definition = pd.DataFrame(scope.download_schemas[schema])
		# print( schema_definition)
		with col2: st.write(scope.download_schemas[schema])
		# with col2: st.dataframe(scope.strategy_price_columns, 100, 200)
		# with col2: st.write(schema_definition)
	with col3: st.write('< download_schemas >')

def results(scope):
	st.subheader('Results from Most Recent Batch Process')
	st.markdown("""---""")
	st.subheader('Result Parameters')
	render_3_columns( 'Result Passed', scope.result_passed, 'result_passed' )
	render_3_columns( 'Result Passed_2', scope.result_passed_2, 'result_passed_2' )
	render_3_columns( 'Result Failed', scope.result_failed, 'result_failed' )



def application(scope):
	st.subheader('General Application Parameters')
	render_3_columns( 'Project Description', scope.project_description, 'project_description' )
	render_3_columns( 'Project Start Time', datetime.fromtimestamp(scope.project_start_time).strftime('%Y-%m-%d %H:%M:%S %p'), 'project_start_time' )
	render_3_columns( 'Current Share Market', scope.share_market, 'share_market' )

def folders(scope):
	st.subheader('Folders and Paths')

	diff_col_size = [2,6,2]

	render_3_columns( 'Project Folder', scope.folder_project, 'folder_project', diff_col_size )
	render_3_columns( 'Share Data Folder', scope.folder_share_data, 'folder_share_data', diff_col_size )
	render_3_columns( 'Results Analysis Folder', scope.folder_results_analysis, 'folder_results_analysis', diff_col_size )
	render_3_columns( 'Website Output Folder', scope.folder_website, 'folder_website', diff_col_size )
	render_3_columns( 'Path for Share Index File', scope.path_ticker_index, 'path_ticker_index', diff_col_size )
	render_3_columns( 'Path for Website Output File', scope.path_website_file, 'path_website_file', diff_col_size )
	render_3_columns( 'Path for Share Data File', scope.path_share_data_file, 'path_share_data_file', diff_col_size )

def market(scope):
	st.subheader('Market Parameters')
	st.info( ('Current Share Market = ' + str(scope.share_market)) )

	render_3_columns( 'Share Market Suffix', scope.market_suffix, 'market_suffix' )
	
	st.markdown("""---""")
	st.subheader('Market Dates - Opening times and Public Holidays')

	render_3_columns( 'Public Holidays', scope.market_public_holidays, 'market_public_holidays' )
	render_3_columns( 'Opening Hours', scope.market_opening_hours, 'market_opening_hours' )


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------------------------------------------------------------------------------------------



def render_3_columns( description, variable, variable_name, diff_col_size=None ):
	if diff_col_size == None:
		col1,col2,col3 = st.columns([2,4,2])
	else:
		col1,col2,col3 = st.columns(diff_col_size)
	
	with col1: st.write(description)
	with col2: st.write(variable)
	with col3: st.write( ('< ' + variable_name + ' >') )

def set_st_button(button:str):
	print( 'Selected Button > ', button)
	st.session_state.st_button = button


