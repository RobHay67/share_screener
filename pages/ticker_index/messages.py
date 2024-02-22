
import streamlit as st





def render_ticker_index_messages(scope):

	if  scope.ticker_index['render']['missing_ticker_index_file'] == True:
		st.error( 'Ticker Index File does not exist at path > ' + str(scope.files['paths']['ticker_index']) )
		st.warning( 'creating an empty ticker_index dataframe' )
		scope.ticker_index['render']['missing_ticker_index_file'] = False

	if scope.ticker_index['render']['created_empty_ticker_index_file'] == True:
		st.success('successfully created empty Ticker Index Dataframe / File')
		scope.ticker_index['render']['created_empty_ticker_index_file'] = False

	if scope.ticker_index['render']['downloading_asx']:
		st.header('Downloading Ticker Index information for the ' + scope.pages['share_market'])
		st.subheader('Downloading Ticker Master Data from https://asx.api.markitdigital.com and adding to the Ticker Index File')
		scope.ticker_index['render']['downloading_asx'] = False

	if scope.ticker_index['render']['download_market_n_a']:
		st.error('DOWNLOAD Ticker data NOT YET CONFIGURED FOR ' + scope.pages['share_market'])
		scope.ticker_index['render']['download_market_n_a'] = False

	if scope.ticker_index['render']['download_success']:
		no_downloaded = str(len(scope.ticker_index['df_downloaded']))
		st.success('number of downloaded ' + scope.pages['share_market'] + ' ticker codes = ' + no_downloaded)
		scope.ticker_index['render']['download_success'] = False

	if scope.ticker_index['render']['updating_ticker_index'] == True:
		st.info( 'Updating the records in the Ticker Index file ')
		scope.ticker_index['render']['updating_ticker_index'] = False

	if scope.ticker_index['render']['added_tickers'] != None:
		message = 'Number of ticker codes added to master ticker index = '+ str(scope.ticker_index['render']['added_tickers'])
		if scope.ticker_index['render']['added_tickers'] > 0:	
			st.warning( message)
		else:
			st.info( message)
		scope.ticker_index['render']['added_tickers'] = None

	if len(scope.ticker_index['render']['non_editable_cols']) >0:
		st.error('Cannot edit these column numbers >'+str(scope.ticker_index['render']['non_editable_cols']))
		scope.ticker_index['render']['non_editable_cols'] = []
		
	if scope.ticker_index['render']['saved_ticker_index']:
		st.success('Saved the Ticker Index File')
		scope.ticker_index['render']['saved_ticker_index'] = False


