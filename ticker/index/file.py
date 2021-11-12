import os
import pandas as pd
import streamlit as st


from ticker.index.schema import schema
from ticker.index.schema import csv_dates
from ticker.index.schema import csv_dtypes

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# TICKER INDEX FILE - loader and Saver
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def load_index( scope ):
	st.title('Loading Ticker Index File')

	if os.path.exists( scope.path_ticker_index ):
		st.write('loading ticker_index.csv file from....... ')
		st.markdown(('##### ' +  str(scope.path_ticker_index) ))

		ticker_index = pd.read_csv(  scope.path_ticker_index, 
									dtype=csv_dtypes(schema),
									parse_dates=csv_dates(schema),
									)
		# ticker_index['blue_chip'] = ticker_index['blue_chip'].astype(int)
		ticker_index['listing_date'] = pd.to_datetime( ticker_index['listing_date'].dt.date  )
		st.write('loaded the ticker index file')
		ticker_index.set_index('share_code', inplace=True)
		# remove any delisted stocks here
		scope.ticker_index_file = ticker_index
		scope.dropdown_lists_need_updating = True
	else: 
		st.error( 'Ticker Index File does not exist at path > ' + str(scope.path_ticker_index) )
		st.info( 'creating an empty ticker_index dataframe' )
		dataframe_columns = []
		for column_name in schema: 
			dataframe_columns.append(column_name)
			ticker_index = pd.DataFrame(columns=dataframe_columns)
		st.success('successfully created empty Ticker Index dataframe')
		ticker_index.set_index('share_code', inplace=True)
		# remove any delisted stocks here
		scope.ticker_index_file = ticker_index
		save_index(scope)
		st.markdown("""---""")
		st.error('Click on the Ticker Index button to update the Ticker Index')

def save_index( scope ): # DONE
	# st.subheader('Save Ticker Index File')
	saving_df = scope.ticker_index_file.copy()
	saving_df.reset_index(inplace=True)      	 # ensure that the index is saved as a normal column
	saving_df.to_csv( scope.path_ticker_index, index=False )
	st.success('saved Ticker Index file')



