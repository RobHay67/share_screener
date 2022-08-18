import streamlit as st


def download_industry_message(scope, message):
	with scope.col5:
		st.write(  message )


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Yahoo Finance - helpers
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def render_download_message(scope, count, industry):
	app = scope.apps['display_app']

	if industry == 'random_tickers':
		download_message = ('Yahoo Finance downloading > ' + scope.apps[app]['worklist'][0] )
	else:
		download_message = ('Yahoo Finance downloading > ' + industry + ' ( ' + str(count+1) + ' of ' + str(len(scope.download['industries'])) + ' )' )
	
	download_industry_message(scope, download_message)


	