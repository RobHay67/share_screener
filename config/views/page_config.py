import streamlit as st
from app.views.widgets.cols_three import three_cols


def show_page_config(scope):
	st.subheader('Page Configuration - Page Settings')
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


