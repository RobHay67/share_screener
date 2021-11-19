import streamlit as st
from datetime import datetime
from datetime import timedelta
import pytz

from config.markets import opening_hours

from analysis.volume.times import view_local_vs_market_time

from analysis.volume.view import prediction

def volume_prediction(scope):
	ticker = scope.selected['volume']['ticker_list'][0]

	local_time=datetime.now()											# Current local time
	market_timezone = opening_hours[scope.share_market]['timezone']		# Timezone for the share market
	market_time = datetime.now(pytz.timezone(market_timezone))			# Current Market time
	view_local_vs_market_time(local_time, market_time)

	if ticker != 'select a ticker':
		# Current Volume Level - Input by the User
		col1,col2 = st.columns([2,10])
		with col1: ticker_current_volume = st.number_input("Current Volume", value=0, format="%d")

		###########################################################################################
		# Predict Total Daily Volume based on current Volume and known information about the ticker
		###########################################################################################

		# Relevant Times for this Ticker
		ticker_opening_time 	= scope.ticker_index.loc[ticker]['opening_time']
		ticker_minutes_per_day 	= scope.ticker_index.loc[ticker]['minutes_per_day']
						
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

		# TODO - we could use a POC model over the recent history and plot the prediction against this - we could smooth in accordance with the POC curve

		prediction( ticker_open_time, minutes_elapsed, ticker_remaining_minutes, ticker_closing_time, 
							volume_to_date, ticker_average_vol_per_minute, extrapolated_daily_volume, ticker_minutes_per_day)


