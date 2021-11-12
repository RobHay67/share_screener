



import streamlit as st


from analysis.data_loaders import single_loader, multi_loader

from analysis.share_data import extract_ticker

from charts.finance import financial_chart_tutorial
from charts.candlestick import plot_candlestick_seperate_volume, plot_candlestick
from charts.line import plot_line_chart


# ==============================================================================================================================================================
# Mult Ticker Analysis
# ==============================================================================================================================================================
def render_multi_page(scope):
	st.header('Analysis - Multiple Tickers')

	multi_loader(scope)

	st.info('I expect the output of any analysis is going to be a list of stocks for further analysis')

	# we migth be able to jumpt to single stock analysis from any list - that migth be cool!!!

	# if len(scope.ticker_list) > 0:
	# 	st.info('We have some tickers')
	# else:
	# 	st.error('Add some tickers')


# ==============================================================================================================================================================
# Single Ticker Analysis
# ==============================================================================================================================================================
def render_single(scope):
	st.header('Analysis - Single Ticker')

	single_loader(scope, 'single')

	# render_ticker_data_file(scope, ticker)


# ==============================================================================================================================================================
# Intra Day Analysis
# ==============================================================================================================================================================
# TODO - this will need to be moved later
from analysis.intraday import add_sma

from analysis.intraday import indicator_selectors, alternative_indicators

def render_intraday(scope):
	st.header('Intra Day Analysis')
	
	single_loader(scope, 'intraday')
	
	st.markdown("""---""")

	ticker = scope.ticker['intraday']


	if ticker in list(scope.share_data_files.keys()):
		# col1,col2 = st.columns([2, 10])
		df_row_limit = None if scope.analysis_apply_limit=='False' else int(scope.analysis_limit_share_data)

		share_data = extract_ticker(scope, ticker, df_row_limit)  # this only gets refreshed if the ticker changes or the no of rows changes

		# TODO - this might be the place to add measures - but only if the have not already been add
		# so - we might collect the measures from the screen.....
		# add the measures to a list and pass the list to a cached function that is responsible
		# 	a) adding any new measures
		# 	b) deleted any removed measures
		# ????? should we record the selected measures if we change screen --- maybe the widgets will keep it 
		# render_alternative_indicators(scope)


		# indicator_selectors(scope)
		
		# Financial Chart adds the following
		# Index(['date', 'open', 'high', 'low', 'close', 'volume', 'MA20', 'MA5'], dtype='object')

		# financial_chart_tutorial(share_data)

		plot_candlestick_seperate_volume(share_data)

	# 	plot_candlestick(share_data)
		
	# 	plot_line_chart(share_data)


# ==============================================================================================================================================================
# Volume Prediction
# ==============================================================================================================================================================
from datetime import datetime
from datetime import timedelta
import pytz

from analysis.volume import render_volume_prediction

def render_volume(scope):
	st.title('Predict Closing Volume to End of Today')
	st.write('Extrapolating the Current Volume to the End of today')
	single_loader(scope, 'volume' )
	st.markdown("""---""")
	
	ticker = scope.ticker['volume']

	local_time		= datetime.now()													# Current local time
	market_timezone = scope.market_opening_hours[scope.share_market]['timezone']		# Timezone for the share market
	market_time 	= datetime.now(pytz.timezone(market_timezone))						# Current Market time

	if ticker != 'select a ticker':	
		# Ticker Master Data
		ticker_opening_time 	= scope.ticker_index_file.loc[ticker]['opening_time']
		ticker_minutes_per_day 	= scope.ticker_index_file.loc[ticker]['minutes_per_day']

		# Current Volume setter
		col1,col2 = st.columns([2,10])
		with col1: ticker_current_volume = st.number_input("Current Volume", value=0, format="%d")

		# Build the open time for this ticker
		open_hour 	= int(ticker_opening_time[:2])
		open_minute = int(ticker_opening_time[3:5])
		open_second = int(ticker_opening_time[6:8])
		ticker_open_time=market_time.replace(hour=open_hour, minute=open_minute, second=open_second)
		
		# minutes difference
		diff_in_seconds = (market_time - ticker_open_time).total_seconds()
		minutes_elapsed = divmod(diff_in_seconds, 60)[0]
		if minutes_elapsed > ticker_minutes_per_day: minutes_elapsed = ticker_minutes_per_day
		
		# Now extrapolate
		ticker_average_vol_per_minute = ticker_current_volume / minutes_elapsed
		ticker_remaining_minutes = ticker_minutes_per_day - minutes_elapsed
		if ticker_remaining_minutes < 0: ticker_remaining_minutes = 0
		extrapolated_daily_volume = "{:8,.0f}".format(ticker_average_vol_per_minute * ticker_minutes_per_day)
		volume_to_date =  "{:8,.0f}".format(ticker_current_volume)
		
		# calc the closing time for this ticker
		ticker_closing_time = datetime.strptime(ticker_opening_time, '%H:%M:%S')
		ticker_closing_time = ticker_closing_time + timedelta(minutes=ticker_minutes_per_day)

		render_volume_prediction(ticker_open_time, minutes_elapsed, ticker_remaining_minutes, ticker_closing_time, volume_to_date, ticker_average_vol_per_minute, extrapolated_daily_volume, ticker_minutes_per_day)



# ==============================================================================================================================================================
# Company Research
# ==============================================================================================================================================================
from tickers.y_finance import fetch_yfinance_metadata
from analysis.company_info import company_general, dividends, fundamental, general, market_info
from web.ticker_file import render_ticker_file
# TODO - delete this later
from analysis.company_info import plot_basic_chart



def render_research(scope):
	st.header('Company Research')
	single_loader(scope, 'research' )
	st.markdown("""---""")
	
	ticker = scope.ticker['research']

	if ticker != 'select a ticker':	
		meta_data, info, divs = fetch_yfinance_metadata(ticker)

		company_general(info)
		dividends(divs)
		fundamental(info)
		general(info)
		plot_basic_chart(scope)		
		market_info(info)
		# render_ticker_file(scope)
		render_ticker_file(scope, ticker)


