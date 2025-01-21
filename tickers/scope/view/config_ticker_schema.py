from app.views.widgets.cols_three import three_cols
import streamlit as st
from app.scope.views.buttons.button_choose_scope import scope_button
from app.scope.views.buttons.button_data_type import data_type_button
from app.scope.views.buttons.show_scope_value import show_scope_single_value, show_scope_values
from app.scope.views.buttons.dropdown_choose_scope import scope_dropdown

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



def show_scope_ticker_schema(scope):

	# col1,col2,col3,col4,col5,col6,col7,col8 = st.columns(8)

	st.subheader('Ticker Configuration')
	three_cols( 'Ticker Configuration stored in', {}, "scope.ticker_schema", widget_type='string' )
	st.divider()

	st.subheader('Ticker Schema Config (and shortcut column lists)')
	three_cols( 'Schema', scope.ticker_schema['schema'], "scope.ticker_schema['schema']" )
	three_cols( 'Use Columns', scope.ticker_schema['usecols'], "scope.ticker_schema['usecols']" )
	three_cols( 'Dtypes', scope.ticker_schema['dtypes'], "scope.ticker_schema['dtypes']" )
	three_cols( 'Date Columns', scope.ticker_schema['dates'], "scope.ticker_schema['dates']" )

	st.divider()
	st.subheader('Missing Tickers Configuration')
	st.caption('Missing Lists')
	three_cols( 'Local', 		scope.ticker_schema['missing']['local'], "scope.ticker_schema['missing']['local']" )
	three_cols( 'Cloud', 		scope.ticker_schema['missing']['cloud'], "scope.ticker_schema['missing']['cloud']" )
	three_cols( 'Complete List', scope.ticker_schema['missing']['list'], "scope.ticker_schema['missing']['list']" )
	st.divider()
	st.caption('Ticker Missing Errors')
	three_cols( 'Missing Ticker Error Messages', scope.ticker_schema['missing']['errors'], "scope.ticker_schema['missing']['errors']" )

	














