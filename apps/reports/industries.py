import pandas as pd
import streamlit as st


def view_industries(scope):
	st.subheader('Ticker Index File contains the following Industries')

	list_of_industries = sorted(scope.ticker_index['industry_group'].unique())


	for industry in list_of_industries:
		industry_df = scope.ticker_index[scope.ticker_index['industry_group'] == industry ]
		industry_label = industry + ' ( ' + str(len(industry_df)) + ' )'
		my_expander = st.expander(label=industry_label, expanded=False )
		my_expander.dataframe(industry_df, 2000, 2000)	





	# industry_group_count = pd.DataFrame(scope.ticker_index['industry_group'].value_counts().rename_axis('Industry').reset_index(name='No of Codes'))
	# industry_group_count = industry_group_count.sort_values(by='Industry')
	# st.dataframe(industry_group_count, 2000, 1200)



