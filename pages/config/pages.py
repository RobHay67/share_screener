import streamlit as st

from pages.config.three_cols import three_cols
from pages.config.charts import render_scope_charts
from pages.config.trials import render_trials_config
from pages.config.ticker_data import render_ticker_df, render_page_ticker_df


def view_page_global_config(scope):

	st.subheader('Page Configuration - Global Page Settings')
	three_cols( 'Page Configuration stored in', {}, 'scope.pages', widget_type='string' )
	
	st.divider()
	three_cols( 'Current Page to Display', scope.pages['display'], "scope.pages['display']" )
	st.divider()
	three_cols( 'Share Market', scope.pages['share_market'], "scope.pages['share_market']" )
	three_cols( 'Row Limit for Page', scope.pages['row_limit'], 'scope.pages.row_limit', widget_type='string' )
	three_cols( 'Days to Download (recent)', scope.pages['download_days'], "scope.pages['download_days']" )
	st.divider()
	three_cols( 'Streamlit Latest Button Pressed', scope.pages['button_for_scope'], 'scope.pages.button_for_scope' )
	three_cols( 'Page List', scope.pages['page_list'], 'scope.pages.app_list', widget_type='string' )

	st.divider()
	three_cols('Specific Page Config', '{}', "scope.pages[page]")
	st.caption('navigate to each page and select config button)')



def render_page_config(scope):

	page = scope.pages['display']

	st.divider()
	st.subheader( 'Configuration for ' + page.upper() + ' page')
	three_cols( 'Page Specific Configuration stored in', {}, 'scope.pages['+page+']', widget_type='string' )
	
	# st.caption('Lists and Dictionaries')
	with st.expander("Page Dictionary and Lists", expanded=False):
		three_cols( 'Search Results'  			 , scope.pages[page]['search_results']		, "scope.pages['"+ page +"']['search_results']"    , widget_type='string' )
		three_cols( 'Worklist - targets for page', scope.pages[page]['worklist']			, "scope.pages['"+ page +"']['worklist']"    , widget_type='string' )
		three_cols( 'Tickers Used by Page'   	 , scope.pages[page]['tickers_used_by_page'], "scope.pages['"+ page +"']['tickers_used_by_page", widget_type='string' )
	
	# st.caption('Selectors')
	with st.expander("Ticker Selectors", expanded=False):
		three_cols( 'Market'  , scope.pages[page]['selectors']['market']    , "scope.pages['"+ page +"']['selectors']['market']"    , widget_type='string' )
		three_cols( 'Industry', scope.pages[page]['selectors']['industries'], "scope.pages['"+ page +"']['selectors']['industries']", widget_type='string' )
		three_cols( 'Tickers' , scope.pages[page]['selectors']['tickers']   , "scope.pages['"+ page +"']['selectors']['tickers']"   , widget_type='string' )
		three_cols( 'Ticker'  , scope.pages[page]['selectors']['ticker']    , "scope.pages['"+ page +"']['selectors']['ticker']"    , widget_type='string' )
	
	with st.expander("Page Render Options", expanded=False):
		three_cols( 'Show Ticker DFs'  			, scope.pages[page]['render']['ticker_file']    	, "scope.pages['"+ page +"']['render']['ticker_file']"    , widget_type='string' )
		three_cols( 'Show Chart Settings'  		, scope.pages[page]['render']['chart_settings']    	, "scope.pages['"+ page +"']['render']['chart_settings']"    , widget_type='string' )
		three_cols( 'Show Overlay Settings'  	, scope.pages[page]['render']['overlay_settings']	, "scope.pages['"+ page +"']['render']['overlay_config']"    , widget_type='string' )
		three_cols( 'Show Trial Settings'  		, scope.pages[page]['render']['trial_settings']    	, "scope.pages['"+ page +"']['render']['trial_settings']"    , widget_type='string' )
		three_cols( 'Show Strategies'  			, scope.pages[page]['render']['strategy']    		, "scope.pages['"+ page +"']['render']['strategy']"    , widget_type='string' )
		three_cols( 'Show page Config (this)'	, scope.pages[page]['render']['app_config']    		, "scope.pages['"+ page +"']['render']['app_config']"    , widget_type='string' )

	
	if page == 'screener':render_trials_config(scope)
	if page == 'chart':render_scope_charts(scope)

	render_ticker_df(scope)
	render_page_ticker_df(scope, page)

	st.divider()



