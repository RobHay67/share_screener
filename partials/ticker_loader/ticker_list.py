
import streamlit as st

import pandas as pd

import numpy as np

def render_selected_tickers(scope):

	col_height = 5

	app = scope.apps['display_app']
	ticker_list = scope.apps[app]['worklist']
	no_of_tickers = len(ticker_list)


	if no_of_tickers == 1:
		with scope.col5: 
			st.button('Target = ' + ticker_list[0])


	if no_of_tickers > 1:
		# Create Dataframe of the Selected Tickers
		if no_of_tickers < col_height:
			ticker_df = pd.DataFrame(ticker_list, columns=['Tickers'])
		else:		
			no_of_columns = no_of_tickers/col_height
			col_no = 0
			ticker_df = pd.DataFrame()

			# add tickers in columns of col_height(10) tickers
			while col_no < no_of_columns:
				col_name = 'col_' + str(col_no)
				sublist = ticker_list[col_no*col_height:(col_no*col_height)+(col_height)]
				# pad for short list length
				while len(sublist) < col_height:
					sublist.append('')
				ticker_df[col_name] = sublist
				col_no +=1

		description = 'Target (' + str(no_of_tickers) + ')'

		with scope.col5: 
			my_expander = st.expander(label=description, expanded=False )
			my_expander.dataframe(ticker_df)

