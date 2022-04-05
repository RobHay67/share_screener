import pandas as pd
import streamlit as st


def view_industries(scope):
	st.subheader('Ticker Index File contains the following Industries')
	industry_group_count = pd.DataFrame(scope.data['ticker_index']['industry_group'].value_counts().rename_axis('Industry').reset_index(name='No of Codes'))
	industry_group_count = industry_group_count.sort_values(by='Industry')
	st.dataframe(industry_group_count, 2000, 1200)

