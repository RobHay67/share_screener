import streamlit as st


def show_active_trials(scope):

	st.divider()
	st.subheader('Currently Active Trials / Tests')

	st.write('https://www.investopedia.com/articles/active-trading/041814/four-most-commonlyused-indicators-trend-trading.asp')

	first_row = True
	col1,col2,col3,col4,col5 = st.columns([2,1,7,1,1])
	# headings
	with col1:st.caption('Trial Name')
	with col2:st.caption('-- and ---')
	with col3:st.caption('Criteria (english explanation)')
	with col4:st.caption('Link to Definition')
	with col5:st.caption('Config Ref')
	st.divider()

	for trial in scope.trials['active_list']:

		connector = 'and ------- >'
		english_explanation = ''
		dict_of_values = scope.trials['user_config'][trial]['add_columns']
		column = dict_of_values['column'] if 'column' in dict_of_values else None
		trend = dict_of_values['trend'] if 'trend' in dict_of_values else None
		duration = dict_of_values['duration'] if 'duration' in dict_of_values else None
		timespan = dict_of_values['timespan'] if 'timespan' in dict_of_values else None
		periods = dict_of_values['periods'] if 'periods' in dict_of_values else None
		lookback_days = dict_of_values['lookback_days'] if 'lookback_days' in dict_of_values else None
		slow = dict_of_values['slow'] if 'slow' in dict_of_values else None
		signal = dict_of_values['signal'] if 'signal' in dict_of_values else None
		definition = scope.trials['user_config'][trial]['definition']
		# print(definition)
		
		with col1: st.write(scope.trials['user_config'][trial]['short_name'])
		
		# st.write(scope.pages['ticker_values'])
		
		if trial in ['price_1', 'price_2', 'price_3']:
			column_name = scope.pages['ticker_values'][column]['long_english']
			english_explanation =  f"{column_name} is {trend}, {duration} of the previous {timespan} days"

		if trial in ['sma_1', 'sma_2', 'sma_3']:
			column_name = scope.pages['ticker_values'][column]['long_english']
			english_explanation =  f"{column_name} is trading {trend} the {periods} day Simple Moving Average (SMA)"

		if trial in ['stochastic_1', 'stochastic_2', 'stochastic_3']:

			english_explanation = 'STOCHASTIC'

		if trial in ['rsi_1', 'rsi_2']:
			column_name = scope.pages['ticker_values'][column]['long_english']

			# buy and sell zone
			if trend in ['up ','down']:
				english_explanation =  f"{column_name} is trending {trend} on the Relative Strength Index (RSI) with a lookback period of  {lookback_days} days."
			else:
				trend = trend.upper()
				english_explanation =  f"{column_name} is in the {trend} zone of the Relative Strength Index (RSI) with a lookback period of  {lookback_days} days."
			
		if first_row:
			connector= '....'
			first_row = False
		
		with col2: st.write(connector)
		with col3: st.write(english_explanation)
		with col4: st.write("[defintion]("+definition+")")
		with col5: st.write(trial)

	st.subheader('Fliss Simple Strategy')
	st.write('Closing Price is up n times over the last x days')
	st.write('Volume is up n times over the last x days')


