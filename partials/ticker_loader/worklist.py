import streamlit as st
import pandas as pd




def render_worklist(scope):

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

		description = 'Work List (' + str(no_of_tickers) + ')'

		with scope.col5: 
			my_expander = st.expander(label=description, expanded=False )
			my_expander.dataframe(ticker_df)



def render_errors(scope):
	print('')
	print('='*100)
	print('render_errors')
	print('-'*100)

	app = scope.apps['display_app']
	for ticker in scope.apps[app]['worklist']:
		if ticker in scope.missing_tickers['errors'].keys():
			# print(ticker)
			if scope.missing_tickers['errors'][ticker]['load'] != None:
				print(ticker, '   >    ', scope.missing_tickers['errors'][ticker]['load'])
			if scope.missing_tickers['errors'][ticker]['yf'] != None:
				print(ticker, '   >    ', scope.missing_tickers['errors'][ticker]['yf'])
			# for error in scope.missing_tickers['errors'][ticker]:
			# 	print(ticker, '   >    ', error)

	print('-'*100)




