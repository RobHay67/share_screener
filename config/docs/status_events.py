# Specific Events occur which require the ticker data and/or the columns attached to the
# ticker data, to require refreshing. We also track missing tickers with these events.


# The events are :
#																													------- missing_tickers ------
# ---- Event -----------------		tickers[ticker].config				page[replace_df]		page[column_adders]		local	cloud	list	errors
# Load a ticker						create empty						....				....					......	......	......	......
# combine downloaded data			............						True				True					......	......	......	......
# download data						............						....				....					remove	remove	remove	......
# data fails to download			............						....				....					......	append	append	append			
# activate a column adder			............						....				True					......	......	......	......
# edit a column adder variable		............						....				True					......	......	......	......
# edit the page row limit			............						True				True					......	......	......	......
# no local file						............						....				....					append	......	append	append
# save a ticker						............						....				....					remove	......	remove	......


# Empty Scope.tickers[ticker] as follows
# scope.tickers[ticker] = {
# 							df	:Dataframe containing all OHLCV 
# 							page	:{
# 									df				: Dataframe - limited by row limit and containing relevant page column adders,
#									replace_df 		: True or False	as set by the above events
#									type_col_adder 	: charts or trials	relevant column adders for the page
#									column_adders	: Dictionary of appropriate columns adders and there active status

# 								  }
#  						}



# Current page and usage of column adders
# page		Objects
# --------------------------------------------
# chart	charts and overlays
# intraday	none
# volume	none
# research	none
# screener	trials

