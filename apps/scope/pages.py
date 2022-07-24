import streamlit as st

from config.results.three_cols import three_cols


def view_pages(scope):
	st.subheader('Pages Configuration')
	three_cols( 'Row Limit (for page)', scope.pages['row_limit'], 'scope.apps.row_limit' )
	three_cols( 'Page to Display (latest)', scope.pages['display_page'], 'scope.apps.display_page' )
	
	st.subheader('Streamlit Re-usable Variables')
	three_cols( 'Streamlit Latest Button Pressed', scope.pages['button_for_scope'], 'scope.apps.button_for_scope' )

	st.subheader('Templates')
	three_cols( 'Chart Template', scope.pages['templates']['charts'], 'scope.apps.templates.charts' )
	three_cols( 'Test Template', scope.pages['templates']['tests'], 'scope.apps.templates.tests' )
	
	st.subheader('Available Pages')
	three_cols( 'Page List', scope.pages['page_list'], 'scope.apps.page_list' )

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


def view_page_specific_variables(scope, page):

	# for page in scope.pages['page_list']:
	st.subheader(page.upper() + ' page')
	three_cols( 'Selected - Market'  , scope.pages[page]['selectors']['market']    , 'scope.apps.'+ page +'.selectors.market'    , widget_type='string' )
	three_cols( 'Selected - Industry', scope.pages[page]['selectors']['industries'], 'scope.apps.'+ page +'.selectors.industries', widget_type='string' )
	three_cols( 'Selected - Tickers' , scope.pages[page]['selectors']['tickers']   , 'scope.apps.'+ page +'.selectors.tickers'   , widget_type='string' )
	three_cols( 'Selected - Ticker'  , scope.pages[page]['selectors']['ticker']    , 'scope.apps.'+ page +'.selectors.ticker'    , widget_type='string' )
	
	three_cols( 'Ticker List'  , scope.pages[page]['ticker_list'], 'scope.apps.'+ page +'.ticker_list'    , widget_type='string' )

	three_cols( 'Status > Replace DataFrames'  , scope.pages[page]['replace_dfs'], 'scope.apps.'+ page +'.replace_dfs'    , widget_type='string' )
	three_cols( 'Status > Replace Columns'  , scope.pages[page]['replace_cols'], 'scope.apps.'+ page +'.replace_cols'    , widget_type='string' )

	three_cols( 'Search Results'  , scope.pages[page]['search_results'], 'scope.apps.'+ page +'.search_results'    , widget_type='string' )
