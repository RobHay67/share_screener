
import streamlit as st
import pandas as pd

def news(metadata):
	news = pd.DataFrame(metadata.news)
	if not news.empty:
		# news.rename(columns={0:'Percentage', 1:'Description'}, inplace = True) 
		# news.sort_values(by=['Percentage'], inplace=True, ascending=False)
		# news = news[['Description', 'Percentage']]
		my_expander = st.expander(label='News', expanded=False)
		my_expander.dataframe(news, 2000, 2000)
	else:
		st.markdown('** No News **')



