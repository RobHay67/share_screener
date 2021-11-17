
import streamlit as st



from ticker.downloader.y_finance import download_from_yahoo_finance
from ticker.downloader.combiner import combine_loaded_and_download_ticker_data

# ==============================================================================================================================================================
# Download Controller : Donwload Ticker Data from y_finance
# ==============================================================================================================================================================
def load_and_download_ticker_data( scope ):
	print ( '\033[91m' + 'Loading before downloading has been turned off - confirm this is what we want' + '\033[0m' )
	st.markdown("""---""")

	# load_ticker_data_files(scope, ticker_list)				# TODO playing with not doing this - make it the users responsibility
	download_from_yahoo_finance(scope )
	combine_loaded_and_download_ticker_data(scope)
	# check_share_data_for_missing_dates( scope )				# TODO Not Sure this is Required anymore

	scope.download_industries = [] 								# Reset for next download







