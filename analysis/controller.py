



import streamlit as st


from ticker.controller import single_loader, multi_loader

# from analysis.ticker_data import analysis_df

from analysis.volume import view_volume_page
from analysis.research import company_general, dividends, fundamental, general, market_info


from charts.finance import financial_chart_tutorial
from charts.candlestick import plot_candlestick_seperate_volume, plot_candlestick
from charts.line import plot_line_chart

from ticker.y_finance import fetch_yfinance_metadata

# ==============================================================================================================================================================
# Mult Ticker Analysis
# ==============================================================================================================================================================
def multi_tickers_page(scope):
	st.header('Analysis - Multiple Tickers')

	multi_loader(scope)

	st.info('I expect the output of any analysis is going to be a list of stocks for further analysis')

	# we migth be able to jumpt to single stock analysis from any list - that migth be cool!!!

	# if len(scope.selected['ticker_list']) > 0:
	# 	st.info('We have some tickers')
	# else:
	# 	st.error('Add some tickers')


# ==============================================================================================================================================================
# Single Ticker Analysis
# ==============================================================================================================================================================
def single_ticker_page(scope):
	st.header('Single Ticker Analysis')

	single_loader(scope, 'single')

	st.markdown("""---""")
	
	# print ('ticker list in scope = ', scope.selected['ticker_list'])
	ticker = scope.selected['single']['ticker_list'][0]
	
	if ticker in list(scope.ticker_data_files.keys()):
		st.write('This is where we do some stuff')
		# col1,col2 = st.columns([2, 10])
		# df_row_limit = None if scope.analysis_apply_limit=='False' else int(scope.analysis_row_limit)

		df_row_limit = int(scope.analysis_row_limit)

		# share_data = analysis_df(scope, ticker, df_row_limit)  # this only gets refreshed if the ticker changes or the no of rows changes

		# TODO - this might be the place to add measures - but only if the have not already been add
		# so - we might collect the measures from the screen.....
		# add the measures to a list and pass the list to a cached function that is responsible
		# 	a) adding any new measures
		# 	b) deleted any removed measures
		# ????? should we record the selected measures if we change screen --- maybe the widgets will keep it 
		# view_alternative_indicators(scope)


		# indicator_selectors(scope)
		
		# Financial Chart adds the following
		# Index(['date', 'open', 'high', 'low', 'close', 'volume', 'MA20', 'MA5'], dtype='object')

		# financial_chart_tutorial(share_data)

		# plot_candlestick_seperate_volume(share_data)

	# 	plot_candlestick(share_data)
		
	# 	plot_line_chart(share_data)

# ==============================================================================================================================================================
# Intra Day Analysis
# ==============================================================================================================================================================
# TODO - this will need to be moved later
from analysis.intraday import add_sma

from analysis.intraday import indicator_selectors, alternative_indicators

def intraday_page(scope):
	st.header('Intra Day Analysis')
	
	single_loader(scope, 'intraday')
	
	st.markdown("""---""")

	ticker = scope.selected['intraday']['ticker_list'][0]


	if ticker in list(scope.ticker_data_files.keys()):
		# col1,col2 = st.columns([2, 10])
		# df_row_limit = None if scope.analysis_apply_limit=='False' else int(scope.analysis_row_limit)

		print('We are here')
		# share_data = analysis_df(scope, ticker, df_row_limit)  # this only gets refreshed if the ticker changes or the no of rows changes

		# TODO - this might be the place to add measures - but only if the have not already been add
		# so - we might collect the measures from the screen.....
		# add the measures to a list and pass the list to a cached function that is responsible
		# 	a) adding any new measures
		# 	b) deleted any removed measures
		# ????? should we record the selected measures if we change screen --- maybe the widgets will keep it 
		# view_alternative_indicators(scope)


		# indicator_selectors(scope)
		
		# Financial Chart adds the following
		# Index(['date', 'open', 'high', 'low', 'close', 'volume', 'MA20', 'MA5'], dtype='object')

		# financial_chart_tutorial(share_data)

		# plot_candlestick_seperate_volume(share_data)

	# 	plot_candlestick(share_data)
		
	# 	plot_line_chart(share_data)


# ==============================================================================================================================================================
# Volume Prediction
# ==============================================================================================================================================================


def volume_page(scope):
	st.title('Predict Closing Volume to End of Today')
	st.write('Extrapolating the Current Volume to the End of today')
	single_loader(scope, 'volume' )
	st.markdown("""---""")
	
	view_volume_page(scope)


# ==============================================================================================================================================================
# Company Research
# ==============================================================================================================================================================

# TODO - delete this later
from analysis.research import plot_basic_chart

def research_page(scope):
	st.header('Company Research')
	single_loader(scope, 'research' )
	st.markdown("""---""")
	
	ticker = scope.selected['research']['ticker_list'][0]

	if ticker != 'select a ticker':	
		meta_data, info, divs = fetch_yfinance_metadata(ticker)

		company_general(info)
		dividends(divs)
		fundamental(info)
		general(info)
		plot_basic_chart(scope)		
		market_info(info)
		# view_ticker_file(scope, ticker)


