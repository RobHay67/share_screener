
import streamlit as st
import pandas as pd


def institutional(metadata):
	institutional = pd.DataFrame(metadata.institutional_holders)
	if not institutional.empty:
		institutional.sort_values(by=['Shares'], inplace=True, ascending=False)
		my_expander = st.expander(label='Institutional Holders', expanded=False)
		my_expander.dataframe(institutional, 2000, 2000)
	else:
		st.markdown('** Missing Institutional Holders Information **')



def major(metadata):
	major_holders = pd.DataFrame(metadata.major_holders)
	if not major_holders.empty:
		major_holders.rename(columns={0:'Percentage', 1:'Description'}, inplace = True) 
		major_holders.sort_values(by=['Percentage'], inplace=True, ascending=False)
		major_holders = major_holders[['Description', 'Percentage']]
		my_expander = st.expander(label='Major Holders', expanded=False)
		my_expander.dataframe(major_holders, 2000, 2000)
	else:
		st.markdown('** Missing Major Holders Information **')




