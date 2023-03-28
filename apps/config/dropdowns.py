import streamlit as st
from apps.config.three_cols import three_cols


def scope_dropdown_menus(scope):
	# Dropdowns
	scope.config['dropdowns'] = {}
	scope.config['dropdowns']['markets'] = []
	scope.config['dropdowns']['industries'] = []
	scope.config['dropdowns']['tickers'] = []
	scope.config['dropdowns']['ticker'] = []
	scope.config['dropdowns']['ohlcv_columns'] 	= ['open', 'high', 'low', 'close', 'volume']
	scope.config['dropdowns']['price_columns'] = ['open', 'high', 'low', 'close' 		   ]	



def view_dropdowns(scope):

	st.subheader('Dropdown Configuration')
	three_cols( 'Dropdown Configuration stored in', {}, "scope.config['dropdowns']", widget_type='string' )

	st.subheader('Dropdowns')
	three_cols( 'Ticker', scope.config['dropdowns']['ticker'],  "scope.config['ticker']", widget_type='selectbox' )
	three_cols( 'Tickers', scope.config['dropdowns']['tickers'],  "scope.config['tickers']", widget_type='multiselect' )
	three_cols( 'Industry', scope.config['dropdowns']['industries'],  "scope.config['industries']", widget_type='multiselect' )
	three_cols( 'Market', scope.config['dropdowns']['markets'], "scope.config['markets']", widget_type='selectbox' )

	three_cols( 'OHLCV Columns', scope.config['dropdowns']['ohlcv_columns'],  "scope.config['ohlcv_columns']", widget_type='selectbox' )
	three_cols( 'Price Columns', scope.config['dropdowns']['price_columns'],  "scope.config['price_columns']", widget_type='selectbox' )



