
import streamlit as st
import pandas as pd


def calendar(metadata):
	calendar = pd.DataFrame(metadata.calendar)
	if not calendar.empty:
		# calendar.rename(columns={0:'Percentage', 1:'Description'}, inplace = True) 
		# calendar.sort_values(by=['Percentage'], inplace=True, ascending=False)
		# calendar = calendar[['Description', 'Percentage']]
		my_expander = st.expander(label='Calendar', expanded=False)
		my_expander.dataframe(calendar, 2000, 2000)
	else:
		st.markdown('** No Calendar Information **')
