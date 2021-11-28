import streamlit as st



def input_volume():
	col1,col2 = st.columns([2,10])
	with col1: ticker_current_volume = st.number_input("Current Volume", value=0, format="%d")
	return ticker_current_volume



def view_prediction(ticker_open_time, minutes_elapsed, ticker_remaining_minutes, ticker_closing_time, 
						volume_to_date, ticker_average_vol_per_minute, extrapolated_daily_volume, ticker_minutes_per_day):
		# Render the results of the calculations
		col1,col2,col3 = st.columns([1,1,1])

		with col1:st.write('Opening Time (for this ticker')
		with col2:st.write(str(ticker_open_time.strftime('%H:%M:%S %p')))
		with col3:st.write('-')

		with col1:st.write('Total Minutes Elapsed')
		with col2:st.write(str(minutes_elapsed))
		with col3:st.write('-')

		with col1:st.write('Remaining Minutes')
		with col2:st.write(str(ticker_remaining_minutes))
		with col3:st.write('-')

		with col1:st.write('Closing Time (for this ticker)')
		with col2:st.write(str(ticker_closing_time.strftime('%H:%M:%S %p')))
		with col3:st.write('-')

		with col1:st.write('Current Volume')
		with col2:st.write(str(volume_to_date))
		with col3:st.write('-')

		with col1:st.subheader('Average Volume per Minute')
		with col2:st.subheader(str(int(ticker_average_vol_per_minute)) )
		with col3:st.write('( ', str(volume_to_date), ' / ', str(minutes_elapsed), ' )')	

		with col1:st.subheader('Extrapolated End of Day Volume')
		with col2:st.subheader(str(extrapolated_daily_volume) )
		with col3:st.write('( '+ str(int(ticker_average_vol_per_minute))+' x '+ str(ticker_minutes_per_day)+' )')

