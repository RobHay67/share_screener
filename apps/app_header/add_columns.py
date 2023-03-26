# ==============================================================
# The primary code to 
# - refresh the App df (completely)
# - Refresh specific df columns (activate or change col_adders)
# ==============================================================

import streamlit as st

from trials.verdict import trial_verdict
from widgets.add_columns import add_columns_button
from widgets.dataframes import page_dataframe_dropdown_list


def col_adder_title(scope):
	button = st.button(
						label='Add Columns to Ticker Data', 
						use_container_width=True, 
						disabled=True,
						key='col_adder_title'
						)
	return button



def render_add_cols_to_df(scope):
	print('%'*33)
	print('render_add_cols_to_df')
	app 				= scope.apps['display_app']
	worklist 			= scope.apps[app]['worklist']
	no_of_tickers		= len(worklist)
	app_row_limit 		= int(scope.apps['row_limit'])
	
	# Progress Bar
	# col1,col2 = st.columns([1.5, 10.5])
	col1,col2,col3,col4,col5 = st.columns([1.5, 5.0, 2.0, 2.0, 1.5])  #12.5


	with col1:col_adder_title(scope)
	with col2:my_bar = st.progress(0)
	# with col3:'Keep this blank'
	with col4:page_dataframe_dropdown_list(scope)
	with col5:replace_cols = add_columns_button(scope)

	if replace_cols:
		st.write('Replace Columns variable = ', replace_cols)
		for counter, ticker in enumerate(worklist):
			
			screener_assessment_required = False

			# Determine POC % for Progress Bar
			poc = int(((counter+1) / no_of_tickers ) * 100)
			my_bar.progress(poc, text='Calculating Ratios and Metrics for Each Ticker')

			if ticker in list(scope.tickers.keys()): 
			# Ensure ticker data available - function will fail if data is not available

				# -------------------------------------------------------------------
				# Replace the App df if requested
				# -------------------------------------------------------------------

				if scope.tickers[ticker][app]['replace_df'] == True:
					ticker_df = scope.tickers[ticker]['df'].copy()
					ticker_df = ticker_df.head(app_row_limit) 				# limit no of rows for the APP df (speeds up app rendering)				
					scope.tickers[ticker][app]['df'] = ticker_df			# Cache the ticker dataframe to be mined by this app

					if ticker not in scope.apps[app]['tickers_with_add_cols']:
					# add ticker to the loaded_ticker list
						print('Adding ticker to tickers_with_add_cols > ', ticker)
						scope.apps[app]['tickers_with_add_cols'].append(ticker)
					
					# Set the status to false to prevent refreshing unnecesarily
					scope.tickers[ticker][app]['replace_df'] = False



				# -------------------------------------------------------------------
				# Replace specific columns in the app df if requested
				# -------------------------------------------------------------------
				
				type_of_column_adder = scope.tickers[ticker][app]['type_col_adder']
				
				if type_of_column_adder != None:			
				# Some apps/pages do not have any column adders
					for column_adder, status in scope.tickers[ticker][app]['column_adders'].items():
						if status == True:	
						# Only replace the columns if requested to do so for this column adder
							ticker_df = scope.tickers[ticker][app]['df']
							# Call the column adding function for this column_adder
							scope[type_of_column_adder][column_adder]['add_columns']['function'](scope, column_adder, ticker, ticker_df)
							# Set the status to false to prevent refreshing unnecesarily
							scope.tickers[ticker][app]['column_adders'][column_adder] = False

							if type_of_column_adder == 'trials':
							# the trial(s) have been rerun so we will need to refresh
							# the overall trial verdict. However we do this later so 
							# we just store the need in local variable.
								screener_assessment_required = True
				
				# -------------------------------------------------------------------
				# Determine an overall verdict if a change has been made to any trial
				# -------------------------------------------------------------------
				if screener_assessment_required == True:	
					trial_verdict(scope, ticker)

				print('Need a status that this ticker is ready to render >', ticker)

		my_bar.progress(100, text='Finished running tests.')


