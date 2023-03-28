# ==============================================================
# The primary code to 
# - refresh the App df (completely)
# - Refresh specific df columns (activate or change col_adders)
# ==============================================================

import streamlit as st

from trials.verdict import trial_verdict


def add_cols_to_df_layer(scope):

	col1,col2,col3 = st.columns([1.5, 9.0, 1.5])  #12.0
	with col1:st.caption('Add Columns to Ticker Files')
	with col2:render_progress_bar(scope)      # TODO this will add/update the columns as well!


def render_progress_bar(scope):
	app = scope.apps['display_app']

	if len(scope.apps[app]['worklist']) == 0:
		st.write('No Files available - make some selections')
	else:
		replace_df_and_add_columns(scope)


def replace_df_and_add_columns(scope):

	app = scope.apps['display_app']
	ticker_list = create_ticker_list_to_add_columns(scope, app)
	app_row_limit = int(scope.apps['row_limit'])
	completion_text = 'Finished adding columns to Ticker File(s)'

	my_bar = st.progress(0)

	if len(ticker_list) > 0:
		no_of_tickers = len(ticker_list)

		for counter, ticker in enumerate(ticker_list):
			poc = int(((counter+1) / no_of_tickers ) * 100)
			my_bar.progress(poc, text='Adding columns where file = '+ticker)
			replace_app_df(scope, app, ticker, app_row_limit)
			replace_specific_app_columns(scope, app, ticker)
			# trial_verdict(scope)

		my_bar.progress(100, text=completion_text)
	else:
		my_bar = st.progress(100, text='No Files available - cannot add columns')


def create_ticker_list_to_add_columns(scope, app):

	list_of_tickers_to_add_columns= []

	for ticker in scope.apps[app]['worklist']:
		# Ensure ticker data available otherwise
		# function will fail on missing columns
		if ticker in list(scope.tickers.keys()): 
			list_of_tickers_to_add_columns.append(ticker)

	return list_of_tickers_to_add_columns


def replace_app_df(scope, app, ticker, app_row_limit):
	# Replace the App df if requested

	if scope.tickers[ticker][app]['replace_df'] == True:
		ticker_df = scope.tickers[ticker]['df'].copy()
		# limit no of rows for the APP df (speeds up app rendering)	
		ticker_df = ticker_df.head(app_row_limit)
		
		# Cache the ticker dataframe to be utilised by this app/page
		scope.tickers[ticker][app]['df'] = ticker_df

		if ticker not in scope.apps[app]['tickers_with_add_cols']:
		# add ticker to the loaded_ticker list
			scope.apps[app]['tickers_with_add_cols'].append(ticker)
		
		# Set the status to false to prevent refreshing unnecesarily
		scope.tickers[ticker][app]['replace_df'] = False


def replace_specific_app_columns(scope, app, ticker):

	type_of_column_adder = scope.tickers[ticker][app]['type_col_adder']
	# screener_assessment_required = False
	scope.apps[app]['render']['verdicts'] = False
				
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
					# screener_assessment_required = True
					scope.apps[app]['render']['verdicts'] = True
					# trial_verdict(scope, app, ticker)













# def progress_bar_add_cols_to_df(scope):

# 	progress_bar_exists = False
# 	app = scope.apps['display_app']
# 	app_row_limit 		= int(scope.apps['row_limit'])

# 	list_of_tickers_to_add_columns = create_ticker_list_to_add_columns(scope, app)

# 	if len(list_of_tickers_to_add_columns) > 0:
		
# 		no_of_tickers = len(list_of_tickers_to_add_columns)

# 		if progress_bar_exists==False:
# 			my_bar = st.progress(0)
# 			progress_bar_exists = True

# 		for counter, ticker in enumerate(list_of_tickers_to_add_columns):
# 			poc = int(((counter+1) / no_of_tickers ) * 100)
# 			my_bar.progress(poc, text='Adding Columns to Ticker File')
# 			replace_app_df(scope, app, ticker, app_row_limit)
# 			replace_specific_app_columns(scope, app, ticker)
# 			# trial_verdict(scope)


# 	if progress_bar_exists==True:
# 		my_bar.progress(100, text='Columns Added to Every Ticker File')
# 	else:
# 		my_bar = st.progress(100, text='No Files available - cannot add columns')












# This is the old code and has been refactored into seperate components for simplicity




# def add_columns_to_dfs_progress_bar(scope):
		

# 		for counter, ticker in enumerate(worklist):
			
# 			screener_assessment_required = False

# 			# Determine POC % for Progress Bar
# 			poc = int(((counter+1) / no_of_tickers ) * 100)
# 			my_bar.progress(poc, text='Calculating Ratios and Metrics for Each Ticker')

# 			if ticker in list(scope.tickers.keys()): 
# 			# Ensure ticker data available - function will fail if data is not available

# 				# -------------------------------------------------------------------
# 				# Replace the App df if requested
# 				# -------------------------------------------------------------------

# 				if scope.tickers[ticker][app]['replace_df'] == True:
# 					ticker_df = scope.tickers[ticker]['df'].copy()
# 					ticker_df = ticker_df.head(app_row_limit) 				# limit no of rows for the APP df (speeds up app rendering)				
# 					scope.tickers[ticker][app]['df'] = ticker_df			# Cache the ticker dataframe to be mined by this app

# 					if ticker not in scope.apps[app]['tickers_with_add_cols']:
# 					# add ticker to the loaded_ticker list
# 						scope.apps[app]['tickers_with_add_cols'].append(ticker)
					
# 					# Set the status to false to prevent refreshing unnecesarily
# 					scope.tickers[ticker][app]['replace_df'] = False



# 				# -------------------------------------------------------------------
# 				# Replace specific columns in the app df if requested
# 				# -------------------------------------------------------------------
				
# 				type_of_column_adder = scope.tickers[ticker][app]['type_col_adder']
				
# 				if type_of_column_adder != None:			
# 				# Some apps/pages do not have any column adders
# 					for column_adder, status in scope.tickers[ticker][app]['column_adders'].items():
# 						if status == True:	
# 						# Only replace the columns if requested to do so for this column adder
# 							ticker_df = scope.tickers[ticker][app]['df']
# 							# Call the column adding function for this column_adder
# 							scope[type_of_column_adder][column_adder]['add_columns']['function'](scope, column_adder, ticker, ticker_df)
# 							# Set the status to false to prevent refreshing unnecesarily
# 							scope.tickers[ticker][app]['column_adders'][column_adder] = False

# 							if type_of_column_adder == 'trials':
# 							# the trial(s) have been rerun so we will need to refresh
# 							# the overall trial verdict. However we do this later so 
# 							# we just store the need in local variable.
# 								screener_assessment_required = True
				
# 				# -------------------------------------------------------------------
# 				# Determine an overall verdict if a change has been made to any trial
# 				# -------------------------------------------------------------------
# 				if screener_assessment_required == True:	
# 					trial_verdict(scope, ticker)

# 				print('Need a status that this ticker is ready to render >', ticker)

# 		my_bar.progress(100, text='Finished running tests.')


