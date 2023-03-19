# TODO what is the responsibility of this function
# it seems to update the columns



import streamlit as st


from trials.verdict import trial_verdict
from widgets.add_columns import add_columns_button

# ==============================================================
# The primary code to 
# - refresh the App df
# - Refresh specific df columns 
# ==============================================================


def refresh_app_df_and_columns(scope):

	app 				= scope.apps['display_app']
	worklist 			= scope.apps[app]['worklist']
	no_of_tickers		= len(worklist)
	app_row_limit 		= int(scope.apps['row_limit'])
	
	# Progress Bar
	col1,col2 = st.columns([1.5, 10.5])

	with col1:replace_cols = add_columns_button(scope)
	with col2:my_bar = st.progress(0)

	if replace_cols:
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

					if ticker not in scope.apps[app]['loaded_tickers']:
					# add ticker to the mined_ticker list
						scope.apps[app]['loaded_tickers'].append(ticker)
					
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

		my_bar.progress(100, text='Finished running tests.')


