import logging



def app_is_re_rendering():
	logging.debug("app_is_re_rendering ================")
	for i in range(10):print('')
	print ( '\033[94m' + 'Application Re-Rendering - see below this line ' + '>'*33 + '\033[0m')
	for i in range(5):print('')