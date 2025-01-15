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

	three_cols( 'Show original Ticker DF + Page Ticker DF with added columns', scope.page[page]['render']['ticker_file']    	, "scope.page['"+ page +"']['render']['ticker_file']"    , widget_type='string' )
	if len(ticker_keys)>0:
		for ticker in ticker_keys:
			print(ticker)
			st.divider()
			three_cols( 'Page Dataframe Information '	, {}													, "scope.tickers["+ticker+"]["+page+"]"					, widget_type='string' )
			three_cols( 'Page Dataframes'						, ticker										, "scope.tickers["+ticker+"]["+page+"][df]"				, widget_type='string' )
			three_cols( 'Page Configuration Group'				, scope.tickers[ticker][page]['schema_group']	, "scope.tickers["+ticker+"]["+page+"][schema_group]"	, widget_type='string' )
			three_cols( 'Replace Dataframe ?'					, scope.tickers[ticker][page]['replace_df']		, "scope.tickers["+ticker+"]["+page+"][replace_df]"		, widget_type='string' )
			three_cols( 'Replace Dataframe Columns ?'			, scope.tickers[ticker][page]['replace_column']	, "scope.tickers["+ticker+"]["+page+"]][replace_column]", widget_type='string' )
		else:
			st.write('No Ticker Information. Load or Download some data')


def show_ticker_config(scope):

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
	three_cols( 'Local', scope.ticker_config['missing']['local'], "scope.ticker_config['missing']['local']" )
	three_cols( 'Cloud', scope.ticker_config['missing']['cloud'], "scope.ticker_config['missing']['cloud']" )
	three_cols( 'Complete List', scope.ticker_config['missing']['list'], "scope.ticker_config['missing']['list']" )
	st.divider()
	st.caption('Ticker Missing Errors')
	three_cols( 'Missing Ticker Error Messages', scope.ticker_config['missing']['errors'], "scope.ticker_config['missing']['errors']" )

	














