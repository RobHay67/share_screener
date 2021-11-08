
import streamlit as st


# -----------------------------------------------------------------------------------------------------------------------------------
# Output Ticker Iteration to Browser
# -----------------------------------------------------------------------------------------------------------------------------------
def render_results(scope, output=None, result=None, final_print=False, passed='', passed_2='', failed='' ):
	# I think what we do here is just build 3 list and save them

	if output == None:
		# this is the initial run so set all the defails
		# width_of_next_output = 0
		scope.result_passed=passed
		scope.result_passed_2=passed_2
		scope.result_failed=failed
		scope.result_passed_count = 0
		scope.result_passed_2_count = 0
		scope.result_failed_count = 0

	# Store the results
	if result=='passed':
		scope.result_passed = scope.result_passed + str(output) + ' '
		scope.result_passed_count +=1
	elif result=='passed_2':
		scope.result_passed_2 = scope.result_passed_2 + str(output) + ' '
		scope.result_passed_2_count +=1
	elif result=='failed':
		scope.result_failed = scope.result_failed + str(output) + ' '
		scope.result_failed_count +=1

	# print (scope.result_passed)
	if final_print: 
		scope.result_passed = scope.result_passed + ' < ( ' + str(scope.result_passed_count) + ' )'
		scope.result_passed_2 = scope.result_passed_2 + ' < ( ' + str(scope.result_passed_2_count) + ' )'
		scope.result_failed = scope.result_failed + ' < ( ' + str(scope.result_failed_count) + ' )'

		if scope.result_passed_count > 0: st.info(scope.result_passed)
		if scope.result_passed_2_count > 0: st.warning(scope.result_passed_2)

		# if len(scope.result_failed) != 0:
		if scope.result_failed_count > 0: st.error(scope.result_failed)



# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Render Re-Usable Sections
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def render_selectors_for_single_ticker(scope, ticker_variable):
	col1,col2,col3,col4,col5 = st.columns([2,2,1.2,2,4.8])
	
	dropdown_list = scope.dropdown_ticker
	index_of_ticker = dropdown_list.index(scope.ticker_for_company_profile)

	with col1: 
		ticker = st.selectbox ( 'Select Ticker', 
								dropdown_list, 
								index=index_of_ticker, 
								help='Select a ticker. Start typing to jump within list'
								) 
	

	scope[ticker_variable] = ticker									# Store the selection for next session
	
	if ticker != 'select a ticker':	
		st.header( scope.ticker_index_file.loc[ticker]['company_name'] )	

		with col3: load_tickers 	= st.button( 'Load File')
		with col3: download_tickers = st.button(('Add ' + str(int(st.download_days)) + ' days'))

		with col4: st.button('Clear Messages')

		scope.ticker_list = [ticker]
		# TODO - we need to set a flag that resets the ticker list button in the sidebar
		scope.download_industries = ['random_tickers']

		if load_tickers : 
			load_ticker_data_files(scope)

		if download_tickers:
			load_and_download_ticker_data(scope)



