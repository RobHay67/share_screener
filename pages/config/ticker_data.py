import streamlit as st
from pages.config.three_cols import three_cols
from pages.header.widgets.ticker import select_a_ticker_for_config

def render_scope_tickers(scope):
	ticker_keys = scope.tickers.keys()

	st.subheader('Tickers Configuration')
	three_cols( 'Tickers Configuration stored in' 		, {}			, "scope.tickers"				, widget_type='string' )
	three_cols( 'Loaded Tickers'						, ticker_keys	, "scope.tickers.keys()"		, widget_type='string' )
	three_cols( 'Page Dataframe and Status Stored in '	, {}			, "scope.tickers[ticker][page]"	, widget_type='string' )


def render_ticker_df(scope):
	page = scope.pages['display']
	ticker_keys = scope.tickers.keys()

	with st.expander("Ticker Dataframe", expanded=False):
		three_cols( 'Loaded Tickers'						, ticker_keys	, "scope.tickers.keys()"		, widget_type='string' )
		select_a_ticker_for_config(scope, page, 'raw')

		ticker = scope.pages[page]['selectors']['config_ticker']
		if ticker != 'select a ticker':
			three_cols( ticker + ' original / raw df stored in', "{ see below }",  "scope.tickers['"+ticker+"']['df']", widget_type='string' )
			st.dataframe(data=scope.tickers[ticker]['df'], width=None, height=None, use_container_width=True)


def render_page_ticker_df(scope, page):
	with st.expander("Page Ticker Dataframe ( df and extra columns status)", expanded=False):
		select_a_ticker_for_config(scope, page, 'page')

		ticker = scope.pages[page]['selectors']['config_ticker']

		if ticker != 'select a ticker':
			three_cols( ticker + ' page df stored in'				, "{ see below }"											,  "scope.tickers['"+ticker+"']["+page+"]['df']"				, widget_type='string' )
			three_cols( 'Replace '+ticker+' df for '+page+' page'	, scope.tickers[ticker][page]['replace_df']		,  "scope.tickers['"+ticker+"']["+page+"]['replace_df']"		, widget_type='string' )
			three_cols( ticker + ' df group (charts or trials)'	 	, scope.tickers[ticker][page]['config_group']	,  "scope.tickers['"+ticker+"']["+page+"]['config_group']"		, widget_type='string' )
			three_cols( 'Replace specific cols on '+ticker+' df ?'	, scope.tickers[ticker][page]['replace_column']	,  "scope.tickers['"+ticker+"']["+page+"]['replace_column']"	, widget_type='string' )
			st.dataframe(data=scope.tickers[ticker][page]['df'], width=None, height=None, use_container_width=True)




