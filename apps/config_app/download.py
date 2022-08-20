
import streamlit as st

from progress.three_cols import three_cols



def view_download(scope):


	st.markdown('##### Most Recent Download Variables and Data')
	three_cols( 'Days to Download (recent)', scope.download['days'], 'scope.download.days' )
	three_cols( 'Industry Groups for y_finance to iterate over', scope.download['yf_download_these_industries'], 'scope.download.yf_download_these_industries',  widget_type='selectbox')
	st.markdown("""---""")

	three_cols( 'Latest Download Batch from y_finance', scope.download['yf_data'], 'scope.download.yf_data' )
	three_cols( 'Latest Error Messages from y_finance', scope.download['yf_errors']  , 'scope.download.yf_errors' )






