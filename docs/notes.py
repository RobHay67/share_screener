
# red         = '\033[91m'
# green       = '\033[92m'
# yellow      = '\033[93m'
# blue        = '\033[94m'
# purple      = '\033[95m'
# cyan        = '\033[96m'
# white 		= '\033[0m'

# downloading new share data is resulting in these records being added to the share Index file - why???

multi,,,,,,,,set_for_download,,,
single,,,,,,,,set_for_download,,,
intraday,,,,,,,,set_for_download,,,
volume,,,,,,,,set_for_download,,,
research,,,,,,,,set_for_download,,,
RESEARCH,,,,,,,,delisted,,,
VOLUME,,,,,,,,delisted,,,
INTRADAY,,,,,,,,delisted,,,
MULTI,,,,,,,,delisted,,,
SINGLE,,,,,,,,delisted,,,



# ========================================================================================================================================================================
# Application Module Structure
# 
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# Initial loader	app.py
#					|
#					1) scope.py    		( Initial config for streamlit and global variables required by the app )
#					2) navigation.py	( renders the appropriate page based on the sidebar button selectors )



#					analysis_intraday.py
#					analysis_multi.py
#					analysis_research.py
#					analysis_single.py
#					analysis_volume.py

#					indicators.py
#					navigation.py
#					scope.py
#					ticker_data.py
#					ticker_index.py
#					web_charts.py
#					web_components.py
#					web_results.py

# Common Browser 





# ========================================================================================================================================================================
# Core Application Processes
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 	Initial Application load of the app performs the following processes :

# 		a) Establishment of Scope object
# 		b) Rendering the initial web page structure (based on the scope)
# 		c) Loading the exisiting (or creating an empty if none exists) Ticker Index

# 	This results in the application rendering the basic application structure in a web browser

# 	The user then decides between the various options including :
# 		Multiple Share Ticker Analysis on either:
# 				a) The entire share market
#				b) An entire industry within the share market
# 				c) A Specific Ticker or Tickers
# 		Single Share Ticker Analysis or research on :
# 				b) End Of Day (EOD) analysis
#				c) Intra Day  (ED)  analysis
# 				e) End Of Day (EOD) prediction of volume
# 				d) Researching a Company
# 
# 	Process after selecting the appropriate option
#				1) Select a ticker or group of tickers (selections are independent for each option)
#				2) Load existing share data
#				3) Download share data (and append to any existing date - auto saved for next time)
#
#	Application processing
#				a) copy selected ticker(s) share data from the share_data_files dictionary
#				b) 
#
#				ok - now it gets tough
#				do we add the measures before trying to render the charts????
#
#
#


