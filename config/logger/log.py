import logging
from config.helpers.scope_keys import print_scope_keys


def set_logging_config(to_terminal=True):
	logging.basicConfig(
						level=logging.DEBUG,
						format="{asctime} - {levelname} - {message}",
						style="{",
						datefmt="%Y-%m-%d %H:%M:%S",
						# filename="screener.log",
						# encoding="utf-8",
						# filemode="a",			# a = append (to log file)
						
						)
	
	print_scope_keys('streamlit_app')
	logging.info("set_logging_config")


# Logging Levels
# logging.debug(		"This is a debug message = 10")
# logging.info(			"This is an info message = 20")
# logging.warning(		"This is a warning message = 30")
# logging.error(		"This is an error message = 40")
# logging.critical(		"This is a critical message = 50")






	# LOGGING_CONFIG = {
	# 		'version': 1,
	# 		'disable_existing_loggers': False,
	# 		'formatters': {
	# 			'default': {
	# 				'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
	# 			},
	# 		},
	# 		'handlers': {
	# 			'file': {
	# 				'level': 'DEBUG',
	# 				'class': 'logging.FileHandler',
	# 				'filename': 'geeksforgeeks.log',
	# 				'formatter': 'default',
	# 			},
	# 			'stdout': {
	# 				'level': 'DEBUG',
	# 				'class': 'logging.StreamHandler',
	# 				'formatter': 'default',
	# 			},
	# 		},
	# 		'loggers': {
	# 			'GeeksforGeeksLogger': {
	# 				'handlers': ['file', 'stdout'],
	# 				'level': 'DEBUG',
	# 				'propagate': True,
	# 			},
	# 		},
	# 	}
	# logging.config.dictConfig(LOGGING_CONFIG)
	# logger = logging.getLogger('GeeksforGeeksLogger')
	# logging.debug('Debug message: Initializing GeeksforGeeks module.')
	# logging.info('Info message: GeeksforGeeks module loaded successfully.')
	# logging.warning('Warning message: GeeksforGeeks module is using deprecated functions.')
	# logging.error('Error message: GeeksforGeeks module encountered an error.')
	# logging.critical('Critical message: GeeksforGeeks module failed to load.')
