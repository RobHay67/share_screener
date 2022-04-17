
import streamlit as st

from widgets.constructors.ohlcv_trend import render_ohlcv_trend


def render_screener_tests(scope):
	
	st.markdown("""---""")
	st.write('**Fundamental Analysis**')

	with st.expander(label='Annual General Meeting', expanded=False):
		st.write('This will be the criteria')

	with st.expander(label='Divdends - Dividend Yield', expanded=False):
		st.write('This will be the criteria')

	with st.expander(label='Price to Earnings Ratio - P/E', expanded=False):
		st.write('Dividend per share / Earning per share')

	with st.expander(label='Current Asset Ratio', expanded=False):
		st.write('This will be the criteria')

	with st.expander(label='Debt to Equity Ratio', expanded=False):
		st.write('This will be the criteria')

	with st.expander(label='Cash Flow - Operating', expanded=False):
		st.write('This will be the criteria')

	with st.expander(label='Cash Flow - Capital', expanded=False):
		st.write('This will be the criteria')
	
	with st.expander(label='Cash Flow - Financial', expanded=False):
		st.write('This will be the criteria')


	st.markdown("""---""")
	st.write('**Ticker Technical Performance Criteria**')

	with st.expander(label='OHLCV', expanded=True):

		# form = st.form(key='my_form')
		# form.text_input(label='Criteria for OHLCV ticker values')
		
		# st.write('This will be the criteria')
		# st.header('This will be the add_cols selection page')

		with st.form(key='my_form'):
			text_input = st.text_input(label='Criteria for OHLCV ticker values')

			col1,col2,col3,col4,col5,col6,col7,col8 = st.columns([1,1,1,1,1,1,1,1])
		
			with col1: render_ohlcv_trend(scope, 'trend_open',   'open')
			with col2: render_ohlcv_trend(scope, 'trend_high',   'high')
			with col3: render_ohlcv_trend(scope, 'trend_low',    'low')
			with col4: render_ohlcv_trend(scope, 'trend_close',  'close')
			with col5: render_ohlcv_trend(scope, 'trend_volume', 'volume')

			submit_button = st.form_submit_button(label='Apply OHLCV Criteria')

			# if submit_button:
			# 	print ( 'X'*100)
			# 	print( scope['config']['tests']['trend_high']['add_columns']['duration'] )

			# 	ticker_list = scope.pages['screener']['ticker_list']

				# for ticker in scope.pages['screener']['ticker_list']:
				# 	print(ticker)
					# print(scope.pages['screener'][])



				# 	print(scope.pages['screener']['renew']['tests'][ticker]['trend_high'] )

				# for page in scope.pages['page_list']:
				# 	print(page)
				# 	if page == 'screener':													# all chart relevant pages
				# 		for ticker in scope.pages[page]['renew']['tests'].keys():			# iterate through each ticker
				# 			print(scope.pages[page]['renew']['tests'][ticker]['trend_high'] )

			# This is the original code - i think I hjave mucked up the names
			# TODO 
			# if submit_button:
			# 	print ( 'X'*100)
			# 	print( scope['screener_tests']['trend_high']['metrics']['duration'] )

			# 	for page in scope.pages.keys():
			# 		print(page)
			# 		if page == 'screener':													# all chart relevant pages
			# 			for ticker in scope.pages[page]['add_metric_data'].keys():			# iterate through each ticker
			# 				print(scope.pages[page]['add_metric_data'][ticker]['trend_high'] )

	




	with st.expander(label='Simple Moving Averages (SMA)', expanded=False):
		st.write('This will be the criteria')
	

	with st.expander(label='Relative Strength Index (RSI)', expanded=False):
		st.write('This will be the criteria')

	with st.expander(label='Stochastic Oscillato', expanded=False):
		st.write('This will be the criteria')

	with st.expander(label='Moving Average - Convergence / Divergence (MACD)', expanded=False):
		st.write('This will be the criteria')

	with st.expander(label='MACD - Volume', expanded=False):
		st.write('This will be the criteria')





from pages.view.three_cols import three_cols


