import streamlit as st

from add_cols.replace_page_df import replace_page_df
from add_cols.replace_df_cols import replace_page_df_columns
from screener.scope.model.verdicts import determine_verdict_for_ticker
from add_cols.list_builder import create_list_of_tickers_to_add_columns


def add_extra_cols_progress_bar(scope, page):

	if len(scope.page[page]['worklist']) == 0:
		st.write('No Files available - select some')
	else:
		ticker_list = create_list_of_tickers_to_add_columns(scope, page)
		app_row_limit = int(scope.config['row_limit'])

		my_bar = st.progress(0)

		if len(ticker_list) > 0:
			no_of_tickers = len(ticker_list)

			for counter, ticker in enumerate(ticker_list):
				poc = int(((counter+1) / no_of_tickers ) * 100)
				my_bar.progress(poc, text='Adding columns to ticker ('+ticker+')')
				replace_page_df(scope, page, ticker, app_row_limit)
				replace_page_df_columns(scope, page, ticker)
				determine_verdict_for_ticker(scope, ticker)

			my_bar.progress(100, text='Finished adding columns to ( ' + str(len(ticker_list)) + ' ) ticker files')
		else:
			my_bar = st.progress(100, text='No Files available - cannot add any columns')
