import streamlit as st

from views.scope_var import three_cols

def view_folders(scope):

	diff_col_size = [2,6,2]

	st.subheader('Folders')
	three_cols( 'Project', scope.folder_project, 'folder_project', diff_col_size )
	three_cols( 'Share Data', scope.folder_share_data, 'folder_share_data', diff_col_size )
	three_cols( 'Results Analysis', scope.folder_results_analysis, 'folder_results_analysis', diff_col_size )
	three_cols( 'Website Output', scope.folder_website, 'folder_website', diff_col_size )

	st.subheader('Paths to Specific Objects')
	three_cols( 'Path for Share Index File', scope.path_ticker_index, 'path_ticker_index', diff_col_size )
	three_cols( 'Path for Website Output File', scope.path_website_file, 'path_website_file', diff_col_size )
	three_cols( 'Path for Share Data File', scope.path_ticker_data_file, 'path_ticker_data_file', diff_col_size )
