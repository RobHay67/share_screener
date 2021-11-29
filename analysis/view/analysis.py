import streamlit as st

from pages.view.three_cols import three_cols



def view_analysis(scope):
	st.subheader('Analysis Settings')
	three_cols( 'Limit for the Number of (recent) rows in any Analysis', scope.analysis_row_limit, 'analysis_row_limit' )


