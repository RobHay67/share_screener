
import streamlit as st

from config.results.three_cols import three_cols



def view_download(scope):


	st.markdown('##### Most Recent Download Variables and Data')
	three_cols( 'Days to Download (recent)', scope.data['download']['days'], 'scope.data.download.days' )
	three_cols( 'Industry Groups for y_finance to iterate over', scope.data['download']['industries'], 'scope.data.download.industries',  widget_type='selectbox')
	st.markdown("""---""")

	three_cols( 'Missing Ticker List', scope.data['download']['missing_list'], 'scope.data.download.missing_list',  widget_type='selectbox')
	three_cols( 'Latest Download Batch from y_finance', scope.data['download']['yf_files'], 'scope.download.yf_files' )
	three_cols( 'Latest Error Messages from y_finance', scope.data['download']['yf_anomolies']  , 'scope.download.yf_anomolies' )






