
# ========================================================================================================================================================================
# Core Application Processes
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 	Initial Application load of the app performs the following processes :

# 		a) Establishment of Scope object
# 		b) Rendering the initial web page structure (based on the scope)
# 		c) Loading the exisiting (or creating an empty if none exists) Ticker Index
#		d) Load the User Configurable Settings

# 	This results in the application rendering the basic application structure in a web browser

# 	The user then decides between the various options including :
#		
# Single Share Ticker Analysis or research on :
# 				b) End Of Day (EOD) analysis
#				c) Intra Day  (ED)  analysis
# 				e) End Of Day (EOD) prediction of volume
# 				d) Researching a Company

# 		Multiple Share Ticker Analysis on either:
# 				a) The entire share market
#				b) An entire industry within the share market
# 				c) A Specific Ticker or Tickers
# 		
# 
# 	Process after selecting the appropriate option
#				1) Select a ticker or group of tickers (selections are independent for each option)
#				2) Load existing share data 							( AUTO loaded after selecting a ticker )
#				3) Download share data and append to any existing date  ( AUTO saved for next time )
#				4) Display Charts
#


#	Application processing
#				a) copy selected ticker(s) share data from the share_data_files dictionary
#				b) 
#
#				ok - now it gets tough
#				do we add the metrics before trying to render the charts????
#
#
#


