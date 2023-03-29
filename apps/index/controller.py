
import streamlit as st

from ticker_index.download import download_ticker_index_data
from apps.reports.industries import view_industries

def render_ticker_index_page(scope):

	no_of_tickers_in_index = str((len(scope.ticker_index)))

	col1,col2,col3 = st.columns([8,2,2])
	with col1:
		st.subheader('Ticker Index File')
		st.write('Currently ' + no_of_tickers_in_index + ' codes in the ticker index')
		st.caption('< scope.ticker_index >')
	with col2:
		industry_report = st.button('Industry Report')
	with col3:
		download_now = st.button('Download latest Ticker Index data')

	if download_now:
		download_ticker_index_data(scope)

	if industry_report:
		view_industries(scope)

	st.dataframe(scope.ticker_index, 2000, 1200)
