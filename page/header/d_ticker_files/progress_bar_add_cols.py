import streamlit as st
from add_cols.model.replace_page_df import replace_page_df
from add_cols.model.replace_df_cols import replace_page_df_columns
from trials.helpers.re_run_verdicts import determine_verdict_for_ticker
from add_cols.helpers.list_builder import create_list_of_tickers_to_add_columns
from tickers.helpers.count_page_tickers import count_page_tickers


def progress_bar_for_adding_extra_columns(scope, page):
	ticker_list = create_list_of_tickers_to_add_columns(scope, page)
	number_to_add_columns = len(ticker_list)
	app_row_limit = int(scope.config['row_limit'])
	status_just_added_columns = False

	if number_to_add_columns > 0:
		my_bar = st.progress(0)
		status_just_added_columns = True
		add_cols_counter=0

		for ticker in ticker_list:
			add_cols_counter+=1
			poc = int(((add_cols_counter) / number_to_add_columns ) * 100)
			my_bar.progress(poc, text='Adding columns to > '+ticker)
			replace_page_df(scope, page, ticker, app_row_limit)
			replace_page_df_columns(scope, page, ticker)
			determine_verdict_for_ticker(scope, ticker)
	
	# Report (columns just added) (or nothing to do)
	load_total = str(len(scope.tickers.keys()))
	page_total = str(count_page_tickers(scope))
	if status_just_added_columns:
		my_bar.empty()
		st.write(':green[Added Columns to '+str(load_total)+' ticker(s)]')
	else:
		st.write(':blue[Total Added Columns Tickers = '+load_total+' | Loaded for Page = '+page_total+']')
