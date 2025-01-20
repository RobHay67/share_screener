import streamlit as st
from app.views.widgets.cols_three import three_cols


def show_ticker_general_config(scope):

	

	



	ticker_keys = scope.tickers.keys()
	st.subheader('Tickers')
	three_cols( 'Tickers Configuration stored in' 		, {}			, "scope.tickers"							, widget_type='string' )
	three_cols( 'Loaded Tickers > scope.tickers[CBA.AX]', ticker_keys	, "scope.tickers.keys()"					, widget_type='string' )
	st.divider()
	three_cols( 'Page Dataframe and Status Stored in '	, {}			, "scope.tickers[ticker][page]"				, widget_type='string' )


def show_ticker_page_config(scope):
	page = scope.config['display']
	ticker_keys = list(scope.tickers.keys())
	st.subheader('Ticker Page Configuration')
	
	if len(ticker_keys)>0:
		for ticker in ticker_keys:
			print(ticker)
			st.divider()
			three_cols( 'Page Dataframe Management (Tickers) '	, {}											, "scope.tickers["+ticker+"]["+page+"]"					, widget_type='string' )
			three_cols( 'Page Dataframes (Raw)'					, ticker										, "scope.tickers["+ticker+"][df]"						, widget_type='string' )
			three_cols( 'Page Dataframes (added Columns)'		, ticker										, "scope.tickers["+ticker+"]["+page+"][df]"				, widget_type='string' )
			three_cols( 'Page Configuration Group'				, scope.tickers[ticker][page]['schema_group']	, "scope.tickers["+ticker+"]["+page+"][schema_group]"	, widget_type='string' )
			three_cols( 'Replace Dataframe ?'					, scope.tickers[ticker][page]['replace_df']		, "scope.tickers["+ticker+"]["+page+"][replace_df]"		, widget_type='string' )
			three_cols( 'Replace Dataframe Columns ?'			, scope.tickers[ticker][page]['replace_column']	, "scope.tickers["+ticker+"]["+page+"]][replace_column]", widget_type='string' )
		else:
			st.write('No Ticker Information. Load or Download some data')


def show_ticker_config(scope):
	
	st.divider()
	st.button('scope.tickers', use_container_width=True, type="primary", key='widget_config_tickers')
	st.button('[ticker] i.e. ANZ.AX', use_container_width=True, type="secondary", key='widget_config_tickers_ticker')
	col1,col2 = st.columns([1,7])
	with col1:st.button('[df]', 				key='widget_config_tickers_df', use_container_width=True, type="secondary")
	with col2:st.button('[page] i.e. charts', key='widget_config_tickers_page', use_container_width=True, type="secondary")

	col1,col2,col3,col4,col5,col6,col7,col8 = st.columns(8)
	with col1:st.button(' ', 	key='widget_config_empty_button', 		use_container_width=True, type="secondary")
	with col2:st.button('[df]', key='widget_config_tickers_page_df', 	use_container_width=True, type="secondary")
	with col3:st.button('[schema_group]', key='widget_config_tickers_page_schema_group', 	use_container_width=True, type="secondary")
	with col4:st.button('[replace_df]', key='widget_config_tickers_page_replace_df', 	use_container_width=True, type="secondary")
	with col5:st.button('[replace_column]', key='widget_config_tickers_page_replace_column', 	use_container_width=True, type="secondary")
	with col6:st.button('[verdict]', key='widget_config_tickers_page_verdict', 	use_container_width=True, type="secondary")
	with col7:st.button('[replace_verdict]', key='widget_config_tickers_page_replace_verdict', 	use_container_width=True, type="secondary")
	with col8:st.button('[trials]', key='widget_config_tickers_page_trials', 	use_container_width=True, type="secondary")

	col1,col2,col3,col4,col5,col6,col7,col8 = st.columns(8)
	with col1:st.button('{ }', key='widget_config_empty_dictionary', 	use_container_width=True, type="secondary")
	with col4:st.button(':blue[True or False]', key='widget_config_boolean', 	use_container_width=True, type="secondary")
	with col5:st.button(':blue[None]', key='widget_config_none', 	use_container_width=True, type="secondary")

	st.write(':red[So when you click on an object we render the contents]')
	st.divider()


	st.write('[ ticker ] :orange[ie ANZ.AX]')
	col1,col2 = st.columns([6.0, 6.0])
	with col1:st.write('[ df ]')
	with col2:st.write('[ page ] :orange[ie charts]')


	# col1,col2,col3,col4,col5,col6,col7,col8 = st.columns(8)

	st.subheader('Ticker Configuration')
	three_cols( 'Ticker Configuration stored in', {}, "scope.ticker_config", widget_type='string' )
	st.divider()

	st.subheader('Ticker Schema Config (and shortcut column lists)')
	three_cols( 'Schema', scope.ticker_config['schema'], "scope.ticker_config['schema']" )
	three_cols( 'Use Columns', scope.ticker_config['usecols'], "scope.ticker_config['usecols']" )
	three_cols( 'Dtypes', scope.ticker_config['dtypes'], "scope.ticker_config['dtypes']" )
	three_cols( 'Date Columns', scope.ticker_config['dates'], "scope.ticker_config['dates']" )

	st.divider()
	st.subheader('Missing Tickers Configuration')
	st.caption('Missing Lists')
	three_cols( 'Local', 		scope.ticker_config['missing']['local'], "scope.ticker_config['missing']['local']" )
	three_cols( 'Cloud', 		scope.ticker_config['missing']['cloud'], "scope.ticker_config['missing']['cloud']" )
	three_cols( 'Complete List', scope.ticker_config['missing']['list'], "scope.ticker_config['missing']['list']" )
	st.divider()
	st.caption('Ticker Missing Errors')
	three_cols( 'Missing Ticker Error Messages', scope.ticker_config['missing']['errors'], "scope.ticker_config['missing']['errors']" )

	














