


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
# x Change the < page_row_limit >			CRa+CaM	CRa+CaM	CRa+CaM			CRa+CaM			CRa+CaM		CRa+CaM			CRa+CaM		= refresh all tickers and rerun all active metrics
# x Load  ticker for cba					CRs+CsM	------	------			------			------		------			------		= refresh the tickers that have changed
# x Download new ticker for cba or NAB		CRs+CsM	CRs+CsM	------			------			CRs+CsM		CRs+CsM			------		= refresh the tickers that have changed
# x Activate overlay or 2nd chart			------	------	------			CsM				CsM			CsM				CsM			= recalculate the specific metrics only	for NON screener pages							
# x Update value in overlay or 2nd chart	------	------	------			CsM				CsM			CsM				CsM			= recalculate the specific metrics only	for NON screener pages	
# x Activate Screener Metric				CsM		CsM		CsM				------			------		------			------		= recalculate the specific metrics only	for screener page
# x Update Screener Metric value 			CsM		CsM		CsM				------			------		------			------		= recalculate the specific metrics only	for screener page

# KEY
# CRa 	= Copy and Replace ALL     ticker_data from < scope.ticker_data_file >				DONE - Function Added
# CRs 	= Copy and Replace changed ticker_data from < scope.ticker_data_file >				DONE - Function Added
# CaM 	= re Calculate ALL     active Metrics for every Ticker in the page 					DONE - Function Added
# CsM	= re Calculate changed active Metrics for every Ticker in the page 					DONE - Function Added

# TODO
# tag the metrics when they have been run													DONE - updated function
# update the scope.page_metrics after changes made 											DONE
# change the ADD_METRIC_DATA after editing scope.page_metrics								DONE
# change the ADD_CHART_DATA  after editing scope.page_metrics								DONE