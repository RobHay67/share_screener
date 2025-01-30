


def build_english_explanation(scope, trial ):
	english_explanation = ''
	dict_of_values = scope.trials['user_config'][trial]['function']
	column = dict_of_values['column'] if 'column' in dict_of_values else None
	trend = dict_of_values['trend'] if 'trend' in dict_of_values else None
	duration = dict_of_values['duration'] if 'duration' in dict_of_values else None
	timespan = dict_of_values['timespan'] if 'timespan' in dict_of_values else None
	periods = dict_of_values['periods'] if 'periods' in dict_of_values else None
	lookback_days = dict_of_values['lookback_days'] if 'lookback_days' in dict_of_values else None
	slow = dict_of_values['slow'] if 'slow' in dict_of_values else None
	signal = dict_of_values['signal'] if 'signal' in dict_of_values else None
	

	if trial in ['price_1', 'price_2', 'price_3']:
		column_name = scope.ticker_schema['schema'][column]['long_english']
		english_explanation =  f"{column_name} is {trend}, {duration} of the previous {timespan} days"

	if trial in ['sma_1', 'sma_2', 'sma_3']:
		column_name = scope.ticker_schema['schema'][column]['long_english']
		english_explanation =  f"{column_name} is trading {trend} the {periods} day Simple Moving Average (SMA)"

	if trial in ['stochastic_1', 'stochastic_2', 'stochastic_3']:

		english_explanation = 'STOCHASTIC'

	if trial in ['rsi_1', 'rsi_2']:
		column_name = scope.ticker_schema['schema'][column]['long_english']

		# buy and sell zone
		if trend in ['up ','down']:
			english_explanation =  f"{column_name} is trending {trend} on the Relative Strength Index (RSI) with a lookback period of  {lookback_days} days."
		else:
			trend = trend.upper()
			english_explanation =  f"{column_name} is in the {trend} zone of the Relative Strength Index (RSI) with a lookback period of  {lookback_days} days."


	return english_explanation