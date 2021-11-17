import pandas as pd
import streamlit as st


def view_index(scope):
	col1,col2 = st.columns([6,2])
	
	with col1: st.subheader('Ticker Index File')
	with col2: st.write('< ticker_index >')

	st.dataframe(scope.ticker_index, 2000, 1200)

def view_industries(scope):
	st.subheader('Ticker Index File contains the following Industries')
	industry_group_count = pd.DataFrame(scope.ticker_index['industry_group'].value_counts().rename_axis('Industry').reset_index(name='No of Codes'))
	industry_group_count = industry_group_count.sort_values(by='Industry')
	st.dataframe(industry_group_count, 2000, 1200)
