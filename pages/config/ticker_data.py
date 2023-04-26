import streamlit as st
from pages.config.three_cols import three_cols




def render_ticker_config(scope):
	ticker_keys = scope.tickers.keys()
	diff_col_size = [2,5,3]

	st.subheader('Tickers Configuration')
	three_cols( 'Tickers Configuration stored in' 		 , {}			, "scope.tickers"				, widget_type='string', diff_col_size=diff_col_size )
	three_cols( 'Page Dataframe and DF Status Stored in ', {}			, 'scope.tickers[ticker][page]'	, widget_type='string', diff_col_size=diff_col_size )
	three_cols( 'Loaded Tickers'						 , ticker_keys	, "scope.tickers.keys()"		, widget_type='string', diff_col_size=diff_col_size )

	ticker = render_ticker_df(scope)
	
	for page in scope.pages['page_list']:
		render_ticker_page_config(scope, page, ticker)



def render_ticker_df(scope):
	st.divider()
	st.subheader('Ticker Dataframe config')

	list_of_tickers = list(scope.tickers.keys())
	ticker = None
	diff_col_size = [2,5,3]
	
	col1,col2 = st.columns([3,9])
	with col1:
		if len(list_of_tickers) > 0:
			ticker = st.selectbox(
						label		='Select a ticker to display page configuration', 
						options		=list_of_tickers,
						key			='widget_ticker_selector',
						)
		else:
			st.write('No Tickers Available')
	
	if ticker != None:
		three_cols( ticker + ' original / raw df stored in', scope.tickers[ticker]['df'],  "scope.tickers['"+ticker+"']['df']", widget_type='df', diff_col_size=diff_col_size )



	
	return ticker


def render_ticker_page_config(scope, page, ticker):
	st.divider()
	st.subheader('Page config > '+page.upper())
	
	diff_col_size = [2,5,3]

	if ticker != None:
		three_cols( 'Replace '+ticker+' df for '+page+' page', scope.tickers[ticker][page]['replace_df']		,  "scope.tickers['"+ticker+"']["+page+"]['replace_df']"		, widget_type='string', diff_col_size=diff_col_size )
		three_cols( ticker + ' df group (charts or trials)'	 		, scope.tickers[ticker][page]['config_group']	,  "scope.tickers['"+ticker+"']["+page+"]['config_group']"		, widget_type='string', diff_col_size=diff_col_size )
		three_cols( 'Replace specific cols on '+ticker+' df ?'	, scope.tickers[ticker][page]['replace_column']	,  "scope.tickers['"+ticker+"']["+page+"]['replace_column']"	, widget_type='string', diff_col_size=diff_col_size )
		three_cols( ticker + ' page df stored in'					, scope.tickers[ticker][page]['df']				,  "scope.tickers['"+ticker+"']["+page+"]['df']"				, widget_type='df'	  , diff_col_size=diff_col_size )
