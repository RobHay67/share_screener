
import streamlit as st

from ticker_index.download import download_ticker_index_data
from apps.reports.industries import render_industry_report
from widgets.industries import industry_report_button

def render_ticker_index_page(scope):

	no_of_tickers_in_index = str((len(scope.ticker_index['df'])))

	col1,col2,col3 = st.columns([9.5,1.0,1.5]) #12
	with col1:
		st.subheader('Ticker Index File')
		st.write('Currently ' + no_of_tickers_in_index + ' codes in the ticker index')
		st.caption("< scope.ticker_index['df'] >")
	with col2:industry_report_button(scope)
		# industry_report = st.button('Industry Report', use_container_width=True)
	with col3:
		download_now = st.button('Download latest Ticker Index data', use_container_width=True, type='primary')

	if download_now:
		download_ticker_index_data(scope)

	# if industry_report:
	render_industry_report(scope)

	ticker_index_df = scope.ticker_index['df']
	# print(ticker_index_df.head(3))
	# st.dataframe(ticker_index_df, 2000, 1200)


	st.experimental_data_editor(ticker_index_df, key="ticker_index_edits")

	# st.experimental_data_editor(data.astype("category"))

	# st.write("Here's the session state:")
	# st.write(st.session_state["ticker_index_edits"]) # 👈 Access the edited data

	
	# determine if we have edited records
	edited_records = st.session_state["ticker_index_edits"]["edited_cells"]

	if len(edited_records) > 0:
		st.write('We have some edited record')
	# st.write(st.session_state["ticker_index_edits"])

		st.write(st.session_state["ticker_index_edits"]["edited_cells"])

	# print('='*66)
	# print(scope.ticker_index['df'].head(1))

	# print(edited_df.head(1))




# Dropdowns are automatically used for categorical columns.

# import pandas as pd
# import streamlit as st

# data = pd.Series(["A", "B", "C"])
# st.experimental_data_editor(data)
# st.experimental_data_editor(data.astype("category"))