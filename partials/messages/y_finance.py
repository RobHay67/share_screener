import streamlit as st




# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Yahoo Finance - helpers
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def render_download_message(scope, batch_no, industry):
	app = scope.apps['display_app']

	if industry == 'random_tickers':
		# download_message = ('Yahoo Finance > ' + scope.apps[app]['worklist'][0] )
		print(scope.download['yf_ticker_string'])
		download_message = ('Yahoo Finance > ' + scope.download['yf_ticker_string'] )
	else:
		download_message = ('Yahoo Finance > ' + industry + ' ( batch ' + str(batch_no+1) + ' of ' + str(len(scope.download['yf_industry_groups'])) + ' )' )
	
	with scope.col5:
		st.write(  download_message )

