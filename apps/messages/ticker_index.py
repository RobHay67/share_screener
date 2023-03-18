import streamlit as st



# If things go wrong!!!

def message_missing_index_file(scope):
	st.error( 'Ticker Index File does not exist at path > ' + str(scope.files['paths']['ticker_index']) )

	st.warning( 'creating an empty ticker_index dataframe' )

def message_new_index_file():
	st.success('successfully created empty Ticker Index Dataframe / File')


# Save messages

def message_save():
	st.success('saved Ticker Index file')


# Update Messages

def message_updating():

	st.info( 'Updating the records in the Ticker Index file ')


def message_warning(add_records_counter, message):

	if add_records_counter > 0:
		st.warning( message)
	else:
		st.info( message)


# Ticker Index Download Messages

def message_download_ticker_index_asx(scope):
	st.header('Downloading Ticker Index information for the ' + scope.config['share_market'])
	st.subheader('Downloading Ticker Master Data from https://asx.api.markitdigital.com and adding to the Ticker Index File')
	st.markdown("""---""")

def message_index_download_success(scope, downloaded_ticker_info):
	st.success('number of downloaded ' + scope.config['share_market'] + ' ticker codes = ' + str(len(downloaded_ticker_info)))

def message_index_not_asx(scope):
	st.error('DOWNLOAD Ticker data NOT YET CONFIGURED FOR ' + scope.config['share_market'])
