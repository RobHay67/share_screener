import streamlit as st
from app.views.widgets.cols_three import three_cols
from app.views.header.b_config.ticker_config import select_a_ticker_for_config


def show_ticker_config(scope):
	ticker_keys = scope.tickers.keys()
	st.subheader('Tickers Configuration')
	three_cols( 'Tickers Configuration stored in' 		, {}			, "scope.tickers"				, widget_type='string' )
	three_cols( 'Loaded Tickers'						, ticker_keys	, "scope.tickers.keys()"		, widget_type='string' )
	three_cols( 'Page Dataframe and Status Stored in '	, {}			, "scope.tickers[ticker][page]"	, widget_type='string' )


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


def show_missing_ticker_config(scope):
	st.subheader('Missing Tickers Configuration')
	three_cols( 'Missing Tickers Configuration stored in', {}, "scope.tickers_missing", widget_type='string' )
	st.divider()
	st.caption('Missing Lists')
	three_cols( 'Local', scope.tickers_missing['local'], "scope.tickers_missing['local']" )
	three_cols( 'Cloud', scope.tickers_missing['cloud'], "scope.tickers_missing['cloud']" )
	three_cols( 'Complete List', scope.tickers_missing['list'], "scope.tickers_missing['list']" )
	st.divider()
	st.caption('Ticker Missing Errors')
	three_cols( 'Missing Ticker Error Messages', scope.tickers_missing['errors'], "scope.tickers_missing['errors']" )

	



