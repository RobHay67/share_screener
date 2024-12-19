
import streamlit as st
import pandas as pd


def dividends(metadata):
	dividends = pd.DataFrame(metadata.dividends)
	if not dividends.empty:
		dividends.reset_index(inplace=True)
		dividends.sort_values(by=['Date'], inplace=True, ascending=False)
		my_expander = st.expander(label='Dividends')
		my_expander.dataframe(dividends, 2000, 2000)
	else:
		st.markdown('** No Dividends **')