import streamlit as st
from app.views.widgets.cols_three import three_cols


def show_page_config(scope):
	st.subheader('Page(s)')
	three_cols( 'Page Configuration', {}, 'scope.config', widget_type='string' )
	# st.divider()
	three_cols('Specific Page Config', '{ }', "scope.page[page]")
	# st.caption('navigate to each page and select config button')
	three_cols( 'Current Page to Display', 		scope.config['display'], 			"scope.config['display']" )
	three_cols( 'Config Group (this screen)',	scope.config['display_config_group'],"scope.config.display_config_group", widget_type='string' )
	st.divider()
	three_cols( 'Share Market', 				scope.config['share_market'], 	"scope.config['share_market']" )
	three_cols( 'Row Limit for Page',		 	scope.config['row_limit'], 		"scope.config.row_limit", widget_type='string' )
	three_cols( 'Days to Download (recent)', 	scope.config['download_days'], 	"scope.config['download_days']" )
	st.divider()
	three_cols( 'Page List', 					scope.config['page_list'], 					"scope.config.app_list", widget_type='string' )
	st.divider()
	st.caption('Ticker Selector Dropdowns')
	three_cols( 'Dropdown Configuration stored in', {}, 									"scope.config['dropdowns']", widget_type='string' )
	three_cols( 'Ticker', 						scope.config['dropdowns']['ticker'], 	 	"scope.config['dropdowns']['ticker']", widget_type='selectbox' )
	three_cols( 'Tickers', 						scope.config['dropdowns']['tickers'],  		"scope.config['dropdowns']['tickers']", widget_type='multiselect' )
	three_cols( 'Industry', 					scope.config['dropdowns']['industries'],		"scope.config['dropdowns']['industries']", widget_type='multiselect' )
	three_cols( 'Market', 						scope.config['dropdowns']['markets'], 		"scope.config['dropdowns']['markets']", widget_type='selectbox' )
	st.caption('Column Selectors')
	three_cols( 'OHLCV Columns', 				scope.config['dropdowns']['ohlcv_columns'],  "scope.config['dropdowns']['ohlcv_columns']", widget_type='selectbox' )
	three_cols( 'Price Columns', 				scope.config['dropdowns']['price_columns'],  "scope.config['dropdowns']['price_columns']", widget_type='selectbox' )
	st.divider()
	three_cols( 'Ticker Search (Default List)', scope.config['ticker_search'], "scope.config['ticker_search']" )


def show_specific_page_config(scope):

	page = scope.config['display']

	# st.divider()
	st.subheader( 'Page Configuration > page = ' + page.title() + ' page')
	three_cols( 'Page Specific Configuration stored in', {}, 'scope.page['+page+']', widget_type='string' )
	
	# st.caption('Lists and Dictionaries')
	with st.expander("Page Dictionary and Lists", expanded=False):
		three_cols( 'Search Results'  			 , scope.page[page]['search_results']		, "scope.page['"+ page +"']['search_results']"    	, widget_type='string' )
		three_cols( 'Worklist - targets for page', scope.page[page]['worklist']			, "scope.page['"+ page +"']['worklist']"    		, widget_type='string' )
		three_cols( 'Tickers Loaded Used by Page', scope.page[page]['loaded_ticker_list']	, "scope.page['"+ page +"']['loaded_ticker_list"	, widget_type='string' )
	
	with st.expander("Ticker Selectors", expanded=False):
		three_cols( 'Market'  , scope.page[page]['selectors']['market']    , "scope.page['"+ page +"']['selectors']['market']"    , widget_type='string' )
		three_cols( 'Industry', scope.page[page]['selectors']['industries'], "scope.page['"+ page +"']['selectors']['industries']", widget_type='string' )
		three_cols( 'Tickers' , scope.page[page]['selectors']['tickers']   , "scope.page['"+ page +"']['selectors']['tickers']"   , widget_type='string' )
		three_cols( 'Ticker'  , scope.page[page]['selectors']['ticker']    , "scope.page['"+ page +"']['selectors']['ticker']"    , widget_type='string' )
	
	with st.expander("Page Show / Hide Options", expanded=False):
		three_cols( 'Show Page Config (this)'	, scope.page[page]['render']['page_config']    		, "scope.page['"+ page +"']['render']['page_config']"    , widget_type='string' )
		three_cols( 'Show Chart Settings'  		, scope.page[page]['render']['chart_settings']    	, "scope.page['"+ page +"']['render']['chart_settings']"    , widget_type='string' )
		three_cols( 'Show Overlay Settings'  	, scope.page[page]['render']['overlay_settings']	, "scope.page['"+ page +"']['render']['overlay_config']"    , widget_type='string' )
		three_cols( 'Show Trial Settings'  		, scope.page[page]['render']['trial_settings']    	, "scope.page['"+ page +"']['render']['trial_settings']"    , widget_type='string' )
		three_cols( 'Show Strategies'  			, scope.page[page]['render']['strategy']    		, "scope.page['"+ page +"']['render']['strategy']"    , widget_type='string' )
		three_cols( 'Show Ticker Configuration'	, scope.page[page]['render']['ticker_config']    	, "scope.page['"+ page +"']['render']['ticker_config']"    , widget_type='string' )
		three_cols( 'Show Ticker DFs'  			, scope.page[page]['render']['ticker_file']    		, "scope.page['"+ page +"']['render']['ticker_file']"    , widget_type='string' )

