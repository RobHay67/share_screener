import streamlit as st



# Dropdowns are automatically used for categorical columns.

# import pandas as pd
# import streamlit as st

# data = pd.Series(["A", "B", "C"])
# st.experimental_data_editor(data)
# st.experimental_data_editor(data.astype("category"))





def ticker_index_editable_df(scope):
    
	widget_key = 'widget_ticker_index_df'

	ticker_index_df = scope.ticker_index['df']

	dataframe = st.experimental_data_editor(
							data=ticker_index_df, 
							key=widget_key, 
							width=2000,
							height=800,
							)
	
	return dataframe


