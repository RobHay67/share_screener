
import pandas as pd
import os
import json


def load_user_table(scope):
	print(scope.files['paths']['users'])

	if os.path.exists( scope.files['paths']['users'] ):
		file = open(scope.files['paths']['users'])
		user_table = json.load(file)

		list_of_users = list(user_table.keys())

		scope.users['json'] = user_table
		scope.users['user_list'] = list_of_users
	else:
		print('='*77)
		print('ERROR - Users File does not exist > ', scope.files['paths']['users'])
		print('='*77)
		quit()




# {"Rob": 
# 	{"password": "password", "chart_height": 500, "download_days": 7, "row_limit": 100,	"tests": 
# 		{"trend_open": 
# 			{"active": true, "add_columns":
# 			 {"column": "open", "trend": "up", "duration": 4, "timespan": 10}}, "trend_high": {"active": true, "add_columns": {"column": "high", "trend": "up", "duration": 5, "timespan": 50}}, "trend_low": {"active": false, "add_columns": {"column": "low", "trend": "up", "duration": 4, "timespan": 10}}, "trend_close": {"active": true, "add_columns": {"column": "close", "trend": "down", "duration": 2, "timespan": 10}}, "trend_volume": {"active": false, "add_columns": {"column": "volume", "trend": "up", "duration": 4, "timespan": 10}}}, "charts": {"candlestick": {"active": true, "add_columns": null}, "scatter": {"active": false, "add_columns": null}, "bar": {"active": false, "add_columns": null}, "line": {"active": true, "add_columns": null}, "heiken_ashi": {"active": false, "add_columns": null}, "volume": {"active": true, "add_columns": null}, "vol_per_minute": {"active": true, "add_columns": null}, "vac": {"active": false, "add_columns": null}, "macd": {"active": true, "add_columns": {"column": "close", "long": 26, "short": 12, "signal": 9}}, "macd_vol": {"active": true, "add_columns": {"column": "volume", "long": 26, "short": 12, "signal": 9}}, "rsi": {"active": true, "add_columns": {"column": "close", "lookback_days": 10}}, "vol_osssy": {"active": false, "add_columns": {"column": "volume", "fast": 14, "slow": 21}}, "stochastic": {"active": true, "add_columns": {"lookback_days": 14, "slow": 3, "signal": 3}}, "sma_1": {"active": true, "add_columns": {"column": "close", "periods": 21}}, "sma_2": {"active": false, "add_columns": {"column": "close", "periods": 50}}, "sma_3": {"active": false, "add_columns": {"column": "close", "periods": 200}}, "ema_1": {"active": false, "add_columns": {"column": "close", "periods": 21}}, "ema_2": {"active": false, "add_columns": {"column": "close", "periods": 50}}, "ema_3": {"active": false, "add_columns": {"column": "close", "periods": 200}}, "bollinger_bands": {"active": false, "add_columns": {"column": "close", "length": 20, "shift_up": 2, "shift_down": 2, "m_a_type": "simple"}}, "dividends": {"active": true, "add_columns": {}}, "announcements": {"active": false, "add_columns": null}, "ichi_moku": {"active": false, "add_columns": null}, "ichi_moku_daily": {"active": false, "add_columns": null}}}, "Fliss": {"password": "password", , "chart_height": 500, "download_days": 7, "row_limit": 100, "tests": {"trend_open": {"active": false, "add_columns": {"column": "open", "trend": "up", "duration": 4, "timespan": 10}}, "trend_high": {"active": true, "add_columns": {"column": "high", "trend": "up", "duration": 5, "timespan": 50}}, "trend_low": {"active": false, "add_columns": {"column": "low", "trend": "up", "duration": 4, "timespan": 10}}, "trend_close": {"active": false, "add_columns": {"column": "close", "trend": "down", "duration": 2, "timespan": 10}}, "trend_volume": {"active": false, "add_columns": {"column": "volume", "trend": "up", "duration": 4, "timespan": 10}}}, "charts": {"candlestick": {"active": true, "add_columns": null}, "scatter": {"active": false, "add_columns": null}, "bar": {"active": false, "add_columns": null}, "line": {"active": true, "add_columns": null}, "heiken_ashi": {"active": false, "add_columns": null}, "volume": {"active": true, "add_columns": null}, "vol_per_minute": {"active": true, "add_columns": null}, "vac": {"active": false, "add_columns": null}, "macd": {"active": true, "add_columns": {"column": "close", "long": 26, "short": 12, "signal": 9}}, "macd_vol": {"active": true, "add_columns": {"column": "volume", "long": 26, "short": 12, "signal": 9}}, "rsi": {"active": true, "add_columns": {"column": "close", "lookback_days": 10}}, "vol_osssy": {"active": false, "add_columns": {"column": "volume", "fast": 14, "slow": 21}}, "stochastic": {"active": true, "add_columns": {"lookback_days": 14, "slow": 3, "signal": 3}}, "sma_1": {"active": true, "add_columns": {"column": "close", "periods": 21}}, "sma_2": {"active": false, "add_columns": {"column": "close", "periods": 50}}, "sma_3": {"active": false, "add_columns": {"column": "close", "periods": 200}}, "ema_1": {"active": false, "add_columns": {"column": "close", "periods": 21}}, "ema_2": {"active": false, "add_columns": {"column": "close", "periods": 50}}, "ema_3": {"active": false, "add_columns": {"column": "close", "periods": 200}}, "bollinger_bands": {"active": false, "add_columns": {"column": "close", "length": 20, "shift_up": 2, "shift_down": 2, "m_a_type": "simple"}}, "dividends": {"active": true, "add_columns": {}}, "announcements": {"active": false, "add_columns": null}, "ichi_moku": {"active": false, "add_columns": null}, "ichi_moku_daily": {"active": false, "add_columns": null}}}}