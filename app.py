# ------------------------------------------------- Execute Application
# streamlit run app.py
# ------------------------------------------------- GitHub
# git push -u origin <branch>
# git branch -d <branch>   will delete local branch
# ------------------------------------------------- Package Management
# pip3 install --user --upgrade django
# pipenv install flask==0.12.1
# pipenv install mplfinance===0.12.7a5
# ------------------------------------------------- 

# Testing Code - TODO - delete later
from cgitb import handler
import pandas as pd
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)




import streamlit as st

from config.controller import set_scope
from pages.view.sidebar import render_sidebar
from pages.controller import render_selected_page

print ( '\033[94m' + 'Application Re-Rendering Now ' + '>'*50 + '\033[0m')

scope = set_scope(st.session_state)
render_sidebar(scope)						# Render the Sidebar
render_selected_page(scope)					# Render the selected Page






# Happy 60th Big Fella
# You have aged well
# It must be all that red wine keeping you well preserved
# Enjoy the celebrations. 
# Party hard
# All the best, Rob and Fliss






def terminal_heading(heading):
	print('')
	print('='*70)
	print(heading.upper(), '   ( level_1 )')
	print('='*70)


def level_2_details(level_1, level_2):
	# print('')
	print('-'*40)
	print(level_1, '/', level_2, ' ( level 2 )', )
	print('-'*40)
	if level_2 in st.session_state[level_1]:
		for key in st.session_state[level_1][level_2]:
			print(level_2 , ' - ', key)

def level_3_details(level_1, level_2, level_3):
	print('-'*50)
	print(level_1, '/', level_2, '/', level_3, ' ( level 3 )')
	print('-'*50)
	if level_2 in st.session_state[level_1]:
		if level_3 in st.session_state[level_1][level_2]:
			for key in st.session_state[level_1][level_2][level_3]:
				print(level_3 , ' - ', key)



if 'initial_load' in st.session_state:
	print('')
	terminal_heading('All keys in st.session_state')
	# for key in sorted(st.session_state):print(key)
	for key in st.session_state:print(key)


# level_1 = 'config'
# if level_1 in st.session_state:
# 	terminal_heading(level_1)
# 	for key in st.session_state[level_1]:print(key)
# 	level_2_details(level_1, 'dropdowns')
	# level_2_details(level_1, 'tests')
	# level_3_details(level_1, 'tests', 'trend_open')
# 	level_2_details(level_1, 'charts')
# 	level_3_details(level_1, 'charts', 'config')
# 	level_2_details(level_1, 'results')

# level_1 = 'files'
# if level_1 in st.session_state:
# 	terminal_heading(level_1)
# 	for key in st.session_state[level_1]:print(key)
# 	level_2_details(level_1, 'folders')
# 	level_2_details(level_1, 'paths')

# level_1 = 'data'
# if level_1 in st.session_state:
# 	terminal_heading(level_1)
# 	for key in st.session_state[level_1]:print(key)
# 	level_2_details(level_1, 'download')
\
level_1 = 'pages'
if level_1 in st.session_state:
	terminal_heading(level_1)
	for key in st.session_state[level_1]:print(key)
# 	level_2_details(level_1, 'templates')
# 	level_2_details(level_1, 'single')
# 	level_2_details(level_1, 'intraday')
# 	level_2_details(level_1, 'volume')
# 	level_2_details(level_1, 'research')
	level_2_details(level_1, 'screener')
	level_3_details(level_1, 'screener', 'selectors')
	

# level_1 = 'strategy'
# if level_1 in st.session_state:
# 	terminal_heading(level_1)
# 	for key in st.session_state[level_1]:print(key)
# 	level_2_details(level_1, 'header')
# 	level_2_details(level_1, 'print')

print ( '='*70)
print('screener/test_results')
print(st.session_state['pages']['screener']['test_results'])


print('data/download/yf_anomolies')
print(st.session_state['data']['download']['yf_anomolies'])
print ( '='*70)








# {'candlestick': {'active': True, 'name': 'CandleStick', 'is_overlay': False, 'add_overlays': True, 'plot': {'function': <function candle_plot at 0x7fdac710eaf0>, 'title': 'Price', 'scale': 1.0, 'yaxis': '$,.2f'}, 'metrics': None},
#  'scatter': {'active': False, 'name': 'Scatter', 'is_overlay': False, 'add_overlays': False, 'plot': {'function': None, 'title': '', 'scale': 0.8, 'yaxis': '$,.2f'}, 'metrics': None}, 'bar': {'active': False, 'name': 'Bar', 'is_overlay': False, 'add_overlays': False, 'plot': {'function': None, 'title': '', 'scale': 0.8, 'yaxis': '$,.2f'}, 'metrics': None}, 
#  'line': {'active': True, 'name': 'Line charts', 'is_overlay': False, 'add_overlays': True, 'plot': {'function': <function line_plot at 0x7fdac713e8b0>, 'title': 'Line', 'scale': 0.5, 'yaxis': '$,.2f'}, 'metrics': {'function': None, 'column': 'close'}}, 'heiken_ashi': {'active': False, 'name': 'Heikin Ashi', 'is_overlay': False, 'add_overlays': False, 'plot': {'function': None, 'title': '', 'scale': 0.8, 'yaxis': '$,.2f'}, 'metrics': None}, 
#  'volume': {'active': True, 'name': 'Volume', 'is_overlay': False, 'add_overlays': False, 'plot': {'function': <function volume_plot at 0x7fdac713ec10>, 'title': 'Volume', 'scale': 0.25, 'yaxis': ',.'}, 'metrics': None}, 'vol_per_minute': {'active': False, 'name': 'Volume Per Minute', 'is_overlay': False, 'add_overlays': False, 'plot': {'function': <function vpm_plot at 0x7fdac7191f70>, 'title': '', 'scale': 0.25, 'yaxis': ',.'}, 'metrics': None}, 
#  'vac': {'active': False, 'name': 'VAC', 'is_overlay': False, 'add_overlays': False, 'plot': {'function': None, 'title': '', 'scale': 0.25, 'yaxis': ',.'}, 'metrics': None}, 
#  'macd': {'active': True, 'name': 'MACD', 'is_overlay': False, 'add_overlays': False, 'plot': {'function': <function macd_plot at 0x7fdac71a3310>, 'title': 'MACD', 'scale': 0.5, 'yaxis': ',.'},  'metrics': {'function': <function macd_cols at 0x7fdac71a2a60>, 
#  'column': 'close', 'long': 26, 'short': 12, 'signal': 9}}, 'macd_vol': {'active': True, 'name': 'MACD on Volume', 'is_overlay': False, 'add_overlays': False, 'plot': {'function': <function macd_vol_plot at 0x7fdac71bb0d0>, 'title': 'MACD (Volume)', 'scale': 0.5, 'yaxis': ',.'}, 'metrics': {'function': <function macd_vol_cols at 0x7fdac71a3a60>, 
#  'column': 'volume', 'long': 26, 'short': 12, 'signal': 9}}, 'rsi': {'active': True, 'name': 'RSI', 'is_overlay': False, 'add_overlays': False, 'plot': {'function': <function rsi_plot at 0x7fdac71bea60>, 'title': 'RSI', 'scale': 0.5, 'yaxis': '.0%'}, 'metrics': {'function': <function rsi_cols at 0x7fdac70ef5e0>, 'column': 'close', 'lookback_days': 10}}, 
#  'vol_osssy': {'active': False, 'name': 'Volume Oscillator', 'is_overlay': False, 'add_overlays': False, 'plot': {'function': None, 'title': '', 'scale': 0.75, 'yaxis': '$,.2f'}, 'metrics': {'function': None, 'column': 'volume', 'fast': 14, 'slow': 21}}, 'stochastic': {'active': True, 'name': 'Stochastic', 'is_overlay': False, 'add_overlays': False, 'plot': {'function': <function stoch_plot at 0x7fdac71435e0>, 'title': 'Stochastic', 'scale': 0.5, 'yaxis': '.0%'}, 'metrics': {'function': <function stoch_cols at 0x7fdac71beaf0>, 'lookback_days': 14, 'slow': 3, 'signal': 3}}, 
#  'sma_1': {'active': False, 'name': 'SMA-1', 'is_overlay': True, 'add_overlays': False, 'plot': {'function': <function sma_plot at 0x7fdac7152ca0>, 'colour': 'blue'}, 'metrics': {'function': <function sma_cols at 0x7fdac71524c0>, 'column': 'close', 'periods': 21}}, 
#  'sma_2': {'active': False, 'name': 'SMA-2', 'is_overlay': True, 'add_overlays': False, 'plot': {'function': <function sma_plot at 0x7fdac7152ca0>, 'colour': 'green'}, 'metrics': {'function': <function sma_cols at 0x7fdac71524c0>, 'column': 'close', 'periods': 50}}, 
#  'sma_3': {'active': False, 'name': 'SMA-3', 'is_overlay': True, 'add_overlays': False, 'plot': {'function': <function sma_plot at 0x7fdac7152ca0>, 'colour': 'green'}, 'metrics': {'function': <function sma_cols at 0x7fdac71524c0>, 'column': 'close', 'periods': 200}}, 
#  'ema_1': {'active': False, 'name': 'EMA-1', 'is_overlay': True, 'add_overlays': False, 'plot': {'function': <function ema_plot at 0x7fdac71523a0>, 'colour': 'red'}, 'metrics': {'function': <function ema_cols at 0x7fdac717d9d0>, 'column': 'close', 'periods': 21}}, 
#  'ema_2': {'active': False, 'name': 'EMA-2', 'is_overlay': True, 'add_overlays': False, 'plot': {'function': <function ema_plot at 0x7fdac71523a0>, 'colour': 'blue'}, 'metrics': {'function': <function ema_cols at 0x7fdac717d9d0>, 'column': 'close', 'periods': 50}}, 
#  'ema_3': {'active': False, 'name': 'EMA-3', 'is_overlay': True, 'add_overlays': False, 'plot': {'function': <function ema_plot at 0x7fdac71523a0>, 'colour': 'SteelBlue'}, 'metrics': {'function': <function ema_cols at 0x7fdac717d9d0>, 'column': 'close', 'periods': 200}}, 'bollinger_bands': {'active': False, 'name': 'Bollinger Bands', 'is_overlay': True, 'add_overlays': False, 'plot': {'function': <function sma_plot at 0x7fdac7152ca0>, 'colour': 'black'}, 'metrics': {'function': <function ema_cols at 0x7fdac717d9d0>, 'column': 'close', 'length': 20, 'shift_up': 2, 'shift_down': 2, 'm_a_type': 'simple'}},
#   'dividends': {'active': True, 'name': 'Dividends', 'is_overlay': True, 'add_overlays': False, 'plot': {'function': <function dividend_plot at 0x7fdac724b1f0>, 'colour': 'blue'}, 'metrics': {'function': <function dividend_cols at 0x7fdac71cd940>}}, 'announcements': {'active': False, 'name': 'Announcements', 'is_overlay': True, 'add_overlays': False, 'plot': {'function': <function sma_plot at 0x7fdac7152ca0>, 'colour': 'black'}, 'metrics': None}, 
#  'ichi_moku': {'active': False, 'name': 'Icki Moku', 'is_overlay': True, 'add_overlays': False, 'plot': {'function': <function sma_plot at 0x7fdac7152ca0>, 'colour': 'black'}, 'metrics': None}, 'ichi_moku_daily': {'active': False, 'name': 'Icki Moku Daily', 'is_overlay': True, 'add_overlays': False, 'plot': {'function': <function sma_plot at 0x7fdac7152ca0>, 'colour': 'black'}, 'metrics': None}}


# {
# 	'trend_open': {'active': False, 'name': 'Open trend', 'column': 'open', 'trend': 'up', 'duration': 4, 'timespan': 10, 'metrics': {'function': <function trend_cols at 0x7fdac7266af0>}}, 
# 	'trend_high': {'active': True, 'name': 'High trend', 'column': 'high', 'trend': 'up', 'duration': 7, 'timespan': 5, 'metrics': {'function': <function trend_cols at 0x7fdac7266af0>}}, 
# 	'trend_low': {'active': False, 'name': 'Low trend', 'column': 'low', 'trend': 'up', 'duration': 4, 'timespan': 10, 'metrics': {'function': <function trend_cols at 0x7fdac7266af0>}},
# 	'trend_close': {'active': False, 'name': 'Close trend', 'column': 'close', 'trend': 'up', 'duration': 4, 'timespan': 10, 'metrics': {'function': <function trend_cols at 0x7fdac7266af0>}}, 
# 	'trend_volume': {'active': False, 'name': 'Volume trend', 'column': 'volume', 'trend': 'up', 'duration': 4, 'timespan': 10, 'metrics': {'function': <function trend_cols at 0x7fdac7266af0>}}}










# # Set Up the Initial Streamlit Environment ======================================================================
# from config.streamlit import set_streamlit_page_config
# from scope.scope import set_scope
# from pages.controller import set_initial_scope
# from scope.dropdowns.refresh_selectors import update_dropdowns


# set_streamlit_page_config()
# scope = set_scope(st.session_state, project_description)

# if scope.config['dropdowns']['update_dropdowns']: 
# 	update_dropdowns(scope)

# print ( '\033[94mApplication Refreshed >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> \033[0m')

# render_selected_page(scope)
# render_sidebar(scope)


