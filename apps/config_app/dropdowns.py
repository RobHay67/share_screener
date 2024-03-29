import streamlit as st
from apps.config_app.three_cols import three_cols


def view_dropdowns(scope):
	
	three_cols( 'Market', scope.config['dropdowns']['markets'], 'markets', widget_type='selectbox' )
	three_cols( 'Industry', scope.config['dropdowns']['industries'], 'industries', widget_type='multiselect' )
	three_cols( 'Tickers', scope.config['dropdowns']['tickers'], 'tickers', widget_type='multiselect' )
	three_cols( 'Ticker', scope.config['dropdowns']['ticker'], 'ticker', widget_type='selectbox' )

	three_cols( 'OHLCV Columns', scope.config['dropdowns']['ohlcv_columns'], 'ohlcv_columns', widget_type='selectbox' )
	three_cols( 'Price Columns', scope.config['dropdowns']['price_columns'], 'price_columns', widget_type='selectbox' )



