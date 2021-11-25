import streamlit as st




# candlestick
#	close above open for the past X days

# line and volume
# 	COLUMN > (HIGHER or LOWER) > last X days

# MACD
#		trending UP or DOWN
#		crossed UP or DOWN
# 		hostogram is STRONG or WEAK



# SMA and EMA
# 	for COLUMN trading ABOVE or BELOW this average


# RSI
#	COLUMN in the BUY / SELL / MIDDLE range

# Stochastic
# 	COLUMN in the BUY / SELL / MIDDLE range
#	COLUMN crossed UP or DOWN




def scope_analysis(scope):
	
	scope.analysis_row_limit 	= 100


	scope.volume_trend = 'up'
	scope.volume_lookback_days = 3



	scope.rsi_level = 0.50
	scope.rsi_column = 'close'

	scope.macd_direction = 'up'
	scope.macd_strength = 'strong'


	scope.sma_line = 'above'
	scope.ema_line = 'above'













