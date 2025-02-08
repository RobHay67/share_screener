import logging
# import logging.config
from config.helpers.scope_keys import print_scope_keys

# tag the info components


def set_logging_config(to_terminal=True):
	logging.basicConfig(
						# level=logging.DEBUG,							# Render minor components (buttons)
						level=logging.INFO,							# Render Pages and main components (controllers / routers)
						# level=logging.WARNING,						# Basic Python Code / Functions
						# level=logging.ERROR,							# Actual errors (captured but not expected)
						# level=logging.CRITICAL,						# TODO and code currently being worked upon
						format="{asctime} - {levelname} - {message}",
						style="{",
						datefmt="%Y-%m-%d %H:%M:%S",
						# filename="screener.log",
						# encoding="utf-8",
						# filemode="a",			# a = append (to log file)
						)
	
	print_scope_keys('streamlit_app')
	logging.warning("set_logging_config")

	logging.critical("Download and Save the dividend data to this app")


# Logging Levels
# logging.comp			"This is a component message = 5"			# For the render components
# logging.render		"This is a major render controller"			# For the main pages and main components that are being rendered		
# logging.debug(		"This is a debug message = 10")				# minimum on every function
# logging.info(			"This is an info message = 20")				# A change is being made to a file or data  
# logging.warning(		"This is a warning message = 30")			# TODO - warn that this need coding
# logging.error(		"This is an error message = 40")			# An actual error message
# logging.critical(		"This is a critical message = 50")			# Something that need to be fixed and soon



# logging.debug(		render components
# logging.info(			render main pages and main compoenets (controller and routers)

# logging.warning(		the basic debug message - what is running
# logging.error(		actual errors and anomolies
# logging.critical(		TODO things that are currently in progress



# def set_logging_config(to_terminal=True):
# 	LOGGING_CONFIG = {
# 			'version': 1,
# 			'disable_existing_loggers': False,
# 			'formatters': {
# 				'default': {
# 					#'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',			
# 					'format':  '%(asctime)s - %(levelname)s - %(message)s',
# 				},
# 			},
# 			'handlers': {
# 				'file': {
# 					'level': 'DEBUG',
# 					'class': 'logging.FileHandler',
# 					'filename': 'screener.log',
# 					'formatter': 'default',
# 				},
# 				'stdout': {
# 					'level': 'DEBUG',
# 					'class': 'logging.StreamHandler',
# 					'formatter': 'default',
# 				},
# 			},
# 			'loggers': {
# 				'Screener_App': {
# 					'handlers': ['file', 'stdout'],
# 					'level': 'DEBUG',
# 					'propagate': True,
# 				},
# 			},
# 		}
# 	logging.config.dictConfig(LOGGING_CONFIG)
# 	log = logging.getLogger('Screener_App')
# 	log.debug('Debug message: Initializing GeeksforGeeks module.')
# 	log.info('Info message: GeeksforGeeks module loaded successfully.')
# 	log.warning('Warning message: GeeksforGeeks module is using deprecated functions.')
# 	log.error('Error message: GeeksforGeeks module encountered an error.')
# 	log.critical('Critical message: GeeksforGeeks module failed to load.')


