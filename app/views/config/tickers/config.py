import streamlit as st
from app.views.widgets.cols_three import three_cols
# from app.views.header.b_pge_config.ticker_config import select_a_ticker_for_config


def show_ticker_general_config(scope):
	ticker_keys = scope.tickers.keys()
	st.subheader('Tickers')
	three_cols( 'Tickers Configuration stored in' 		, {}			, "scope.tickers"							, widget_type='string' )
	three_cols( 'Loaded Tickers > scope.tickers[CBA.AX]', ticker_keys	, "scope.tickers.keys()"					, widget_type='string' )
	st.divider()
	three_cols( 'Page Dataframe and Status Stored in '	, {}			, "scope.tickers[ticker][page]"				, widget_type='string' )
	st.write(':red[TODO I want to be able to select one of tickers to get to the raw data]')


def show_ticker_page_config(scope):
	page = scope.pages['display']
	ticker_keys = list(scope.tickers.keys())
	st.subheader('Ticker Page Configuration')

	three_cols( 'Show original Ticker DF + Page Ticker DF with added columns', scope.pages[page]['render']['ticker_file']    	, "scope.pages['"+ page +"']['render']['ticker_file']"    , widget_type='string' )
	if len(ticker_keys)>0:
		for ticker in ticker_keys:
			st.divider()
			three_cols( 'Page Dataframe Information '	, {}													, "scope.tickers["+ticker+"]["+page+"]"				, widget_type='string' )
			three_cols( 'Page Dataframes'						, ticker										, "scope.tickers["+ticker+"]["+page+"][df]"			, widget_type='string' )
			three_cols( 'Page Configuration Group'				, scope.tickers[ticker][page]['config_group']	, "scope.tickers["+ticker+"]["+page+"][config_group]"			, widget_type='string' )
			three_cols( 'Replace Dataframe ?'					, scope.tickers[ticker][page]['replace_df']		, "scope.tickers["+ticker+"]["+page+"][replace_df]"	, widget_type='string' )
			three_cols( 'Replace Dataframe Columns ?'			, scope.tickers[ticker][page]['replace_column']	, "scope.tickers["+ticker+"]["+page+"]][replace_column]"			, widget_type='string' )
		else:
			st.write('No Ticker Information. Load or Download some data')









# TODO - do we want to enable the ticker frame ?
def render_page_ticker_df(scope, page):
	with st.expander("Page Ticker Dataframe ( df and extra columns status)", expanded=False):
		# select_a_ticker_for_config(scope, page, 'page')
		ticker = scope.pages[page]['selectors']['config_ticker']
		st.write(ticker)
		# if ticker != 'select a ticker':
		# 	three_cols( ticker + ' page df stored in'				, "{ see below }"											,  "scope.tickers['"+ticker+"']["+page+"]['df']"				, widget_type='string' )
		# 	three_cols( 'Replace '+ticker+' df for '+page+' page'	, scope.tickers[ticker][page]['replace_df']		,  "scope.tickers['"+ticker+"']["+page+"]['replace_df']"		, widget_type='string' )
		# 	three_cols( ticker + ' df group (charts or trials)'	 	, scope.tickers[ticker][page]['config_group']	,  "scope.tickers['"+ticker+"']["+page+"]['config_group']"		, widget_type='string' )
		# 	three_cols( 'Replace specific cols on '+ticker+' df ?'	, scope.tickers[ticker][page]['replace_column']	,  "scope.tickers['"+ticker+"']["+page+"]['replace_column']"	, widget_type='string' )
		# 	st.dataframe(data=scope.tickers[ticker][page]['df'], width=None, height=None, use_container_width=True)






