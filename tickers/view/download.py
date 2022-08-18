
import streamlit as st

from progress.three_cols import three_cols



def view_download(scope):


	st.markdown('##### Most Recent Download Variables and Data')
	three_cols( 'Days to Download (recent)', scope.download['days'], 'scope.download.days' )
	three_cols( 'Industry Groups for y_finance to iterate over', scope.download['industry_groups'], 'scope.download.industries',  widget_type='selectbox')
	st.markdown("""---""")

	three_cols( 'Latest Download Batch from y_finance', scope.download['yf_files'], 'scope.download.yf_files' )
	three_cols( 'Latest Error Messages from y_finance', scope.download['yf_anomolies']  , 'scope.download.yf_anomolies' )






