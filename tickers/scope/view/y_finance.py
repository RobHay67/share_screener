import streamlit as st
from app.views.widgets.cols_three import three_cols


def show_y_finance_config(scope):
	st.subheader('Y Finance ( Download Configuration )')
	three_cols( 'Download Variables', 	{}, 							"scope.yf", widget_type='string' )
	three_cols( 'Days to Download',	 	scope.config['download_days'], 	"scope.config['download_days']" )
	three_cols( 'Download periods',		scope.config['periods'], 		"scope.yf['periods']" )
	st.divider()
	st.caption('yFinance Batch Download Variables')
	three_cols( 'Type', scope.yf['batch_type'], "scope.yf['batch_type']" )
	# three_cols( 'Batch Number', scope.yf['batch_no'], "scope.yf['batch_no']" )
	# three_cols( 'Industry', scope.yf['batch_industry'], "scope.yf['batcbatch_industryh_type']" )
	three_cols( 'Ticker String', 	scope.yf['batch_ticker_string'], "scope.yf['batch_ticker_string']" )
	three_cols( 'Data', 			scope.yf['batch_data'], "scope.yf['batch_data']" )
	three_cols( 'Errors', 			scope.yf['batch_errors'], "scope.yf['batch_errors']" )
	st.divider()
	st.caption('Download Variables')
	# three_cols( 'Ticker List', scope.yf['ticker_list'], "scope.yf['ticker_list']" )
	three_cols( 'All Errors', 		scope.yf['all_errors']  , "scope.yf['all_errors']" )
	three_cols( 'All Data', 		scope.yf['all_data'], "scope.yf['all_data']" )
	