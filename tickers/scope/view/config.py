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


def build_ticker_list(scope):
	ticker_list = scope.tickers.keys()
	return ticker_list


def show_scope_tickers(scope):
	scope_button(scope, "scope.tickers", scope.tickers, make_red=True, suffix_only=False)
	scope_button(scope, "[ticker] i.e. ANZ.AX", scope.tickers, make_red=False, suffix_only=False)
	
	ticker = scope_dropdown(scope, build_ticker_list(scope))

	col1,col2 = st.columns([1,4])
	with col1:scope_button(scope, "scope.tickers["+ticker+"]['df']", scope.tickers[ticker]['df'])
	with col2:scope_button(scope, "scope.tickers["+ticker+"]['page']", scope.config['page_list'])
	with col2:page = scope_dropdown(scope, scope.config['page_list'])


	col1,col2,col3,col4,col5 = st.columns([1,1,1,1,1])
	with col2:scope_button(scope, "scope.tickers["+ticker+"]["+page+"][df]", scope.tickers[ticker][page]['df'])
	with col3:scope_button(scope, "scope.tickers["+ticker+"]["+page+"][replace_df]", scope.tickers[ticker][page]['replace_df'])
	with col4:scope_button(scope, "scope.tickers["+ticker+"]["+page+"][replace_column]", scope.tickers[ticker][page]['replace_column'])
	with col5:scope_button(scope, "scope.tickers["+ticker+"]["+page+"][schema_group]", scope.tickers[ticker][page]['schema_group'])

	col1,col2,col3,col4,col5 = st.columns([1,1,1,1,1])
	with col4:show_scope_single_value("replace_df", scope.tickers[ticker][page]['replace_df'])
	with col5:show_scope_single_value("schema_group", scope.tickers[ticker][page]['schema_group'])

	st.divider()
	if scope.config['display_scope']['scope_key'] != None:
		show_scope_values(scope)







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

	














