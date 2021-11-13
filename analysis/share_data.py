
import streamlit as st





# this only gets refreshed if the ticker changes or the number of rows changes
@st.cache
def extract_ticker(scope, ticker, df_row_limit ):

	share_data = scope.share_data_files[ticker].copy()

	if df_row_limit != None:
		share_data.sort_values(by=['date'], inplace=True, ascending=False)
		share_data = share_data.head(df_row_limit)
		
	return share_data