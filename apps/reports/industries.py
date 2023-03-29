import pandas as pd
import streamlit as st


def render_industry_report(scope):


	if scope.ticker_index['render']['industry_report']:

		st.subheader('Ticker Index File contains the following Industries')

		list_of_industries = sorted(scope.ticker_index['df']['industry_group'].unique())


		for industry in list_of_industries:
			industry_df = scope.ticker_index['df'][scope.ticker_index['df']['industry_group'] == industry ]
			industry_label = industry + ' ( ' + str(len(industry_df)) + ' )'
			my_expander = st.expander(label=industry_label, expanded=False )
			my_expander.dataframe(industry_df, 2000, 2000)	


