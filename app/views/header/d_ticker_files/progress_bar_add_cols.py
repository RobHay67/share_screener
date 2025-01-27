import streamlit as st
from add_cols.model.replace_page_df import replace_page_df
from add_cols.model.replace_df_cols import replace_page_df_columns
from screener.scope.model.verdicts import determine_verdict_for_ticker
from add_cols.model.list_builder import create_list_of_tickers_to_add_columns


def add_extra_cols_progress_bar(scope, page):
	status_added_columns = False
	ticker_list = create_list_of_tickers_to_add_columns(scope, page)
	number_to_add_columns = len(ticker_list)
	app_row_limit = int(scope.config['row_limit'])

	if number_to_add_columns > 0:
		# st.write(':red[I am adding olumns again]')
		if status_added_columns == False:
			my_bar = st.progress(0)
			status_added_columns = True

		for counter, ticker in enumerate(ticker_list):
			poc = int(((counter+1) / number_to_add_columns ) * 100)
			my_bar.progress(poc, text='Adding columns to ticker ('+ticker+')')
			replace_page_df(scope, page, ticker, app_row_limit)
			replace_page_df_columns(scope, page, ticker)
			determine_verdict_for_ticker(scope, ticker)
		
	# What to show after we have added columns or not added any columns
	if status_added_columns:
		success_string = ':green[Added Columns to ( '+str(number_to_add_columns)+' ) ticker files]'
		my_bar.progress(100, text=success_string)
	else:
		# my_bar = st.progress(100, text='No Files available - cannot add any columns')
		st.write(':green[Previously Added Columns - nothing to do]')
		# st.write(':green[('+total_loaded+') files - previously loaded]')
