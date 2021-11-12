import pandas as pd
import streamlit as st



# -----------------------------------------------------------------------------------------------------------------------------------
# Ticker Index Industry Report
# -----------------------------------------------------------------------------------------------------------------------------------
def industry_report(scope):
	st.subheader('Ticker Index File contains the following Industries')
	industry_group_count = pd.DataFrame(scope.ticker_index_file['industry_group'].value_counts().rename_axis('Industry').reset_index(name='No of Codes'))
	industry_group_count = industry_group_count.sort_values(by='Industry')
	st.dataframe(industry_group_count, 2000, 1200)


