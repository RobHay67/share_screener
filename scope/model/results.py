import streamlit as st


def scope_results(scope):
	# Results - for batch processing of multiple tickers
	scope.results = { 
						'passed':'', 
						'passed_2':'', 
						'failed':'', 
						'passed_count':0, 
						'passed_2_count':0, 
						'failed_count':0 
					}
