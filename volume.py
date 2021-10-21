import datetime


def average_volume(st):
	st.title('Extrapolating the Current Volume to the End of today')

	# Current time
	current_time=datetime.datetime.today()
	st.info('Current Time = '+ current_time.strftime('%Y-%m-%d %H:%M:%S %p') )
	
	# -----------------------------------------------------------------------------------
	# Extract master data from share index file for Ticker 1
	ticker_1 = st.session_state.ticker_list[0]
	ticker_1_opening_time = st.session_state.share_index_file.loc[ticker_1]['opening_time']
	ticker_1_minutes_per_day = st.session_state.share_index_file.loc[ticker_1]['minutes_per_day']
	# Ticker 1
	st.header( ticker_1 + ' - ' + st.session_state.share_index_file.loc[ticker_1]['company_name'] )
	ticker_1_current_volume = st.number_input("Current Volume", value=0, format="%d")
	# Build the open time for this ticker
	open_hour = int(ticker_1_opening_time[:2])
	open_minute = int(ticker_1_opening_time[3:5])
	ticker_1_open_time=current_time.replace(hour=open_hour, minute=open_minute)
	# minutes difference
	diff_in_seconds = (current_time - ticker_1_open_time).total_seconds()
	minutes_elapsed = divmod(diff_in_seconds, 60)[0]
	if minutes_elapsed > ticker_1_minutes_per_day: minutes_elapsed = ticker_1_minutes_per_day
	# Now extrapolate
	ticker_1_average_vol_per_minute = ticker_1_current_volume / minutes_elapsed
	ticker_1_remaining_minutes = ticker_1_minutes_per_day - minutes_elapsed
	if ticker_1_remaining_minutes < 0: ticker_1_remaining_minutes = 0
	extrapolated_daily_volume = "{:8,.0f}".format(ticker_1_average_vol_per_minute * ticker_1_minutes_per_day)
	volume_to_date =  "{:8,.0f}".format(ticker_1_current_volume)

	
	col1,col2 = st.columns([3,4])
	with col1: 
		st.write('Opening Time')
		st.write('Total Minutes Elapsed')
		st.write('Current Volume')
		st.write('Average Volume per Minute')
		st.write('Remaining Minutes')
		st.write('Extrapolated EOD Volume')

	with col2: 
		st.write(str(ticker_1_open_time.strftime('%Y-%m-%d %H:%M:%S %p')))
		st.write(str(minutes_elapsed))
		st.write(str(volume_to_date))
		st.write(str(int(ticker_1_average_vol_per_minute)) + ' ..........( ', str(volume_to_date), ' / ', str(minutes_elapsed), ' )')
		st.write(str(ticker_1_remaining_minutes))
		st.write(str(extrapolated_daily_volume) + ' .........( '+ str(int(ticker_1_average_vol_per_minute))+' x '+ str(ticker_1_minutes_per_day)+' )')
		st.write()






