import streamlit as st
from apps.config.three_cols import three_cols




def view_ticker_data(scope):
    
	st.subheader('Tickers Configuration')
	three_cols( 'Tickers Configuration stored in', {}, "scope.tickers", widget_type='string' )

	for ticker in scope.tickers.keys():
		print(ticker)

		st.subheader(ticker)
		three_cols( 'Ticker DataFrame', '{ }',  "scope.tickers["+ticker+"]['df']", widget_type='string' )
		three_cols( 'Ticker Trials', scope.tickers[ticker]['trials'],  "scope.tickers["+ticker+"]['df']", widget_type='string' )
		# for app in scope.apps[]
		for app in scope.apps['app_list']:
			st.write('---')
			st.subheader(app.upper() + ' app / page')
			three_cols( 'Dataframe with added columns', scope.tickers[ticker][app]['df'],  "scope.tickers["+ticker+"]["+app+"]['df']", widget_type='string' )
			three_cols( 'Replace this Dataframe', scope.tickers[ticker][app]['replace_df'],  "scope.tickers["+ticker+"]["+app+"]['replace_df']", widget_type='string' )
			three_cols( 'Type of Column Adder', scope.tickers[ticker][app]['type_col_adder'],  "scope.tickers["+ticker+"]["+app+"]['type_col_adder']", widget_type='string' )
			three_cols( 'Column Adder Config', scope.tickers[ticker][app]['column_adders'],  "scope.tickers["+ticker+"]["+app+"]['column_adders']", widget_type='string' )
