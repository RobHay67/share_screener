import logging
import sys
import streamlit
import pandas
import yfinance
import matplotlib
import plotly
import pytz
import streamlit_extras



def print_system_info_to_terminal():
	logging.warning("print_system_info_to_terminal")
	print ( '\033[94m')
	print('='*100)
	print ( 'EXPECTED Python Verion  = 3.13.13')
	print ( 'ACTUAL Version      	=', sys.version )
	print ( 'Python Executable     	=', sys.executable )  
	print ( 'Environment Version   	=', sys.prefix )
	print('-'*100)
	print ( 'Streamlit               =', streamlit.__version__)
	print ( 'Pandas                  =', pandas.__version__)
	print ( 'YFinance                =', yfinance.__version__)
	print ( 'MatPlotLib              =', matplotlib.__version__)
	print ( 'Plotly                  =', plotly.__version__)
	print ( 'pytz                    =', pytz.__version__)
	print ( 'Streamlit Extras        =', streamlit_extras.__version__)
	logging.critical("Rob we need to lock these versions into the pipfile prior to production release")
	print('='*100)
	print ( '\33[0m')
	for i in range(5):print('')





# [packages]
# pandas = "==1.5.3"
# streamlit = "*"
# datetime = "*"
# yfinance = "==0.2.14"
# mplfinance = "===0.12.7a5"
# matplotlib = "*"
# plotly = "*"
# pytz = "==2023.3"
# watchdog = "*"
# streamlit-extras = "*"
# jinja2 = "*"

# [dev-packages]

# [requires]
# python_version = "3.8"