


# ========================================================================================================================================================================
# Primary Objects
#  description									type					Description
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ticker_index 									DataFrame  				A list of all tickers available to the application
# ticker_data_files								dict of DataFrames		All Share Data files indexed by Ticker Code
# scope.selected[page]['screener_df'][ticker]	DataFrame				Copy of selected ticker(s) from share_data_files with all metrics added for screening
# scope.selected[page]['plot_df]['ticker]		DataFrame				Copy of selected ticker(s) from share_data_files with all metrics added for plotting


#																		-----------------------------
#																		|							|
#	dictionary of all loaded and downloaded OHLCV ticker data			|  scope.ticker_data_files  |	
#																		|							|
#																		-----------------------------
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
#											|    screener_df   	|			|      chart_df   	|		|      chart_df   	|
#											|					|			|					|		|					|
#											---------------------			---------------------		---------------------
#
# example									cba 	NAB		anz				ifl				NAB			NAB				wbc
#
#
# Events that change the data
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Change in the < page_row_limit >			CR+CaM	CR+CaM	CR+CaM			CR+CaM			CR+CaM		CR+CaM			CR+CaM		= refresh all tickers and rerun all active metrics
# Download new ticker for cba and NAB		CR+CaM	CR+CaM	------			------			CR+CaM		CR+CaM			------		= just refresh the tickers that have changed
# Activate overlay or 2nd chart				------	------	------			CsM				CsM			CsM				CsM			= recalculate the specific metrics only	for NON screener pages							
# Update value in overlay or 2nd chart		------	------	------			CsM				CsM			CsM				CsM			= recalculate the specific metrics only	for NON screener pages	
# Activate Screener Metric					CsM		CsM		CsM				------			------		------			------		= recalculate the specific metrics only	for screener page
# Update Screener Metric value 				CsM		CsM		CsM				------			------		------			------		= recalculate the specific metrics only	for screener page

# KEY
# CR 	= copy and replace the ticker_data from < scope.ticker_data_file >
# CaM 	= recalculate ALL     active metrics      for every Ticker in the page 
# CsM	= recalculate changed active metrics ONLY for every Ticker in the page 


