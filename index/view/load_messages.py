import streamlit as st




def message_title():
	st.subheader('Loading Ticker Index File')


def message_loading(scope):
	# st.write('loading ticker_index.csv file from....... ')
	st.info( ('loading ticker_index.csv file from > ' +  str(scope.path_ticker_index) ))


def message_loaded():
	st.info('Finished loaded the ticker index file')






# If things go wrong!!!



def message_missing_index_file(scope):
	st.error( 'Ticker Index File does not exist at path > ' + str(scope.path_ticker_index) )

	st.warning( 'creating an empty ticker_index dataframe' )

def message_new_index_file():
	st.success('successfully created empty Ticker Index Dataframe / File')