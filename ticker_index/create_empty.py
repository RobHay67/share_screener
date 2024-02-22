
import pandas as pd
import streamlit as st

from ticker_index.save import save_index



def create_empty_ticker_index(scope):

	st.toast('Ticker Index File does not exist at path > ' + str(scope.files['paths']['ticker_index']), icon='⚠️')

	dataframe_columns = []
	for column_name in scope.ticker_index['schema']: 
		dataframe_columns.append(column_name)
		ticker_index = pd.DataFrame(columns=dataframe_columns)

	ticker_index.set_index('share_code', inplace=True)
	
	# remove any delisted stocks here
	
	scope.ticker_index['df'] = ticker_index
	
	st.toast('Successfully created empty Ticker Index Dataframe / File', icon='🏆')

	save_index(scope)
