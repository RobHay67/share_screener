import streamlit as st
from app.views.widgets.cols_three import three_cols

def show_specific_page_config(scope):

	page = scope.pages['display']

	# st.divider()
	st.write( 'Configuration for ' + page.upper() + ' page')
	three_cols( 'Page Specific Configuration stored in', {}, 'scope.pages['+page+']', widget_type='string' )
	
	# st.caption('Lists and Dictionaries')
	with st.expander("Page Dictionary and Lists", expanded=False):
		three_cols( 'Search Results'  			 , scope.pages[page]['search_results']		, "scope.pages['"+ page +"']['search_results']"    	, widget_type='string' )
		three_cols( 'Worklist - targets for page', scope.pages[page]['worklist']			, "scope.pages['"+ page +"']['worklist']"    		, widget_type='string' )
		three_cols( 'Tickers Loaded Used by Page', scope.pages[page]['loaded_ticker_list']	, "scope.pages['"+ page +"']['loaded_ticker_list"	, widget_type='string' )
	
	with st.expander("Ticker Selectors", expanded=False):
		three_cols( 'Market'  , scope.pages[page]['selectors']['market']    , "scope.pages['"+ page +"']['selectors']['market']"    , widget_type='string' )
		three_cols( 'Industry', scope.pages[page]['selectors']['industries'], "scope.pages['"+ page +"']['selectors']['industries']", widget_type='string' )
		three_cols( 'Tickers' , scope.pages[page]['selectors']['tickers']   , "scope.pages['"+ page +"']['selectors']['tickers']"   , widget_type='string' )
		three_cols( 'Ticker'  , scope.pages[page]['selectors']['ticker']    , "scope.pages['"+ page +"']['selectors']['ticker']"    , widget_type='string' )
	
	with st.expander("Page Show / Hide Options", expanded=False):
		three_cols( 'Show Page Config (this)'	, scope.pages[page]['render']['page_config']    	, "scope.pages['"+ page +"']['render']['page_config']"    , widget_type='string' )
		three_cols( 'Show Chart Settings'  		, scope.pages[page]['render']['chart_settings']    	, "scope.pages['"+ page +"']['render']['chart_settings']"    , widget_type='string' )
		three_cols( 'Show Overlay Settings'  	, scope.pages[page]['render']['overlay_settings']	, "scope.pages['"+ page +"']['render']['overlay_config']"    , widget_type='string' )
		three_cols( 'Show Trial Settings'  		, scope.pages[page]['render']['trial_settings']    	, "scope.pages['"+ page +"']['render']['trial_settings']"    , widget_type='string' )
		three_cols( 'Show Strategies'  			, scope.pages[page]['render']['strategy']    		, "scope.pages['"+ page +"']['render']['strategy']"    , widget_type='string' )
		three_cols( 'Show Ticker DFs'  			, scope.pages[page]['render']['ticker_file']    	, "scope.pages['"+ page +"']['render']['ticker_file']"    , widget_type='string' )

