import streamlit as st

from apps.config_app.three_cols import three_cols


def view_folders(scope):

	diff_col_size = [2,6,2]

	st.subheader('Folders')
	three_cols( 'Project', scope.files['folders']['project'], 'scope.files.folders.project', diff_col_size )
	three_cols( 'Files', scope.files['folders']['files'], 'scope.files.folders.files', diff_col_size )
	three_cols( 'Share Data', scope.files['folders']['tickers'], 'scope.files.folders.tickers', diff_col_size )
	three_cols( 'Results Analysis', scope.files['folders']['results_analysis'], 'scope.files.folders.results_analysis', diff_col_size )
	three_cols( 'Website Output', scope.files['folders']['website'], 'scope.files.folders.website', diff_col_size )

	st.subheader('Paths to Specific Objects')
	three_cols( 'Path for Share Index File', scope.files['paths']['ticker_index'], 'scope.files.paths.ticker_index', diff_col_size )
	three_cols( 'Path for Website Output File', scope.files['paths']['website'], 'scope.files.paths.website', diff_col_size )
	three_cols( 'Path for Share Data File', scope.files['paths']['ticker_data'], 'scope.files.paths.ticker_data', diff_col_size )


