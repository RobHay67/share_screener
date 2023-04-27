import streamlit as st
from pages.config.three_cols import three_cols


def render_scope_tickers(scope):
	ticker_keys = scope.tickers.keys()

	st.subheader('Tickers Configuration')
	three_cols( 'Tickers Configuration stored in' 		, {}			, "scope.tickers"				, widget_type='string' )
	three_cols( 'Loaded Tickers'						, ticker_keys	, "scope.tickers.keys()"		, widget_type='string' )
	three_cols( 'Page Dataframe and Status Stored in '	, {}			, "scope.tickers[ticker][page]"	, widget_type='string' )


def render_ticker_df(scope):
	page = scope.pages['display']
	# diff_col_size = [2,5,3]

	with st.expander("Ticker Dataframe", expanded=False):
		ticker = render_ticker_selector(scope, page, 'raw')
		if ticker != 'select a ticker':
			three_cols( ticker + ' original / raw df stored in', "{ see below }",  "scope.tickers['"+ticker+"']['df']", widget_type='string' )
			st.dataframe(data=scope.tickers[ticker]['df'], width=None, height=None, use_container_width=True)


def render_page_ticker_df(scope, page):
	with st.expander("Page Ticker Dataframe ( df and extra columns status)", expanded=False):
		ticker = render_ticker_selector(scope, page, 'page')
		if ticker != 'select a ticker':
			three_cols( ticker + ' page df stored in'				, "{ see below }"											,  "scope.tickers['"+ticker+"']["+page+"]['df']"				, widget_type='string' )
			three_cols( 'Replace '+ticker+' df for '+page+' page'	, scope.tickers[ticker][page]['replace_df']		,  "scope.tickers['"+ticker+"']["+page+"]['replace_df']"		, widget_type='string' )
			three_cols( ticker + ' df group (charts or trials)'	 	, scope.tickers[ticker][page]['config_group']	,  "scope.tickers['"+ticker+"']["+page+"]['config_group']"		, widget_type='string' )
			three_cols( 'Replace specific cols on '+ticker+' df ?'	, scope.tickers[ticker][page]['replace_column']	,  "scope.tickers['"+ticker+"']["+page+"]['replace_column']"	, widget_type='string' )
			st.dataframe(data=scope.tickers[ticker][page]['df'], width=None, height=None, use_container_width=True)


def render_ticker_selector(scope, page, type):
	list_of_tickers = list(scope.tickers.keys())
	list_of_tickers.insert(0, 'select a ticker')
	ticker = 'select a ticker'
	widget_key = 'widget_ticker_selector_'+page+'_'+type
	
	col1,col2 = st.columns([3,9]) # ensure dropdown is not super wide
	with col1:
		if len(list_of_tickers) > 1:
			ticker = st.selectbox(
						label		='Select a loaded ticker file', 
						options		=list_of_tickers,
						key			=widget_key,
						)
		else:
			st.write('No Tickers Available')
		
	return ticker

