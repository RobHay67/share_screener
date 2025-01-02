import streamlit as st
from app.views.widgets.cols_three import three_cols


def show_page_config(scope):
	st.subheader('Page(s)')
	three_cols( 'Page Configuration stored in', {}, 'scope.pages', widget_type='string' )
	# st.divider()
	three_cols('Specific Page Config', '{ }', "scope.pages[page]")
	# st.caption('navigate to each page and select config button')
	three_cols( 'Current Page to Display', 		scope.pages['display'], 		"scope.pages['display']" )
	three_cols( 'Show Config (this screen)',	scope.pages['render_config'], 	"scope.pages.render_config", widget_type='string' )
	st.divider()
	three_cols( 'Share Market', 				scope.pages['share_market'], 	"scope.pages['share_market']" )
	three_cols( 'Row Limit for Page',		 	scope.pages['row_limit'], 		"scope.pages.row_limit", widget_type='string' )
	three_cols( 'Days to Download (recent)', 	scope.pages['download_days'], 	"scope.pages['download_days']" )
	st.divider()
	three_cols( 'Page List', 					scope.pages['page_list'], 					"scope.pages.app_list", widget_type='string' )
	st.divider()
	st.caption('Ticker Selector Dropdowns')
	three_cols( 'Dropdown Configuration stored in', {}, 									"scope.pages['dropdowns']", widget_type='string' )
	three_cols( 'Ticker', 						scope.pages['dropdowns']['ticker'], 	 	"scope.pages['dropdowns']['ticker']", widget_type='selectbox' )
	three_cols( 'Tickers', 						scope.pages['dropdowns']['tickers'],  		"scope.pages['dropdowns']['tickers']", widget_type='multiselect' )
	three_cols( 'Industry', 					scope.pages['dropdowns']['industries'],		"scope.pages['dropdowns']['industries']", widget_type='multiselect' )
	three_cols( 'Market', 						scope.pages['dropdowns']['markets'], 		"scope.config['dropdowns']['markets']", widget_type='selectbox' )
	st.caption('Column Selectors')
	three_cols( 'OHLCV Columns', 				scope.pages['dropdowns']['ohlcv_columns'],  "scope.pages['dropdowns']['ohlcv_columns']", widget_type='selectbox' )
	three_cols( 'Price Columns', 				scope.pages['dropdowns']['price_columns'],  "scope.pages['dropdowns']['price_columns']", widget_type='selectbox' )
	st.divider()
	three_cols( 'Ticker Search (Default List)', scope.pages['ticker_search'], "scope.pages['ticker_search']" )


def show_specific_page_config(scope):

	page = scope.pages['display']

	# st.divider()
	st.subheader( 'Configuration for ' + page.title() + ' page')
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

