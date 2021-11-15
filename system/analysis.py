import streamlit as st

from system.reports import render_3_columns


def scope_analysis(scope):
	# Analysis Variables
	# Analysis_dfs are stored in the page variables

	scope.analysis_row_limit = 300
	# scope.analysis_apply_limit = False


def render_analysis(scope):
	st.subheader('Analysis Variables')
	render_3_columns( 'Analysis Row Limit', scope.analysis_row_limit, 'analysis_row_limit' )



def render_analysis_row_limit(scope): # limit_analysis

	previous_selection = int(scope.analysis_row_limit)

	input_analysis_days = st.number_input( 	
										'limit analysis dataframes to this many rows (by date - most recent)', 
										min_value=0, 
										# max_value=max_value, 
										value=previous_selection,
										key='95'
										)  

	# Store the selection for smoother transition between pages
	scope.analysis_row_limit = input_analysis_days



def render_all_analysis_files(scope): # 
	st.subheader('Loaded and downloaded Ticker data.')
	col1,col2 = st.columns([6,2])
	with col1: st.write('Loaded and Downloaded share data stored in > ')
	with col2: st.write('< ticker_data_files >')	
	st.markdown("""---""")

	list_of_analysis_tickers = list(scope.selected['multi']['analysis_df'].keys())
	list_of_analysis_tickers.sort()


	for ticker in list_of_analysis_tickers:
		analysis_df = scope.selected['multi']['analysis_df'][ticker]
		analysis_df.sort_values(by=['date'], inplace=True, ascending=False)
		no_of_rows = str(len(analysis_df))
		my_expander = st.expander(label=(ticker+' ( ' + no_of_rows + ' )'))
		# TODO - this is where the sorting of the dataframes should occur - we can probably do it in one go and then undo it at the end
		my_expander.dataframe(analysis_df, 2000, 2000)	

def render_an_analysis_file(scope): # WIP
	ticker = scope.selected[scope.display_page]['ticker_list'][0]
	analysis_df = scope.selected[scope.display_page]['analysis_df'][ticker]
	analysis_df.sort_values(by=['date'], inplace=True, ascending=False)
	no_of_rows = str(len(analysis_df))
	my_expander = st.expander(label=(ticker+' ( ' + no_of_rows + ' )'), expanded=True)
	# TODO - this is where the sorting of the dataframes should occur - we can probably do it in one go and then undo it at the end
	my_expander.dataframe(analysis_df, 2000, 2000)	