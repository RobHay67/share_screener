import streamlit as st


def scope_tickers(scope):
	scope.ticker_data_files = {}


def scope_download(scope):
	scope.download_days 			= 5 
	scope.download_industries 		= []
	scope.download_yf_files			= {}
	scope.downloaded_loaded_list 	= []
	scope.downloaded_missing_list 	= []
	scope.downloaded_yf_anomolies 	= {}

