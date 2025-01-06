import streamlit as st




def message_downloading(scope):
	st.toast(
		'Downloading '
		+ scope.config['share_market'] 
		+ ' Ticker Master Data from https://asx.api.markitdigital.com and adding to the Ticker Index File'
		)


def message_completed_download(scope, downloaded_df):
	st.toast(
		'Downloaded '
		+ str(len(downloaded_df)) 
		+ ' for the ' + scope.config['share_market'] 
		+ ' share market', 
		icon='🏆'
		)
	
def message_failed_market(scope):
	st.toast(
		'DOWNLOAD Ticker data NOT YET CONFIGURED FOR ' 
		+ scope.config['share_market'], 
		icon='⚠️'
		)
