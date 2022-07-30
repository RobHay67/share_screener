import streamlit as st

from config.progress.three_cols import three_cols




def scope_progress(scope):
	# Results - for batch processing of multiple tickers
	scope.progress = {}

	scope.progress = { 
						'passed':'', 
						'passed_2':'', 
						'failed':'', 
						'passed_count':0, 
						'passed_2_count':0, 
						'failed_count':0 
					}



