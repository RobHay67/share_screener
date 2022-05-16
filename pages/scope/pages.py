import streamlit as st

from config.results.three_cols import three_cols


def view_pages(scope):
	st.subheader('Pages Configuration')
	three_cols( 'Row Limit (for page)', scope.pages['row_limit'], 'scope.pages.row_limit' )
	three_cols( 'Page to Display (latest)', scope.pages['display_page'], 'scope.pages.display_page' )
	
	st.subheader('Streamlit Re-usable Variables')
	three_cols( 'Streamlit Latest Button Pressed', scope.pages['button_for_scope'], 'scope.pages.button_for_scope' )

	st.subheader('Templates')
	three_cols( 'Chart Template', scope.pages['templates']['charts'], 'scope.pages.templates.charts' )
	three_cols( 'Test Template', scope.pages['templates']['tests'], 'scope.pages.templates.tests' )
	
	st.subheader('Available Pages')
	three_cols( 'Page List', scope.pages['page_list'], 'scope.pages.page_list' )

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
	three_cols( 'Selected - Market'  , scope.pages[page]['selectors']['market']    , 'scope.pages.'+ page +'.selectors.market'    , widget_type='string' )
	three_cols( 'Selected - Industry', scope.pages[page]['selectors']['industries'], 'scope.pages.'+ page +'.selectors.industries', widget_type='string' )
	three_cols( 'Selected - Tickers' , scope.pages[page]['selectors']['tickers']   , 'scope.pages.'+ page +'.selectors.tickers'   , widget_type='string' )
	three_cols( 'Selected - Ticker'  , scope.pages[page]['selectors']['ticker']    , 'scope.pages.'+ page +'.selectors.ticker'    , widget_type='string' )
	
	three_cols( 'Ticker List'  , scope.pages[page]['ticker_list'], 'scope.pages.'+ page +'.ticker_list'    , widget_type='string' )

	three_cols( 'Status > Replace DataFrames'  , scope.pages[page]['replace_dfs'], 'scope.pages.'+ page +'.replace_dfs'    , widget_type='string' )
	three_cols( 'Status > Replace Columns'  , scope.pages[page]['replace_cols'], 'scope.pages.'+ page +'.replace_cols'    , widget_type='string' )

	three_cols( 'Search Results'  , scope.pages[page]['search_results'], 'scope.pages.'+ page +'.search_results'    , widget_type='string' )
