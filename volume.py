import streamlit as st
from datetime import datetime
from datetime import timedelta
import pytz





def render_volume_page(scope):
	st.title('Predict Closing Volume to End of Today')

	st.write('Extrapolating the Current Volume to the End of today')
	st.markdown("""---""")
	# Current local time
	local_time=datetime.now()

	# Current Market time
	market_timezone = scope.market_opening_hours[scope.share_market]['timezone']
	market_time = datetime.now(pytz.timezone(market_timezone))

	col1,col2,col3 = st.columns([1,1,1])
	with col1:st.write('Local Time')
	with col2:st.write(str(local_time.strftime('%H:%M:%S %p')))
	with col3:st.write(str(local_time.strftime('%Y-%m-%d')))

	with col1:st.write('Market Time')
	with col2:st.subheader(str(market_time.strftime('%H:%M:%S %p')))
	with col3:st.write(str(market_time.strftime('%Y-%m-%d')))
	
	st.markdown("""---""")


	# -----------------------------------------------------------------------------------
	# Extract master data from share index file for the first ticker in the list pos=[0]
	if len(scope.ticker_list) > 0:
		ticker_1 = scope.ticker_list[0]
		if len(scope.ticker_list) > 1:
			st.error( 'Ticker List contains more that 1 ticker. Volume analysis to be performed on the first ticker only > ' + ticker_1)

		ticker_1_opening_time = scope.share_index_file.loc[ticker_1]['opening_time']
		ticker_1_minutes_per_day = scope.share_index_file.loc[ticker_1]['minutes_per_day']
		# Ticker 1
		st.header( ticker_1 + ' - ' + scope.share_index_file.loc[ticker_1]['company_name'] )
		ticker_1_current_volume = st.number_input("Current Volume", value=0, format="%d")
		# Build the open time for this ticker
		open_hour 	= int(ticker_1_opening_time[:2])
		open_minute = int(ticker_1_opening_time[3:5])
		open_second = int(ticker_1_opening_time[6:8])
		ticker_1_open_time=market_time.replace(hour=open_hour, minute=open_minute, second=open_second)
		# minutes difference
		diff_in_seconds = (market_time - ticker_1_open_time).total_seconds()
		minutes_elapsed = divmod(diff_in_seconds, 60)[0]
		if minutes_elapsed > ticker_1_minutes_per_day: minutes_elapsed = ticker_1_minutes_per_day
		# Now extrapolate
		ticker_1_average_vol_per_minute = ticker_1_current_volume / minutes_elapsed
		ticker_1_remaining_minutes = ticker_1_minutes_per_day - minutes_elapsed
		if ticker_1_remaining_minutes < 0: ticker_1_remaining_minutes = 0
		extrapolated_daily_volume = "{:8,.0f}".format(ticker_1_average_vol_per_minute * ticker_1_minutes_per_day)
		volume_to_date =  "{:8,.0f}".format(ticker_1_current_volume)
		
		# calc the closing time for this ticker
		ticker_1_closing_time = datetime.strptime(ticker_1_opening_time, '%H:%M:%S')
		ticker_1_closing_time = ticker_1_closing_time + timedelta(minutes=ticker_1_minutes_per_day)

		col1,col2,col3 = st.columns([1,1,1])

		with col1:st.write('Opening Time (for this ticker')
		with col2:st.write(str(ticker_1_open_time.strftime('%H:%M:%S %p')))
		with col3:st.write('-')

		with col1:st.write('Total Minutes Elapsed')
		with col2:st.write(str(minutes_elapsed))
		with col3:st.write('-')

		with col1:st.write('Remaining Minutes')
		with col2:st.write(str(ticker_1_remaining_minutes))
		with col3:st.write('-')

		with col1:st.write('Closing Time (for this ticker)')
		with col2:st.write(str(ticker_1_closing_time.strftime('%H:%M:%S %p')))
		with col3:st.write('-')

		with col1:st.write('Current Volume')
		with col2:st.write(str(volume_to_date))
		with col3:st.write('-')

		with col1:st.subheader('Average Volume per Minute')
		with col2:st.subheader(str(int(ticker_1_average_vol_per_minute)) )
		with col3:st.write('( ', str(volume_to_date), ' / ', str(minutes_elapsed), ' )')	

		with col1:st.subheader('Extrapolated End of Day Volume')
		with col2:st.subheader(str(extrapolated_daily_volume) )
		with col3:st.write('( '+ str(int(ticker_1_average_vol_per_minute))+' x '+ str(ticker_1_minutes_per_day)+' )')

	else:
		st.error('Currently No Tickers Selected - add a ticker to use this function')





