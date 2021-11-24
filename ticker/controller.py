from results.view import results
from ticker.path import generate_path_for_share_data_file
from ticker.helpers.verify_file import verify_file_exists_before_loading


from ticker.y_finance import download_from_yahoo_finance
from ticker.combiner import combine_loaded_and_download_ticker_data




def load_tickers(scope, col6, ticker=None):				# will be given a single ticker or a list of tickers

	results(scope, 
			passed='LOADED Share Data Files > ', 
			failed='MISSING Share Data Files for > ', 
			passed_2='na',
			)

	ticker_list = [ticker] if ticker != None else scope.pages['multi']['ticker_list']

	for ticker in ticker_list:
		if ticker not in scope.ticker_data_files:					# Ensure it has not already been loaded
			print ( '\033[92m' + ticker + ' > loading file\033[0m')
			generate_path_for_share_data_file(scope, ticker )
			verify_file_exists_before_loading(scope, ticker)
		else:
			print ( '\033[92m' + ticker + ' > skipping load\033[0m')

	results(scope, 'Finished', final_print=True )
	
	view_load_results(scope, col6)



def view_load_results(scope, col6):
	import streamlit as st
	with col6:
		if scope.results['passed_count'] > 0: st.info(scope.results['passed'])
		if scope.results['passed_2_count'] > 0: st.warning(scope.results['passed_2'])
		if scope.results['failed_count'] > 0: st.error(scope.results['failed'])






def download_tickers(scope):
	# scope.download_industries = ['random_tickers']			# used for y_finance downloading - set at beginning of process
	# load_and_download_ticker_data(scope)						# loading of existing data has already occured
	download_from_yahoo_finance(scope)
	combine_loaded_and_download_ticker_data(scope)
	# check_share_data_for_missing_dates( scope )				# TODO Not Sure this is Required anymore
	scope.download_industries = [] 								# Reset for next download

	page = scope.display_page
	scope.pages[page]['refresh_chart_df'] = True


