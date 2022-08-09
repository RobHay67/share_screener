import streamlit as st

from progress.three_cols import three_cols


def view_apps(scope):
	st.subheader('Pages Configuration')
	three_cols( 'Row Limit (for App)', scope.apps['row_limit'], 'scope.apps.row_limit' )
	three_cols( 'App to Display (latest)', scope.apps['display_app'], 'scope.apps.display_app' )
	
	st.subheader('Streamlit Re-usable Variables')
	three_cols( 'Streamlit Latest Button Pressed', scope.apps['button_for_scope'], 'scope.apps.button_for_scope' )

	st.subheader('Available Pages')
	three_cols( 'App List', scope.apps['app_list'], 'scope.apps.app_list' )

	# st.markdown("""---""")


def view_single_page(scope):
	view_page_specific_variables(scope, 'single')

def view_intra_day_page(scope):
	view_page_specific_variables(scope, 'intra_day')

def view_volume_page(scope):
	view_page_specific_variables(scope, 'volume')

def view_research_page(scope):
	view_page_specific_variables(scope, 'research')

def view_screener_page(scope):
	view_page_specific_variables(scope, 'screener')


def view_page_specific_variables(scope, app):

	# for App in scope.apps['app_list']:
	st.subheader(app.upper() + ' App')
	three_cols( 'Selected - Market'  , scope.apps[app]['selectors']['market']    , 'scope.apps.'+ app +'.selectors.market'    , widget_type='string' )
	three_cols( 'Selected - Industry', scope.apps[app]['selectors']['industries'], 'scope.apps.'+ app +'.selectors.industries', widget_type='string' )
	three_cols( 'Selected - Tickers' , scope.apps[app]['selectors']['tickers']   , 'scope.apps.'+ app +'.selectors.tickers'   , widget_type='string' )
	three_cols( 'Selected - Ticker'  , scope.apps[app]['selectors']['ticker']    , 'scope.apps.'+ app +'.selectors.ticker'    , widget_type='string' )
	
	three_cols( 'Ticker List'  , scope.apps[app]['ticker_list'], 'scope.apps.'+ app +'.ticker_list'    , widget_type='string' )

	three_cols( 'Status > Replace DataFrames'  , scope.apps[app]['replace_dfs'], 'scope.apps.'+ app +'.replace_dfs'    , widget_type='string' )
	three_cols( 'Status > Replace Columns'  , scope.apps[app]['replace_cols'], 'scope.apps.'+ app +'.replace_cols'    , widget_type='string' )

	three_cols( 'Search Results'  , scope.apps[app]['search_results'], 'scope.apps.'+ app +'.search_results'    , widget_type='string' )
