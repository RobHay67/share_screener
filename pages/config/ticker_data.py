import streamlit as st
from pages.config.three_cols import three_cols




def view_ticker_data(scope):
    
	st.subheader('Tickers Configuration')
	three_cols( 'Tickers Configuration stored in', {}, "scope.tickers", widget_type='string' )

	for ticker in scope.tickers.keys():
		st.subheader(ticker)
		three_cols( 'Ticker DataFrame', '{ }',  "scope.tickers["+ticker+"]['df']", widget_type='string' )
		three_cols( 'Ticker Trials', scope.tickers[ticker]['trials'],  "scope.tickers["+ticker+"]['df']", widget_type='string' )
		for page in scope.pages['page_list']:
			st.divider()
			st.subheader(page.upper() + ' page')
			three_cols( 'Dataframe with added columns', scope.tickers[ticker][page]['df'],  "scope.tickers["+ticker+"]["+page+"]['df']", widget_type='string' )
			three_cols( 'Replace Dataframe for page', scope.tickers[ticker][page]['replace_df'],  "scope.tickers["+ticker+"]["+page+"]['replace_df']", widget_type='string' )
			three_cols( 'Settings Group (Charts or Trials)', scope.tickers[ticker][page]['config_group'],  "scope.tickers["+ticker+"]["+page+"]['config_group']", widget_type='string' )
			three_cols( 'Recalculate This Column Adder', scope.tickers[ticker][page]['replace_column'],  "scope.tickers["+ticker+"]["+page+"]['replace_column']", widget_type='string' )
