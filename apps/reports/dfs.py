
import streamlit as st


def render_loaded_df(scope):

	app = scope.apps['display_app']

	ticker = scope.apps[app]['render']['ticker_file']

	dataframe = scope.tickers[ticker]['df']

	no_of_rows = str(len(dataframe))
	my_expander = st.expander(
					label=('raw file > ' + ticker+' (' + no_of_rows + ')'), 
					expanded=True 
					)
	my_expander.dataframe(dataframe, 2000, 500)	


def render_df_with_added_cols(scope):

	app = scope.apps['display_app']

	ticker = scope.apps[app]['render']['col_added_df']

	dataframe = scope.tickers[ticker][app]['df']

	no_of_rows = str(len(dataframe))
	my_expander = st.expander(
					label=('add cols > ' + ticker+' (' + no_of_rows + ')'), 
					expanded=True 
					)
	my_expander.dataframe(dataframe, 2000, 500)	

