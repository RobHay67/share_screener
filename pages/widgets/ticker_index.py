
import streamlit as st
from ticker_index.save import save_index
from ticker_index.download import download_ticker_index_data
from ticker_index.schema import editable_columns


# Dropdowns are automatically used for categorical columns.

# import pandas as pd
# import streamlit as st

# data = pd.Series(["A", "B", "C"])
# st.experimental_data_editor(data)
# st.experimental_data_editor(data.astype("category"))

def ticker_index_editable_df(scope):
    
	widget_key = 'widget_ticker_index_df'

	ticker_index_df = scope.ticker_index['df']

	dataframe = st.experimental_data_editor(
							data=ticker_index_df, 
							key=widget_key, 
							width=2000,
							height=800,
							)
	
	return dataframe


def download_ticker_index_button(scope):
	
	widget_key = 'widget_download_ticker_index_button'
	
	button = st.button(
						label='Download latest Ticker Index data', 
						use_container_width=True, 
						type='primary',
						key=widget_key,
						on_click=download_ticker_index_data,
						args=(scope, )
						)
	
	return button


def save_ticker_index_button(scope):

	widget_key = 'widget_save_ticker_index'
	
	button = st.button(
						label='Save Changes to Ticker Index', 
						use_container_width=True, 
						type='secondary',
						key=widget_key,
						on_click=save_changes_to_ticker_index,
						args=(scope,)
						)
	
	return button


def save_changes_to_ticker_index(scope):
	# TODO st.experimental_data_editor
	# Note this solution is refering to the old_df to get the keys.
	# it should be referring to the new editable df
	# this will probable break if we allow add rows
	
	editable_cols = editable_columns(scope)
	save_required = False

	ticker_index_df = scope.ticker_index['df']

	# determine if we have edited records
	edited_records = st.session_state["widget_ticker_index_df"]["edited_cells"]

	# for key in sorted(st.session_state["widget_ticker_index_df"]):print(key)

	if len(edited_records)>0:
		for position, new_value in edited_records.items():
			print('Coordinates  = ', position)
			print('New Value    = ', new_value)

			co_ordinates = position.split(':')
			row_no = int(co_ordinates[0])
			col_no = int(co_ordinates[1])
			print('Row Number   = ', row_no)
			print('Col Number   = ', col_no)

			# Check if we are allowed to edit this column
			if col_no in editable_cols.keys():

				col_name = editable_cols[col_no]
				print('Col Name     = ', col_name)
				
				print('Determine the index for the specified row > ', row_no)
				index_name = ticker_index_df.iloc[[row_no]].index.values.tolist()
				ticker = index_name[0]
				print('Ticker       = ', ticker)

				print('Lets Update the Original df')
				# scope.ticker_index['df'].at[ticker, 'company_name'] = new_value
				ticker_index_df.at[ticker, col_name] = new_value

				save_required = True
			else:
				scope.ticker_index['render']['non_editable_cols'].append(col_no)
		
		if save_required:save_index(scope)



def render_ticker_index_messages(scope):

	if  scope.ticker_index['render']['missing_ticker_index_file'] == True:
		st.error( 'Ticker Index File does not exist at path > ' + str(scope.files['paths']['ticker_index']) )
		st.warning( 'creating an empty ticker_index dataframe' )
		scope.ticker_index['render']['missing_ticker_index_file'] = False

	if scope.ticker_index['render']['created_empty_ticker_index_file'] == True:
		st.success('successfully created empty Ticker Index Dataframe / File')
		scope.ticker_index['render']['created_empty_ticker_index_file'] = False

	if scope.ticker_index['render']['downloading_asx']:
		st.header('Downloading Ticker Index information for the ' + scope.config['share_market'])
		st.subheader('Downloading Ticker Master Data from https://asx.api.markitdigital.com and adding to the Ticker Index File')
		scope.ticker_index['render']['downloading_asx'] = False

	if scope.ticker_index['render']['download_market_n_a']:
		st.error('DOWNLOAD Ticker data NOT YET CONFIGURED FOR ' + scope.config['share_market'])
		scope.ticker_index['render']['download_market_n_a'] = False

	if scope.ticker_index['render']['download_success']:
		no_downloaded = str(len(scope.ticker_index['df_downloaded']))
		st.success('number of downloaded ' + scope.config['share_market'] + ' ticker codes = ' + no_downloaded)
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


