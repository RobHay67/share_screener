import streamlit as st

from views.header.add_columns.update_files import replace_df_and_add_columns


def render_progress_bar(scope, page):

	if len(scope.pages[page]['worklist']) == 0:
		st.write('No Files available - select some')
	else:
		replace_df_and_add_columns(scope, page)