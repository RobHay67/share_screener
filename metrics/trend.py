
import numpy as np


def trend_cols(scope, screener_df, test):

	column 		= scope.config['tests'][test]['add_columns']['column']
	trend 		= scope.config['tests'][test]['add_columns']['trend']
	duration	= int(scope.config['tests'][test]['add_columns']['duration'])
	timespan 	= int(scope.config['tests'][test]['add_columns']['timespan'])
	
	screener_df['temp_shifted'] = screener_df[column].shift(1)
	screener_df['temp_shifted'] = screener_df['temp_shifted'].fillna(0.0).astype(float)
	if trend == 'up':
		screener_df['temp_trend'] = np.where( screener_df[column] > screener_df['temp_shifted'], 1, 0 )
	else:
		screener_df['temp_trend'] = np.where( screener_df[column] < screener_df['temp_shifted'], 1, 0 )

	screener_df['temp_trend_total'] = screener_df['temp_trend'].rolling(timespan, min_periods=1).sum().astype(int)

	screener_df[test] = np.where( screener_df['temp_trend_total'] >= duration, 'passed', 'failed')

	screener_df.drop(['temp_shifted', 'temp_trend', 'temp_trend_total'], axis=1, inplace=True)








# this was the old code
def recent_price_moves( params, share_df, lookback_days=5 ):
	for column in params.strategy['price_columns'] + ['volume']:
		# lets just say the column = 'close'

		# report_function( params, f'Price direction on {column} today and over the past {lookback_days} days' )
		trend_col_name = 'c_' + str(column[:1])
		lookback_col_name = 'lb_' + str(column[:1])		
		share_df['yesterday'] = np.where( share_df[column] > share_df[column].shift(1), 1, 0 )
		share_df[trend_col_name] = np.where( share_df['yesterday'] == 1, 'U', 'D' )
		share_df[lookback_col_name] = share_df['yesterday'].rolling(lookback_days, min_periods=1).sum().astype(int)
		share_df.drop([ 'yesterday'], axis=1, inplace=True)	
	return share_df



# this would say look at the close price
#   close		yesterday	trend_col_name	lookback_col_name
#							< c_close >		< lb_close >
#   12.5		1			U				0
#	12.8		1			U				0
#	12.9		1			U				1
#	12.85		0			D				0
#				< dropped >


# This is Fliss simple strategy

def fliss_simple():
	lookback_days = 3

	for ticker in params.share_data['files']:
		analysis_df = params.share_data['files'][ticker].copy()	
		analysis_df = recent_price_moves( params, analysis_df )

		if len( analysis_df)> lookback_days:
			# volume
			analysis_df['volume_shifted'] = analysis_df['volume'].shift(1)
			analysis_df['volume_shifted'] = analysis_df['volume_shifted'].fillna(0).astype(int)
			analysis_df['volume_up'] = np.where( analysis_df['volume'] > analysis_df['volume_shifted'], 1, 0 )
			result_volume_up_days = 0
			for i in range( 1, lookback_days+1 ):
				if analysis_df.iloc[-i]['volume_up'] == 1: 
					result_volume_up_days += 1
			# close
			analysis_df['close_shifted'] = analysis_df['close'].shift(1)
			analysis_df['close_shifted'] = analysis_df['close_shifted'].fillna(0.0).astype(float)
			analysis_df['close_up'] = np.where( analysis_df['close'] > analysis_df['close_shifted'], 1, 0 )
			result_close_up_days = 0
			for i in range( 1, lookback_days+1 ):
				if analysis_df.iloc[-i]['close_up'] == 1: result_close_up_days += 1
					
			# do the analysis
			analysis_df['recommendation'] = np.where(
													( result_volume_up_days == lookback_days ) &		# RSI is 50% or above
													( result_close_up_days  == lookback_days )
													, 'buy_this_one', 'fails_criteria'
												) 
			params.strategy['results'][ticker] = analysis_df



# this would say look at the close price
# lookback_days = 3
#   close		close_shifted	close_up	lookback_col_name
#												< lb_close >
#   12.5		0.0				1				0
#	12.8		12.5			1				0
#	12.9		12.8			1				1
#	12.85		12.9			0				0
#				< dropped >