


# ========================================================================================================================================================================
# Primary Objects
#  description									type					Description
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ticker_index 									DataFrame  				A list of all tickers available to the application
# ticker_data_files								dict of DataFrames		All Share Data files indexed by Ticker Code
# scope.selected[page]['df'][ticker]			DataFrame				Copy of selected ticker(s) from share_data_files with all add_cols added for screening
# scope.selected[page]['df]['ticker]			DataFrame				Copy of selected ticker(s) from share_data_files with all add_cols added for plotting


#																		---------------------------------
#																		|								|
#	dictionary of all loaded and downloaded OHLCV ticker data			|   scope.data['ticker_files']  |	
#																		|								|
#																		---------------------------------
#																					|
#																					|
#							  										copy specific <ticker_data_files> only
# 														specific tickers stored in < scope.pages[page]['ticker_list] >
# 																Limit rows to < page_row_limit > default = 100	
#																   /				|				 \
#															  	  /					|			 	  \
#																 /					|			  	   \
#																/					|			   		\
#											---------------------			---------------------		---------------------
#											| 	 scope.pages	|			| 	 scope.pages	|		| 	 scope.pages	|
# 											|	 ['screener']	|			|	  ['single']	|		|	['intra_day']	|
#											|    	[df]   		|			|     	[df]   		|		|      [df]   		|
#											|					|			|					|		|					|
#											---------------------			---------------------		---------------------
#
# example (page.ticker_list)				[cba 	NAB		anz ]			[ifl			NAB ]		[NAB			wbc ]
#
#
# Events that change the data
											
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Load ticker for cba						T-r_df	T-r_dfl ------			------			-------		-------			-------		= refresh the tickers that have changed
#											T-r_col	T-r_col ------			------			-------		-------			-------
# Download new ticker for cba + NAB			T-r_df	T-r_dfl ------			-------			T-r_df		T-r_df			-------		= refresh the tickers that have changed
#											T-r_col	T-r_col ------			------			-------		-------			-------
# Change the < page_row_limit >				T-r_all T-r_all T-r_all			T-r_all			T-r_all		T-r_all			T-r_all		= refresh all tickers and rerun all active add_cols
# Activate overlay or 2nd chart				------	------	------			T-r_col			T-r_col		T-r_col			T-r_col		= recalculate the specific add_cols only	for NON screener pages							
# Update value in overlay or 2nd chart		------	------	------			T-r_col			T-r_col		T-r_col			T-r_col		= recalculate the specific add_cols only	for NON screener pages	
# Activate a col_adder						T-r_col	T-r_col	T-r_col			-------			-------		-------			-------		= recalculate the specific add_cols only	for screener page
# Change col_adder value 					T-r_col	T-r_col	T-r_col			-------			-------		-------			-------		= recalculate the specific add_cols only	for screener page
# Replace the page_df on single page		R-r_df	-------	-------			-------			-------		-------			-------
# Rerun the column adder single page		R-r_col	-------	-------			-------			-------		-------			-------		
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
# KEY		Description				Pages		Tickers		Dataframe									add_columns	replace_cols							Replace DF Func		Replace Cols Func		
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
# T-r_df 	tag to replace df		All			Specific	set_replace_df_status_for_ticker			------------------------------------------------	replace_dfs			---------------------	
# T-r_col	tag to add_cols			All			Specific	-----------------------------------------	set_replace_col_status_for_ticker					--------------- 	replace_cols
# t-col		change col_adder		All			All			-----------------------------------------	set_replace_col_status_for_col_adder					---------------		replace_cols
# t-ALL 	replace all dfs	& cols	All			All			set_replace_df_status_for_all_tickers 		set_replace_cols_status_for_all_tickers 				replace_dfs			replace_cols
# Rdf		replace the DF			Specific	Specific	set_replace_df_status_for_ticker_and_page	------------------------------------------------	
# Rcol		replace the cols		Specific	Specific	-----------------------------------------	set_replace_col_adder_status_for_ticker_and_page
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
# T			= tag the object
# R			= perform the actual replacement (results in a False status)
# r_df		= scope.pages[page]['replace_dfs']
# r_col		= scope.pages[page]['replace_cols']
# r_all		= both the scope.pages[page]['replace_dfs'] and scope.pages[page]['replace_cols'] dictionaries


# tag the add_cols when they have been run													???? - updated function
# update the scope.page_metrics after changes made 											????
# change the test after editing scope.page_metrics											????
# change the chart  after editing scope.page_metrics										????


