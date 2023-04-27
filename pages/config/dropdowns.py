import streamlit as st
from pages.config.three_cols import three_cols



def view_dropdowns(scope):

	st.subheader('Dropdown Configuration')
	three_cols( 'Dropdown Configuration stored in', {}, "scope.pages['dropdowns']", widget_type='string' )

	st.divider()
	st.caption('Ticker Selector Dropdowns')
	three_cols( 'Ticker', scope.pages['dropdowns']['ticker'],  "scope.pages['dropdowns']['ticker']", widget_type='selectbox' )
	three_cols( 'Tickers', scope.pages['dropdowns']['tickers'],  "scope.config['dropdowns']['tickers']", widget_type='multiselect' )
	three_cols( 'Industry', scope.pages['dropdowns']['industries'],  "scope.config['dropdowns']['industries']", widget_type='multiselect' )
	three_cols( 'Market', scope.pages['dropdowns']['markets'], "scope.config['dropdowns']['markets']", widget_type='selectbox' )

	st.divider()
	st.caption('Ticker Selector in Config')
	three_cols( 'Ticker (for Config)', scope.pages['dropdowns']['config_ticker'],  "scope.pages['dropdowns']['config_ticker']", widget_type='selectbox' )

	st.divider()
	st.caption('Column Selectors')
	three_cols( 'OHLCV Columns', scope.pages['dropdowns']['ohlcv_columns'],  "scope.config['dropdowns']['ohlcv_columns']", widget_type='selectbox' )
	three_cols( 'Price Columns', scope.pages['dropdowns']['price_columns'],  "scope.config['dropdowns']['price_columns']", widget_type='selectbox' )



